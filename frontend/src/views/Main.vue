<template>
<div>
  <v-app id="keep">
    <v-app-bar
      app
      clipped-left
      color="#1a4b7e"
      dark
    >
    <v-app-bar-nav-icon @click="toogleDrawer()"/>
      <span class="title ml-3 mr-5" v-if="!isMobil">
        Heimabend&nbsp;
        <span class="font-weight-light">
          Inspirator
        </span>
      </span>

      <v-text-field
        class="px-3"
        v-model="searchInput"
        outlined
        hide-details
        :label="getLabel"
        prepend-inner-icon="mdi-magnify"
        clearable
        :dense="isMobil"
      />
      <v-spacer />
      <img v-on:click="onLoginClick" class="mr-2" :src="require('../assets/logo.gif')" height="50"/>


    </v-app-bar>

    <MenuLeft
      ref="mainMenuLeft"
      :levelFilter="levelFilter"
      :tags="tags"
      @onTagFilterChanged="onTagFilterChanged"
      @openImpressum="onImpressumClick"
      @openAboutProject="onAboutProjectClick"
      @onLevelFilterChanged="onLevelFilterChanged"
      @tagOverview="onTagOverviewClick"
    />

    <v-content id="lateral">
      <Topbar
        ref="topFilterToolbar"
        :levelFilter="levelFilter"
        :tags="tags"
        @openImpressum="onImpressumClick"
        @openAboutProject="onAboutProjectClick"
        @onLevelFilterChanged="onLevelFilterChanged"
        @tagOverview="onTagOverviewClick"
      />
      <div class="row mx-2" justify="center">
        <div class="col-sm-12">
          <HeimabendCard
            :items="getItems"
            :isMobil="isMobil"
            @onUpdateClick="onUpdateClick"
          />
          <v-btn
            class="ma-10"
            v-if="!getItems.length"
            @click="onResetClick()"
          >
            Alle Filter zurücksetzen
          </v-btn>
        </div>
   <v-fab-transition>
      <v-btn
      @click="onNewClick"
        fab
        color="green"
        dark
        fixed
        bottom
        right
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-fab-transition>
      </div>
    </v-content>

    <CreateDialog
      ref="createGroupClassModal"
      @dialogClose="onDialogClose"
      :tags="tags"
    />
    <Tags
      ref="tagsOverview"
      @dialogClose="onDialogClose"
    />
    <Impressum
      ref="impressumDialog"
    />
    <AboutProject
      ref="aboutProject"
    />
    <Login
      ref="login"
    />
  </v-app>
</div>
</template>

<script>
import axios from 'axios';

import CreateDialog from './components/dialogs/CreateDialog.vue';
import Login from './components/dialogs/Login.vue'; // eslint-disable-line
import Impressum from './components/dialogs/Impressum.vue';
import Tags from './tags/Main.vue';
import AboutProject from './components/dialogs/AboutProject.vue';
import HeimabendCard from './components/cards/Heimabend.vue';
import MenuLeft from './components/menu/Left.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';

export default {
  components: {
    CreateDialog,
    AboutProject,
    HeimabendCard,
    MenuLeft,
    Impressum,
    Login,
    Tags,
    Topbar,
  },
  props: {
    source: String,
  },
  mounted() {
    this.isMobil = this.$vuetify.breakpoint.smAndDown;
  },
  computed: {
    getItems() {
      const {
        isPossibleInside,
        isPossibleOutside,
        withoutPreperation,
        justActive,
        withoutCosts,
        getSorter,
      } = this.$store.getters;
      let returnArray = this.items
        .filter(item => item.description.toLowerCase().includes(this.searchInput.toLowerCase())
          || item.title.toLowerCase().includes(this.searchInput.toLowerCase())
          || item.material.toLowerCase().includes(this.searchInput.toLowerCase()))
        .filter(item => this.isTagMatchToEvent(item))
        .filter(item => (isPossibleInside === item.isPossibleInside
          || isPossibleOutside === item.isPossibleOutside)
          && (isPossibleInside || isPossibleOutside))
        .filter((item) => {
          const allowOne = this.levelFilter.includes(0);
          const allowTwo = this.levelFilter.includes(1);
          const allowThree = this.levelFilter.includes(2);
          const allow = (allowOne && allowOne === item.isLvlOne)
            || (allowTwo && allowTwo === item.isLvlTwo)
            || (allowThree && allowThree === item.isLvlThree);
          return allow;
        })
        .filter(item => !withoutPreperation || item.isPrepairationNeeded === 0)
        .filter(item => justActive === item.isActive)
        .filter(item => !withoutCosts || item.costsRating === 1);
      debugger;
      if (getSorter === 'alpha' && returnArray) {
        returnArray = this._.orderBy(returnArray, ['title'], ['asc']);
      }
      if (getSorter === 'newest' && returnArray) {
        returnArray = this._.orderBy(returnArray, ['createdAt'], ['asc']);
      }
      if (getSorter === 'random' && returnArray) {
        debugger;
        // returnArray = this._.shuffle(returnArray);
      }
      return returnArray;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isDrawer() {
      return this.$store.getters.isDrawer;
    },
    getLabel() {
      return `Suche in ${this.getItems.length} Heimabenden`;
    },
  },
  methods: {
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(this.convertUrlToId(tag)); // eslint-disable-line
      });
      if (this.filterTags && this.filterTags.length) {
        const matches = eventTagArray.filter(element => this.filterTags.includes(element));
        return !!matches.length;
      }
      return true;
    },
    toogleDrawer() {
      this.$store.commit('toogleDrawer');
    },
    onNewClick() {
      this.$refs.createGroupClassModal.show();
    },
    onImpressumClick() {
      this.$refs.impressumDialog.show();
    },
    onAboutProjectClick() {
      this.$refs.aboutProject.show();
    },
    onTagOverviewClick() {
      this.$refs.tagsOverview.show();
    },
    onLoginClick() {
      this.$refs.login.show();
    },
    onUpdateClick(item) {
      const tags = item.tags; // eslint-disable-line
      tags.forEach((tag, index) => {
        item.tags[index] = this.convertUrlToId(tag); // eslint-disable-line
      });
      this.$refs.createGroupClassModal.show(item);
    },
    convertUrlToId(url) {
      const idStringArray = url.split('/');
      const id = idStringArray[idStringArray.length - 2];

      return parseInt(id, 10);
    },
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
    },
    onDialogClose() {
      this.getEvents();
      this.getTags();
    },
    onTagFilterChanged(data) {
      this.filterTags = data;
    },
    onLevelFilterChanged(data) {
      this.levelFilter = data;
    },
    onResetClick() {
      this.$store.commit('clearFilters');
      this.$refs.mainMenuLeft.resetTags();
    },
    getEvents() {
      const path = `${this.API_URL}basic/event/`;
      axios.get(path)
        .then((res) => {
          this.items = res;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.tags = res;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getEvents();
    this.getTags();
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    filterTags: [],
    levelFilter: [0, 1, 2],
    searchInput: '',
    fab: false,
    colorFab: 'green',
    iconFab: 'mdi-plus',
    isMobil: false,
    tags: [],
    items: [],
  }),
};

</script>

<style scoped>
  #lateral .v-btn--example {
    bottom: 0;
    position: absolute;
    margin: 0 0 16px 16px;
  }

</style>

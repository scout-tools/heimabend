<template>
<div>
  <v-app id="keep">
    <v-app-bar
      app
      clipped-left
      color="#1a4b7e"
      dark
    >
    <v-app-bar-nav-icon @click="drawer = !drawer"/>
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
        label="Suche"
        prepend-inner-icon="mdi-magnify"
        clearable
        :dense="isMobil"
      />
      <v-spacer />
      <img v-on:click="onLoginClick" class="mr-2" :src="require('../assets/logo.gif')" height="50"/>


    </v-app-bar>

    <MenuLeft
      ref="mainMenuLeft"
      :filterStatus="filterStatus"
      :levelFilter="levelFilter"
      :tags="tags"
      @onTagFilterChanged="onTagFilterChanged"
      @openImpressum="onImpressumClick"
      @openAboutProject="onAboutProjectClick"
      @onLevelFilterChanged="onLevelFilterChanged"
      :drawer="drawer"
    />

    <v-content id="lateral">
      <div class="row mx-2" justify="center">
        <div class="col-sm-12">
          <HeimabendCard
            :items="getItems"
            :isMobil="isMobil"
            :tags="tags"
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
      v-on:dialogClose="onDialogClose"
      :tags="tags"
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
import AboutProject from './components/dialogs/AboutProject.vue';
import HeimabendCard from './components/cards/Heimabend.vue';
import MenuLeft from './components/menu/Left.vue';

export default {
  components: {
    CreateDialog,
    AboutProject,
    HeimabendCard,
    MenuLeft,
    Impressum,
    Login,
  },
  props: {
    source: String,
  },
  mounted() {
    this.isMobil = this.$vuetify.breakpoint.smAndDown;
  },
  computed: {
    getItems() {
      return this.items
        .filter(item => item.description.includes(this.searchInput)
          || item.title.includes(this.searchInput))
      // .filter(item => this.filterTags.filter(element => item.tags.includes(element)).length
      // || !this.filterTags.length)
        .filter(item => !this.filterStatus.isPossibleInside
          || item.isPossibleInside === this.filterStatus.isPossibleInside)
        .filter(item => !this.filterStatus.isPossibleOutside
          || item.isPossibleOutside === this.filterStatus.isPossibleOutside)
        .filter((item) => {
          const allowOne = this.levelFilter.includes(0);
          const allowTwo = this.levelFilter.includes(1);
          const allowThree = this.levelFilter.includes(2);
          const allow = (allowOne && allowOne === item.isLvlOne)
            || (allowTwo && allowTwo === item.isLvlTwo)
            || (allowThree && allowThree === item.isLvlThree);
          return allow;
        })
        .filter(item => !this.filterStatus.withoutPreperation || item.isPrepairationNeeded === 1)
        .filter(item => this.filterStatus.justActive === item.isActive)
        .filter(item => !this.filterStatus.withoutCosts || item.costsRating === 1);
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    onNewClick() {
      this.$refs.createGroupClassModal.show();
    },
    onImpressumClick() {
      this.$refs.impressumDialog.show();
    },
    onAboutProjectClick() {
      this.$refs.aboutProject.show();
    },
    onLoginClick() {
      this.$refs.login.show();
    },
    onUpdateClick(item) {
      const tags = item.tags; // eslint-disable-line
      debugger;
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
    },
    onTagFilterChanged(data) {
      this.filterTags = data;
    },
    onLevelFilterChanged(data) {
      this.levelFilter = data;
    },
    onResetClick() {
      this.filterStatus = {
        isPossibleInside: false,
        isPossibleOutside: false,
        withoutPreperation: false,
        withoutCosts: false,
        justActive: true,
      };
      this.levelFilter = [0, 1, 2];
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
    drawer: true,
    filterStatus: {
      isPossibleInside: false,
      isPossibleOutside: false,
      withoutPreperation: false,
      withoutCosts: false,
      justActive: true,
    },
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

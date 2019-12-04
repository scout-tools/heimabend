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
      <v-btn
        icon
        fab
        large
        @click="onNewClick()"
      >
        <v-icon color="green">mdi-pencil-plus</v-icon>
      </v-btn>
      <v-spacer />
      <img v-on:click="onLoginClick" class="mr-2" :src="require('../assets/logo.gif')" height="50"/>


    </v-app-bar>

    <MenuLeft
      ref="mainMenuLeft"
      :filterStatus="filterStatus"
      :tags="tags"
      @onTagFilterChanged="onTagFilterChanged"
      @openImpressum="onImpressumClick"
      @openAboutProject="onAboutProjectClick"
      :drawer="drawer"
    />

    <v-content id="lateral">
      <div class="row mx-2" justify="center">
        <div class="col-sm-12">
          <HeimabendCard
            :items="getItems"
            :isMobil="isMobil"
            :tags="tags"
          />
          <v-btn
            class="ma-10"
            v-if="!getItems.length"
            @click="onResetClick()"
          >
            Alle Filter zurücksetzen
          </v-btn>
        </div>
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
import Login from './components/dialogs/Login.vue';
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
        .filter(item => item.beschreibung.includes(this.searchInput)
          || item.title.includes(this.searchInput))
      // .filter(item => this.filterTags.filter(element => item.tags.includes(element)).length
      // || !this.filterTags.length)
        .filter(item => !this.filterStatus.isPossibleInside
          || item.isPossibleInside === this.filterStatus.isPossibleInside)
        .filter(item => !this.filterStatus.isPossibleOutside
          || item.isPossibleOutside === this.filterStatus.isPossibleOutside)
        .filter(item => !this.filterStatus.withoutPreperation || item.prepairationRating === 1)
        .filter(item => !this.filterStatus.withoutCosts || item.costsRating === 1);
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
      this.$refs.createGroupClassModal.show(item);
    },
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
    },
    onDialogClose() {
      // reload
    },
    onTagFilterChanged(data) {
      this.filterTags = data;
    },
    onResetClick() {
      this.filterStatus = {
        isPossibleInside: false,
        isPossibleOutside: false,
        withoutPreperation: false,
        withoutCosts: false,
      };
      this.$refs.mainMenuLeft.resetTags();
    },
    getEvents() {
      const path = 'http://localhost:8000/basic/event/';
      axios.get(path)
        .then((res) => {
          debugger;
          this.items = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getTags() {
      const path = 'http://localhost:8000/basic/tag/';
      axios.get(path)
        .then((res) => {
          this.tags = res.data;
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
    filterTags: [],
    drawer: null,
    filterStatus: {
      isPossibleInside: false,
      isPossibleOutside: false,
      withoutPreperation: false,
      withoutCosts: false,
    },
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

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
      <span
        class="title ml-3 mr-5"
        v-if="!isMobil"
        @click="onHeaderClick()"
      >
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
      :tags="tags"
      @openImpressum="onImpressumClick"
      @openAboutProject="onAboutProjectClick"
      @tagOverview="onTagOverviewClick"
    />

    <v-content id="lateral">
      <Topbar
        ref="topFilterToolbar"
        @openImpressum="onImpressumClick"
        @openAboutProject="onAboutProjectClick"
        @tagOverview="onTagOverviewClick"
      />
      <div class="row mx-2" justify="center">
        <router-view
          class="content ma-10"
          @onUpdateClick="onUpdateClick"
        />

        <v-fab-transition
          v-if="!isMobil"
        >
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
    <Login
      ref="login"
    />
    <create-dialog
      ref="createGroupClassModal"
      @dialogClose="onDialogClose"
      :tags="tags"
    />
  </v-app>
</div>
</template>

<script>
import axios from 'axios';

import Login from './components/dialogs/Login.vue'; // eslint-disable-line
import MenuLeft from './components/menu/Left.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';
import CreateDialog from './heimabend/create/Dialog.vue'; // eslint-disable-line

export default {
  components: {
    CreateDialog,
    MenuLeft,
    Login,
    Topbar,
  },
  props: {
    source: String,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getLabel() {
      const counter = this.$store.getters.heimabendCounter;
      return `${counter} Heimabende`;
    },

    getFilterTags() {
      return this.$store.getters.filterTags;
    },
  },
  methods: {
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(this.convertUrlToId(tag)); // eslint-disable-line
      });
      if (this.getFilterTags && this.getFilterTags.length) {
        const matches = eventTagArray.filter(element => this.getFilterTags.includes(element));
        return !!matches.length;
      }
      return true;
    },
    onUpdateClick(item) {
      const tags = item.tags; // eslint-disable-line
      tags.forEach((tag, index) => {
        item.tags[index] = this.convertUrlToId(tag); // eslint-disable-line
      });
      this.$refs.createGroupClassModal.show(item);
    },
    toogleDrawer() {
      this.$refs.mainMenuLeft.toggleDrawer();
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
    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
    },
    onDialogClose() {
      this.getEvents();
      this.getTags();
    },
    onResetClick() {
      this.$store.commit('clearFilters');
      this.$refs.mainMenuLeft.resetTags();
    },
    getEvents() {
      const path = `${this.API_URL}basic/event/`;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {
        });
    },
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.tags = res.data;
        })
        .catch(() => {
        });
    },
    onHeaderClick() {
      this.$router.push({ name: 'overview' });
    },
  },
  created() {
    this.getEvents();
    this.getTags();
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    searchInput: '',
    fab: false,
    colorFab: 'green',
    iconFab: 'mdi-plus',
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

  .content {
    flex: 1;
  }
</style>

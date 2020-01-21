<template>
<div>
  <v-app id="keep">
    <v-app-bar
      app
      clipped-left
      color="#1a4b7e"
      dark
    >
    <v-app-bar-nav-icon
      @click="toogleDrawer()"
    />
      <span
        class="title hand-cursor ml-3 mr-5"
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
        @input="onChangeSearchInput()"
      />
      <v-spacer />
      <img
        v-on:click="onLoginClick"
        class="mr-2"
        :src="require('../assets/logo.gif')" height="50"
      />


    </v-app-bar>

    <MenuLeft
      ref="mainMenuLeft"
    />

    <v-content id="lateral">
      <topbar
        v-if="isMainPage"
        ref="topFilterToolbar"
      />
      <sub-pages-top-bar
        v-if="!isMainPage"
      />
      <template>
        <router-view
          class="content"
          :class="getMargin"
        />
        <v-fab-transition
          v-if="isMainPage"
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
      </template>
    </v-content>
    <Login
      ref="login"
    />
  </v-app>
</div>
</template>

<script>
import axios from 'axios';

import Login from './components/dialogs/Login.vue'; // eslint-disable-line
import MenuLeft from './components/menu/Left.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';
import SubPagesTopBar from './components/toolbar/SubPagesTopBar.vue';

export default {
  components: {
    MenuLeft,
    Login,
    Topbar,
    SubPagesTopBar,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    getLabel() {
      const counter = this.$store.getters.heimabendCounter;
      return `${counter} Heimabende`;
    },
    getMargin() {
      return this.isMobil ? 'ma-1' : 'ma-10';
    },
    tags() {
      return this.$store.getters.tags;
    },
    isMainPage() {
      return this.currentRouteName === 'overview';
    },
    currentRouteName() {
      return this.$route.name;
    },
  },
  methods: {
    onChangeSearchInput() {
      this.$store.commit('setSearchInput', this.searchInput);
    },
    toogleDrawer() {
      this.$refs.mainMenuLeft.toggleDrawer();
    },
    onNewClick() {
      this.$router.push({ name: 'heimabendCreate' });
    },
    onLoginClick() {
      this.$refs.login.show();
    },
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.$store.commit('setTags', res.data);
        })
        .catch(() => {
        });
    },
    onHeaderClick() {
      this.$router.push({ name: 'overview' });
    },
  },
  created() {
    this.getTags();
    this.$store.commit('enableJustActive');
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    searchInput: '',
    fab: false,
    colorFab: 'green',
    iconFab: 'mdi-plus',
  }),
};

</script>

<style>
  #lateral .v-btn--example {
    bottom: 0;
    position: absolute;
    margin: 0 0 16px 16px;
  }

  .content {
    flex: 1;
  }
  .v-btn-toggle--group > .v-btn.v-btn {
    margin: 2px !important;
  }
  .hand-cursor {
    cursor: pointer
  }
</style>

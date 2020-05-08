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
      v-if="!apiIsDown"
      @click="toogleDrawer()"
    />
      <h1
        class="title hand-cursor ml-3 mr-5"
        v-if="!isMobil"
        @click="onHeaderClick()"
      >
        Heimabend&nbsp;
        <span class="font-weight-light">
          Inspirator
        </span>
      </h1>

      <v-text-field
        class="px-3"
        v-model="currentSearchInput"
        outlined
        hide-details
        :label="getLabel"
        prepend-inner-icon="mdi-magnify"
        clearable
        :dense="isMobil"
        @keydown.enter="onChangeSearchInput()"
      />

      <v-spacer/>

      <img
        src="https://dpbm.de/wp/wp-content/uploads/2019/02/mosaikWhite.svg"
        class="mr-2"
        height="50"
        alt="Bundesabzeichen vom Deutschen Pfadfinderbund Mosaik"
      />
    </v-app-bar>

    <menu-left
      ref="mainMenuLeft"
    />

    <v-content
      id="lateral"
    >
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
      <Fab
        v-if="isMainPage && !apiIsDown"
      />
      </template>
    <api-down-banner
      v-if="apiIsDown"
    />
    </v-content>
    <pricacy-banner
      v-if="!acceptedPrivacy"
    />
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
    >
      {{ 'Es ist ein Fehler aufgetreten' }}
    </v-snackbar>
  </v-app>
</div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

import PricacyBanner from './components/banner/Privacy.vue';
import MenuLeft from './components/menu/Left.vue';
import ApiDownBanner from './components/banner/ApiDown.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';
import SubPagesTopBar from './components/toolbar/SubPagesTopBar.vue';
import Fab from './components/fab/Standard.vue';

export default {
  components: {
    MenuLeft,
    Topbar,
    SubPagesTopBar,
    ApiDownBanner,
    Fab,
    PricacyBanner,
  },
  computed: {
    ...mapGetters([
      'searchInput',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getLabel() {
      const counter = this.$store.getters.heimabendCounter;
      return `Suche in ${counter} Heimabenden ...`;
    },
    getMargin() {
      return this.isMobil ? 'ma-1' : 'ma-0';
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
    apiIsDown() {
      return !!this.$store.getters.apiIsDown;
    },
    acceptedPrivacy() {
      return !!this.$store.getters.acceptedPrivacy;
    },
  },
  watch: {
    searchInput(value) {
      if (value === '' || !value) {
        this.currentSearchInput = value;
      } else {
        // eslint-disable-next-line no-undef
        _paq.push(['trackSiteSearch', value, false, false]);
      }
    },
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    onChangeSearchInput() {
      this.$store.commit('setSearchInput', this.currentSearchInput);
    },
    toogleDrawer() {
      this.$refs.mainMenuLeft.toggleDrawer();
    },
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.$store.commit('setTags', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
    onHeaderClick() {
      this.$router.push({ name: 'overview' });
    },
  },
  mounted() {
    this.getTags();
    this.$store.dispatch('resetFilters');
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    fab: false,
    colorFab: 'green',
    iconFab: 'mdi-plus',
    showError: false,
    currentSearchInput: '',
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
    min-height: "100vh" !important;
  }
  .v-btn-toggle--group > .v-btn.v-btn {
    margin: 2px !important;
  }
  .hand-cursor {
    cursor: pointer
  }
  .info-cursor {
    cursor: help !important;
  }
  .theme--light.v-application {
    background: transparent !important;
  }
</style>

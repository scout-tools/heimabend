<template>
  <v-app id="keep">
    <v-app-bar app clipped-left color="#1a4b7e" dark v-if="!isScoringMode">
      <v-app-bar-nav-icon
        v-if="!apiIsDown && !isScoringMode"
        @click="toogleDrawer()"
      />
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
        v-if="!isScoringMode"
      />

      <v-spacer />
      <router-link to="/">
      <img
        :src="require('@/assets/inspi.png')"
        class="mr-2"
        height="70"
        alt="Bundesabzeichen vom Deutschen Pfadfinderbund Mosaik"
      />
      </router-link>
    </v-app-bar>

    <menu-left ref="mainMenuLeft" v-if="!isScoringMode" />

    <v-main id="lateral">
      <topbar v-if="isMainPage && !isScoringMode" ref="topFilterToolbar" />
      <sub-pages-top-bar v-if="!isMainPage && !isScoringMode" />

      <filter-top-sub-bar v-if="isMainPage && !isMobil && !isScoringMode" />
          <router-view class="content" :class="getMargin" v-scroll="onScroll" />
      <api-down-banner v-if="apiIsDown" />
    </v-main>
    <pricacy-banner v-if="!acceptedPrivacy" />
    <v-snackbar v-model="showError" color="error" y="top">
      {{ 'Es ist ein Fehler aufgetreten' }}
    </v-snackbar>
  </v-app>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

import PricacyBanner from './components/banner/Privacy.vue';
import MenuLeft from './components/menu/Left.vue';
import ApiDownBanner from './components/banner/ApiDown.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';
import SubPagesTopBar from './components/toolbar/SubPagesTopBar.vue';
import FilterTopSubBar from './components/toolbar/FilterSubBar.vue';

export default {
  components: {
    MenuLeft,
    Topbar,
    SubPagesTopBar,
    ApiDownBanner,
    PricacyBanner,
    FilterTopSubBar,
  },
  computed: {
    ...mapGetters(['searchInput', 'tags', 'isScoringMode']),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getLabel() {
      const counter = this.$store.getters.heimabendCounter;
      return `Suche in ${counter} Heimabendideen`;
    },
    getMargin() {
      return this.isMobil ? 'ma-1' : 'ma-2';
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
      const path = `${
        this.API_URL
      }basic/tag/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTags', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
    getTagCategory() {
      const path = `${
        this.API_URL
      }basic/tag-category/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTagCategory', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
    onHeaderClick() {
      this.$router.push({ name: 'overview' });
    },
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
    onScroll() {
      const isOnTop = window.scrollY > 20;
      this.$store.commit('setPageScrolled', isOnTop);
    },
  },
  mounted() {
    this.getTags();
    this.getTagCategory();
    this.$store.dispatch('resetFilters');
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    colorFab: 'green',
    iconFab: 'mdi-plus',
    showError: false,
    currentSearchInput: '',
    chips: [],
  }),
};
</script>

<style>
.content {
  flex: 1;
  min-height: '100vh' !important;
}
.hand-cursor {
  cursor: pointer;
}
.info-cursor {
  cursor: help !important;
}
.theme--light.v-application {
  background: #f4f4f434 !important;
}
</style>

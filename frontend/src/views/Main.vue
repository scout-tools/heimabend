<template>
  <v-app id="keep">
    <v-app-bar app clipped-left color="#4171A4" dark>
      <v-app-bar-nav-icon
        v-if="!apiIsDown && !isSubPage &&!isMobil"
        @click="onDrawerIconClicked()"
      />
      <router-link
        v-if="isSubPage"
        :to="{ name: 'overview' }"
        class="no-underline"
      >
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              color="white"
              v-bind="attrs"
              v-on="on"
              @click="onCloseButtonClicked"
            >
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </template>
          <span>Zurück zum Inspirator</span>
        </v-tooltip>
      </router-link>
      <h1
        v-if="!isScoringMode && !isSubPage && !isMobil"
        class="title hand-cursor ml-3 mr-5"
        @click="onHeaderClick()"
      >
        <span class="font-weight-thin"> Heimabend&nbsp; </span>
        <span class="font-weight-light">
          <b class="font-weight-black">Inspi</b>
          <span>rator</span>
        </span>
      </h1>
      <v-spacer v-if="!isMainPage && !searching" />
      <h1 v-if="!isMainPage" class="title text-uppercase">
        {{ headerString }}
      </h1>
      <v-spacer />
      <div v-show="searching" transition="slide-x-transition">
        <v-text-field
          class="px-3"
          v-model="currentSearchInput"
          solo-inverted
          hide-details
          prepend-inner-icon="mdi-magnify"
          clearable
          :dense="isMobil"
          ref="mainsearchfield"
          @keydown.enter="onChangeSearchInput()"
          v-show="!isScoringMode && isMainPage"
          @blur="searching=false"
        />
      </div>
      <v-btn
        v-show="!isScoringMode && isMainPage && !searching"
        icon
        @click="onSearchIconClicked"
      >
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-tooltip bottom v-if="isMainPage && !searching">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
            tile
            icon
            color="white"
            @click="onInstaClicked"
          >
            <v-icon> mdi-instagram </v-icon>
          </v-btn>
        </template>
        <span>Link zu meinen Instagram Account</span>
      </v-tooltip>
      <router-link v-show="!searching" to="/">
        <img
          :src="require('@/assets/inspi/inspi_thinking.webp')"
          class="mr-2"
          :height="isMobil ? 85 : 98"
          alt="Bild von Inspi"
        />
        <div
          id="hideMe"
          class="box sb1 fade-in"
          v-if="firstVisit && $route.name == 'overview'"
        >
          Hallo, Ich bin Inspi. <br />Willkommen auf meiner Seite.
        </div>
      </router-link>
    </v-app-bar>

    <menu-left ref="mainMenuLeft" v-if="!isMobil"/>

    <v-main id="lateral">
      <topbar v-if="isMainPage && !isScoringMode" ref="topFilterToolbar" />
      <filter-menu />
      <router-view class="content" v-scroll="onScroll" />
      <api-down-banner v-if="apiIsDown" />
      <v-snackbar v-model="showError" color="error" y="top">
        {{ 'Es ist ein Fehler aufgetreten' }}
      </v-snackbar>
    </v-main>
    <Footer v-if="!isScoringMode && !isMobil" />
    <MobileBottomBar @openBottomMenu="openBottomMenu" v-if="isMobil"/>
    <BottomMenu ref="BottomMenuRef" />
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
// eslint-disable-next-line
import Footer from '@/components/navigation/Footer.vue';
import MenuLeft from './components/menu/Left.vue';
import ApiDownBanner from './components/banner/ApiDown.vue';
import Topbar from './components/toolbar/FilterTopBar.vue';
import FilterMenu from '@/components/heimabend/FilterMenu.vue'; // eslint-disable-line
import MobileBottomBar from '@/components/menu/MobileBottomBar.vue'; // eslint-disable-line
import BottomMenu from '@/components/menu/BottomMenu.vue'; // eslint-disable-line

export default {
  components: {
    MenuLeft,
    Topbar,
    ApiDownBanner,
    BottomMenu,
    // FilterTopSubBar,
    MobileBottomBar,
    Footer,
    FilterMenu,
  },
  computed: {
    ...mapGetters([
      'searchInput',
      'tags',
      'isScoringMode',
      'headerString',
      'isSubPage',
      'isDrawer',
      'apiIsDown',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getLabel() {
      const counter = this.$store.getters.heimabendCounter;
      return this.isMobil
        ? `Suche in ${counter} Ideen`
        : `Suche in ${counter} Heimabendideen`;
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
  },
  methods: {
    openBottomMenu() {
      this.$refs.BottomMenuRef.show();
    },
    onSearchIconClicked() {
      this.searching = !this.searching;
      setTimeout(() => {
        // ugly work around
        this.$nextTick(() => this.$refs.mainsearchfield.focus());
      }, 50);
    },
    onCloseButtonClicked() {
      this.$store.commit('setIsSubPage', false);
      // todo: looks strange
    },
    // eslint-disable-next-line no-unused-vars
    onChangeSearchInput() {
      this.searching = false;
      this.$store.commit('setIsFirstEventLoaded', false);
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setSearchInput', this.currentSearchInput);
    },
    onDrawerIconClicked() {
      if (this.isMobil) {
        setTimeout(() => {
          // ugly work around
          this.$store.commit('setDrawer', true);
        }, 50);
        this.$store.commit('setDrawer', false);
      } else {
        this.$store.commit('toogleDrawer');
      }
    },
    onHeaderClick() {
      this.$router.push({ name: 'overview' });
    },
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
    onScroll() {
      this.firstVisit = false;
      const isOnTop = window.scrollY > 20;
      this.$store.commit('setPageScrolled', isOnTop);
    },
    onInstaClicked() {
      window.open('https://www.instagram.com/inspi_rator/?hl=de', '_blank');
    },
  },
  created() {
    this.$store.dispatch('resetFilters');
    this.$store.commit('setDrawer', false);
    this.$store.commit('setPageScrolled', false);
    if (this.firstVisit) {
      this.$store.commit('setScollPosition', 0);
    }
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    colorFab: 'green',
    iconFab: 'mdi-plus',
    showError: false,
    currentSearchInput: '',
    chips: [],
    firstVisit: true,
    searching: false,
  }),
};
</script>

<style>
.hand-cursor {
  cursor: pointer;
}
.info-cursor {
  cursor: help !important;
}
* {
  margin: 0px;
  padding: 0px;
}

.box {
  width: 300px;
  margin: 50px auto;
  background: #a6bf98;
  padding: 20px;
  text-align: center;
  font-weight: 900;
  color: #fff;
  font-family: arial;
  position: absolute;
  z-index: 10;
  right: 100px;
  top: 0px;
  border-radius: 0.4em;
}

.sb1:before {
  content: '';
  width: 0px;
  height: 0px;
  position: absolute;
  border-left: 10px solid #a6bf98;
  border-right: 10px solid transparent;
  border-top: 10px solid #a6bf98;
  border-bottom: 10px solid transparent;
  right: -19px;
  top: 6px;
}

#hideMe {
  -webkit-animation: cssAnimation 7s forwards;
  animation: cssAnimation 7s forwards;
}
@keyframes cssAnimation {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@-webkit-keyframes cssAnimation {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>

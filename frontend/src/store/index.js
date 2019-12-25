import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'; // eslint-disable-line
import { event } from 'vue-analytics';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    currentUser: null,
    drawer: true,
    isPossibleInside: true,
    isPossibleOutside: true,
    withoutPreperation: false,
    withoutCosts: false,
    justActive: true,
    sorter: 'random',
  },
  getters: {
    isAuthenticated(state) {
      return !!state.accessToken;
    },
    isDrawer(state) {
      return !!state.drawer;
    },
    isPossibleInside(state) {
      return !!state.isPossibleInside;
    },
    isPossibleOutside(state) {
      return !!state.isPossibleOutside;
    },
    withoutPreperation(state) {
      return !!state.withoutPreperation;
    },
    withoutCosts(state) {
      return !!state.withoutCosts;
    },
    justActive(state) {
      return !!state.justActive;
    },
    getUsername(state) {
      return state.currentUser;
    },
    getSorter(state) {
      return state.sorter;
    },
  },
  mutations: {
    changeSorter(state, newSorter) {
      state.sorter = newSorter;
    },
    toogleDrawer(state) {
      state.drawer = !state.drawer;
      event('user-click', 'toogle', 'drawer', state.drawer);
    },
    tooglePossibleInside(state) {
      state.isPossibleInside = !state.isPossibleInside;
      event('user-click', 'toogle', 'possibleInside', state.isPossibleInside);
    },
    tooglePossibleOutside(state) {
      state.isPossibleOutside = !state.isPossibleOutside;
      event('user-click', 'toogle', 'isPossibleOutside', state.isPossibleOutside);
    },
    toogleWithoutPreperation(state) {
      state.withoutPreperation = !state.withoutPreperation;
      event('user-click', 'toogle', 'possibleInside', state.withoutPreperation);
    },
    toogleWithoutCosts(state) {
      state.withoutCosts = !state.withoutCosts;
      event('user-click', 'toogle', 'possibleInside', state.withoutCosts);
    },
    toggleJustActive(state) {
      state.justActive = !state.justActive;
      event('user-click', 'toogle', 'possibleInside', state.justActive);
    },
    setTokens(state, access, refresh) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    clearFilters(state) {
      state.isPossibleInside = true;
      state.isPossibleOutside = true;
      state.withoutPreperation = false;
      state.withoutCosts = false;
      state.justActive = true;
    },
    clearAccessToken(state) {
      state.accessToken = null;
    },
    clearTokens(state) {
      state.accessToken = null;
      state.refreshToken = null;
      state.originalAccessToken = null;
      state.originalRefreshToken = null;
    },
    setCurrentUser(state, payload) {
      state.currentUser = payload;
    },
  },
  actions: {
    logout({ commit }) {
      commit('clearTokens');
      commit('setCurrentUser', null);
    },
  },
  plugins: [createPersistedState()],
});

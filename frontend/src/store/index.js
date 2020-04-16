import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'; // eslint-disable-line

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    currentUser: null,
    isPossibleInside: true,
    isPossibleOutside: false,
    isPossibleDigital: false,
    isPossibleAlone: false,
    isPrepairationNeeded: false,
    withoutCosts: false,
    isActive: true,
    sorter: 'random',
    levelFilter: [0, 1, 2],
    filterTags: [],
    heimabendCounter: 0,
    tags: [],
    searchInput: '',
    apiIsDown: false,
    acceptedPrivacy: false,
    liked: [],
  },
  getters: {
    isAuthenticated(state) {
      return !!state.accessToken;
    },
    liked(state) {
      return state.liked;
    },
    acceptedPrivacy(state) {
      return !!state.acceptedPrivacy;
    },
    tags(state) {
      return state.tags;
    },
    tagById(state, id) {
      return state.tags.find(tag => tag.id === id);
    },
    isPossibleInside(state) {
      return !!state.isPossibleInside;
    },
    isPossibleOutside(state) {
      return !!state.isPossibleOutside;
    },
    isPossibleAlone(state) {
      return !!state.isPossibleAlone;
    },
    isPossibleDigital(state) {
      return !!state.isPossibleDigital;
    },
    isPrepairationNeeded(state) {
      return !!state.isPrepairationNeeded;
    },
    withoutCosts(state) {
      return !!state.withoutCosts;
    },
    isActive(state) {
      return !!state.isActive;
    },
    getUsername(state) {
      return state.currentUser;
    },
    sorter(state) {
      return state.sorter;
    },
    levelFilter(state) {
      return state.levelFilter;
    },
    filterTags(state) {
      return state.filterTags;
    },
    heimabendCounter(state) {
      return state.heimabendCounter;
    },
    searchInput(state) {
      return state.searchInput;
    },
    apiIsDown(state) {
      return state.apiIsDown;
    },
  },
  mutations: {
    acceptedPrivacy(state, acceptedPrivacy) {
      state.acceptedPrivacy = acceptedPrivacy;
    },
    apiIsDown(state, status) {
      state.apiIsDown = status;
    },
    changeSorter(state, newSorter) {
      state.sorter = newSorter;
    },
    setTags(state, newTags) {
      state.tags = newTags;
    },
    setSearchInput(state, newSearchInput) {
      state.searchInput = newSearchInput;
    },
    changeFilterTags(state, newTags) {
      state.filterTags = newTags;
    },
    tooglePossibleInside(state) {
      state.isPossibleInside = !state.isPossibleInside;
    },
    tooglePossibleOutside(state) {
      state.isPossibleOutside = !state.isPossibleOutside;
    },
    tooglePossibleAlone(state) {
      state.isPossibleAlone = !state.isPossibleAlone;
    },
    tooglePossibleDigital(state) {
      state.isPossibleDigital = !state.isPossibleDigital;
    },
    toogleIsPreperationNeeded(state) {
      state.isPrepairationNeeded = !state.isPrepairationNeeded;
    },
    toogleWithoutCosts(state) {
      state.withoutCosts = !state.withoutCosts;
    },
    toggleIsActive(state) {
      state.isActive = !state.isActive;
    },
    enableIsActive(state) {
      state.isActive = true;
    },
    setHeimabendCounter(state, payload) {
      state.heimabendCounter = payload;
    },
    setLevelFilter(state, newFilter) {
      state.levelFilter = newFilter;
    },
    setTokens(state, access, refresh) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    clearFilters(state) {
      state.isPossibleInside = true;
      state.isPossibleOutside = true;
      state.isPossibleDigital = false;
      state.isPossibleAlone = false;
      state.levelFilter = [0, 1, 2];
      state.searchInput = '';
      state.isPrepairationNeeded = false;
      state.withoutCosts = false;
      state.isActive = true;
      state.filterTags = [];
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
    setLiked(state, id) {
      state.liked.push(id);
    },
  },
  actions: {
    logout({ commit }) {
      commit('clearTokens');
      commit('setCurrentUser', null);
    },
    resetFilters({ commit }) {
      commit('enableIsActive');
      commit('changeFilterTags', []);
      commit('setSearchInput', '');
    },
  },
});

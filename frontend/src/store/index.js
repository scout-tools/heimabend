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
    sorter: '-createdAt',
    isLvlOne: false,
    isLvlTwo: false,
    isLvlThree: false,
    filterTags: [],
    mandatoryFilter: {},
    heimabendCounter: 0,
    tags: [],
    tagCategory: null,
    searchInput: '',
    apiIsDown: false,
    acceptedPrivacy: false,
    liked: [],
  },
  getters: {
    isLvlOne(state) {
      return state.isLvlOne;
    },
    isLvlTwo(state) {
      return state.isLvlTwo;
    },
    isLvlThree(state) {
      return state.isLvlThree;
    },
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
    tagCategory(state) {
      return state.tagCategory;
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
    filterTags(state) {
      return state.filterTags;
    },
    mandatoryFilter(state) {
      return state.mandatoryFilter;
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
    setTagCategory(state, newValue) {
      state.tagCategory = newValue;
    },
    setSearchInput(state, newSearchInput) {
      state.searchInput = newSearchInput;
    },
    changeFilterTags(state, newTags) {
      state.filterTags = newTags;
    },
    changeMandatoryFilter(state, newTags) {
      state.mandatoryFilter = newTags;
    },
    removeOneFilter(state, itemToRemove) {
      const tempArray = state.mandatoryFilter;
      const index1 = tempArray.indexOf(itemToRemove);
      if (index1 !== -1) {
        tempArray.splice(index1, 1);
      }
      state.mandatoryFilter = tempArray;

      const tempArray2 = state.filterTags;
      const index2 = tempArray2.indexOf(itemToRemove);
      if (index2 !== -1) {
        tempArray2.splice(index2, 1);
      }
      state.filterTags = tempArray2;
    },
    setPossibleInside(state, value) {
      state.isPossibleInside = value;
    },
    setPossibleOutside(state, value) {
      state.isPossibleOutside = value;
    },
    setPossibleAlone(state, value) {
      state.isPossibleAlone = value;
    },
    setPossibleDigital(state, value) {
      state.isPossibleDigital = value;
    },
    setIsPreperationNeeded(state, value) {
      state.isPrepairationNeeded = value;
    },
    setWithoutCosts(state, value) {
      state.withoutCosts = value;
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
    setIsLvlOne(state, value) {
      state.isLvlOne = value;
    },
    setIsLvlTwo(state, value) {
      state.isLvlTwo = value;
    },
    setIsLvlThree(state, value) {
      state.isLvlThree = value;
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
      state.isLvlOne = false;
      state.isLvlTwo = false;
      state.isLvlThree = false;
      state.searchInput = '';
      state.isPrepairationNeeded = false;
      state.withoutCosts = false;
      state.isActive = true;
      state.filterTags = [];
      state.mandatoryFilter = [];
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
      commit('changeMandatoryFilter', []);
      commit('changeFilterTags', []);
      commit('setSearchInput', '');
    },
  },
  plugins: [createPersistedState()],
});

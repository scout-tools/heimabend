import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'; // eslint-disable-line

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    currentUser: null,
    isPrepairationNeeded: false,
    withoutCosts: false,
    isPublic: true,
    sorter: '-createdAt',
    filterTags: [],
    mandatoryFilter: [],
    numberFilter: [],
    heimabendCounter: 0,
    tags: [],
    tagCategory: null,
    searchInput: '',
    apiIsDown: false,
    acceptedPrivacy: false,
    liked: [],
    pageScrolled: false,
    isScoringMode: false,
    headerString: 'Inspi',
    isSubPage: false,
    isDrawer: false,
    messageType: [],
    heimabendItems: [],
    scollPosition: 0,
    nextPath: '',
    isEventLoading: false,
    isFirstEventLoaded: false,
    saveFilterLastFilter: [],
    isExtended: false,
  },
  getters: {
    saveFilterLastFilter(state) {
      return state.saveFilterLastFilter;
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
    isPrepairationNeeded(state) {
      return !!state.isPrepairationNeeded;
    },
    withoutCosts(state) {
      return !!state.withoutCosts;
    },
    getUsername(state) {
      return state.currentUser;
    },
    filterTags(state) {
      return state.filterTags;
    },
    mandatoryFilter(state) {
      return state.mandatoryFilter;
    },
    numberFilter(state) {
      return state.numberFilter;
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
    isPageScrolled(state) {
      return state.pageScrolled;
    },
    isScoringMode(state) {
      return state.isScoringMode;
    },
    headerString(state) {
      return state.headerString;
    },
    isSubPage(state) {
      return state.isSubPage;
    },
    isDrawer(state) {
      return state.isDrawer;
    },
    messageType(state) {
      return state.messageType;
    },
    heimabendItems(state) {
      return state.heimabendItems;
    },
    scollPosition(state) {
      return state.scollPosition;
    },
    nextPath(state) {
      return state.nextPath;
    },
    isEventLoading(state) {
      return state.isEventLoading;
    },
    isFirstEventLoaded(state) {
      return state.isFirstEventLoaded;
    },
    isExtended(state) {
      return state.isExtended;
    },
  },
  mutations: {
    setIsExtended(state, isExtended) {
      state.isExtended = isExtended;
    },
    setSaveFilterLastFilter(state, value) {
      state.saveFilterLastFilter = value;
    },
    setIsEventLoading(state, value) {
      state.isEventLoading = value;
    },
    setIsFirstEventLoaded(state, value) {
      state.isFirstEventLoaded = value;
    },
    acceptedPrivacy(state, acceptedPrivacy) {
      state.acceptedPrivacy = acceptedPrivacy;
    },
    apiIsDown(state, status) {
      state.apiIsDown = status;
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
    addNumberFilter(state, newTags) {
      state.numberFilter = [newTags, ...state.numberFilter];
    },
    setNumberFilter(state, newTags) {
      state.numberFilter = newTags;
    },
    removeNumberFilter(state, itemToRemove) {
      const tempArray = state.numberFilter;
      const index1 = tempArray.indexOf(itemToRemove);
      if (index1 !== -1) {
        tempArray.splice(index1, 1);
      }
      state.numberFilter = tempArray;
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
    setIsPreperationNeeded(state, value) {
      state.isPrepairationNeeded = value;
    },
    setWithoutCosts(state, value) {
      state.withoutCosts = value;
    },
    setHeimabendCounter(state, payload) {
      state.heimabendCounter = payload;
    },
    setScollPosition(state, payload) {
      state.scollPosition = payload;
    },
    setTokens(state, access, refresh) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    clearFilters(state) {
      state.searchInput = '';
      state.isPrepairationNeeded = false;
      state.withoutCosts = false;
      state.filterTags = [];
      state.mandatoryFilter = [];
      state.numberFilter = [];
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
    setPageScrolled(state, isScrolled) {
      state.pageScrolled = isScrolled;
    },
    setIsScoringMode(state, isScoringMode) {
      state.isScoringMode = isScoringMode;
    },
    setHeaderString(state, headerString) {
      state.headerString = headerString;
    },
    setIsSubPage(state, isSubPage) {
      state.isSubPage = isSubPage;
    },
    setDrawer(state, isDrawer) {
      state.isDrawer = isDrawer;
    },
    toogleDrawer(state) {
      state.isDrawer = !state.isDrawer;
    },
    setMessageType(state, messageType) {
      state.messageType = messageType;
    },
    extendHeimabendItems(state, newHeimabendItems) {
      state.heimabendItems = state.heimabendItems.concat(newHeimabendItems);
    },
    resetHeimabendItems(state) {
      state.heimabendItems = [];
    },
    setNextPath(state, payload) {
      state.nextPath = payload;
    },
  },
  actions: {
    logout({ commit }) {
      commit('clearTokens');
      commit('setCurrentUser', null);
    },
    resetFilters({ commit }) {
      commit('changeMandatoryFilter', []);
      commit('changeFilterTags', []);
      commit('setNumberFilter', []);
      commit('setSearchInput', '');
      commit('resetHeimabendItems');
      commit('setIsFirstEventLoaded', false);
      commit('setNextPath', false);
    },
  },
  plugins: [createPersistedState()],
});

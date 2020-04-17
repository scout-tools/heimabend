<template>
<div>
  <div class="col-sm-12">
    <heimabend-card
      ref="eventCards"
      v-if="items.length"
      @refresh="refresh()"
      @loadMore="loadMore()"
      :items="items"
      :loading="loading"
      :isMobil="isMobil"
    />
    <v-btn
      class="ma-10"
      v-if="!items.length && !loading"
      @click="onResetClick()"
    >
      Alle Filter zurücksetzen
    </v-btn>
    <v-progress-circular
      v-if="loading"
      color="primary"
      indeterminate
    />
  <span v-if="!isMobil" class="bg"/>
  </div>
</div>
</template>


<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

import HeimabendCard from './cards/Heimabend.vue';

export default {
  components: {
    HeimabendCard,
  },
  watch: {
    axiosParams() {
      this.refresh();
    },
  },
  computed: {
    ...mapGetters([
      'isPossibleInside',
      'isPossibleOutside',
      'isPossibleAlone',
      'isPossibleDigital',
      'isPrepairationNeeded',
      'isActive',
      'withoutCosts',
      'searchInput',
      'sorter',
      'levelFilter',
      'filterTags',
      'tags',
      'isAuthenticated',
      'heimabendCounter',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    axiosParams() {
      const params = new URLSearchParams();
      const isLvlOne = this.levelFilter.includes(0);
      const isLvlTwo = this.levelFilter.includes(1);
      const isLvlThree = this.levelFilter.includes(2);
      // if (this.isPossibleOutside) {
      //   params.append('isPossibleOutside', this.isPossibleOutside);
      // }
      // if (this.isPossibleInside) {
      //   params.append('isPossibleInside', this.isPossibleInside);
      // }
      if (this.isPossibleAlone) {
        params.append('isPossibleAlone', this.isPossibleAlone);
      }
      if (this.isPossibleDigital) {
        params.append('isPossibleDigital', this.isPossibleDigital);
      }
      if (this.isPrepairationNeeded) {
        params.append('isPrepairationNeeded', this.isPrepairationNeeded);
      }
      if (this.withoutCosts) {
        params.append('withoutCosts', this.withoutCosts);
      }
      if (!isLvlOne) {
        params.append('isLvlOne', isLvlOne);
      }
      if (!isLvlTwo) {
        params.append('isLvlTwo', isLvlTwo);
      }
      if (!isLvlThree) {
        params.append('isLvlThree', isLvlThree);
      }
      if (this.searchInput && this.searchInput !== '') {
        params.append('search', this.searchInput);
      }
      if (this.filterTags && this.filterTags.length) {
        this.filterTags.forEach((filterTag) => {
          params.append('filterTags', filterTag);
        });
      }
      if (this.isAuthenticated) {
        params.append('isActive', this.isActive);
      }
      params.append('sorter', this.sorter);
      params.append('page', 1);
      params.append('ts', Date.now());
      return params;
    },
  },

  methods: {
    loadMore() {
      const stillRunning = this.isLoadingMore;
      this.isLoadingMore = true;

      if (!stillRunning && this.nextPath !== null) {
        this.getMoreItems(this.axiosParams);
      }
    },

    async getMoreItems() {
      axios.get(this.nextPath)
        .then((res) => {
          this.items = this.items.concat(res.data.results);
          this.nextPath = res.data.next;
          this.loading = false;
          this.isLoadingMore = false;
        });
    },

    refresh() {
      this.items = [];
      this.getAllEventItems();
    },

    getAllEventItems() {
      const path = `${this.API_URL}basic/event/`;
      this.loading = true;

      axios.get(path, {
        params: this.axiosParams,
      })
        .then((res) => {
          this.items = res.data.results;
          this.nextPath = res.data.next;

          this.$store.commit('setHeimabendCounter', res.data.count);
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },

    onUpdateClick(item) {
      this.$emit('onUpdateClick', item);
    },

    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    onResetClick() {
      this.$store.commit('clearFilters');
    },
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(this.convertUrlToId(tag)); // eslint-disable-line
      });
      if (this.filterTags && this.filterTags.length) {
        const matches = eventTagArray.filter(element => this.filterTags.includes(element));
        return !!matches.length;
      }
      return true;
    },
    getItems(items, size, page) {
      const {
        // isPossibleInside,
        // isPossibleOutside,
        isPossibleAlone,
        isPossibleDigital,
        isPrepairationNeeded,
        isActive,
        withoutCosts,
        sorter,
        searchInput,
        levelFilter, // eslint-disable-line
      } = this.$store.getters;
      if (items && items.filter) {
        let returnArray = items
          .filter(item => item.description.toLowerCase().includes(searchInput.toLowerCase())
            || item.title.toLowerCase().includes(searchInput.toLowerCase())
            || item.material.toLowerCase().includes(searchInput.toLowerCase()))
          .filter(item => this.getFilterTags !== '13213' && this.isTagMatchToEvent(item))
          .filter(item => (!isPossibleAlone || isPossibleAlone === item.isPossibleAlone))
          .filter(item => (!isPossibleDigital || isPossibleDigital === item.isPossibleDigital))
          .filter((item) => {
            const allowOne = levelFilter.includes(0);
            const allowTwo = levelFilter.includes(1);
            const allowThree = levelFilter.includes(2);
            const allow = (allowOne && allowOne === item.isLvlOne)
              || (allowTwo && allowTwo === item.isLvlTwo)
              || (allowThree && allowThree === item.isLvlThree);
            return allow;
          })
          .filter(item => !isPrepairationNeeded || item.isPrepairationNeeded === false)
          .filter(item => isActive === item.isActive)
          .filter(item => !withoutCosts || item.costsRating === 0);
        if (sorter === 'alpha' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['title'], ['asc']);
        }
        if (sorter === 'newest' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['createdAt'], ['desc']);
        }
        if (sorter === 'random' && returnArray && returnArray.length) {
          returnArray = this._.shuffle(returnArray);
        }
        if (sorter === 'rating' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['like_score'], ['desc']);
        }
        return returnArray.slice(size, page);
      }
      return [];
    },
  },

  created() {
    this.getAllEventItems();
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: {},
    loading: true,
    nextPath: null,
  }),
};
</script>

<style scoped>
.bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background: url( 'back-2.jpg') no-repeat center center;
    background-size: 2000px 1300px;
    background-attachment: fixed;
    z-index: -1;
  }
</style>

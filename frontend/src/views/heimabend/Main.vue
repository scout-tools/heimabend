<template>
<div>
  <div class="col-sm-12">
    <heimabend-card
      v-if="getItems.length && !loading"
      @refresh="refresh()"
      :items="getItems"
      :isMobil="isMobil"
    />
    <v-btn
      class="ma-10"
      v-if="!getItems.length && !loading"
      @click="onResetClick()"
    >
      Alle Filter zurücksetzen
    </v-btn>
    <v-progress-circular
      v-if="loading"
      color="primary"
      indeterminate
    />
  </div>
</div>
</template>


<script>
import axios from 'axios';

import HeimabendCard from './cards/Heimabend.vue';

export default {
  components: {
    HeimabendCard,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    getItems() {
      const {
        // isPossibleInside,
        // isPossibleOutside,
        isPossibleAlone,
        isPossibleDigital,
        withoutPreperation,
        justActive,
        withoutCosts,
        getSorter,
        searchInput,
        levelFilter, // eslint-disable-line
      } = this.$store.getters;
      if (this.items && this.items.filter) {
        let returnArray = this.items
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
          .filter(item => !withoutPreperation || item.isPrepairationNeeded === false)
          .filter(item => justActive === item.isActive)
          .filter(item => !withoutCosts || item.costsRating === 0);
        if (getSorter === 'alpha' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['title'], ['asc']);
        }
        if (getSorter === 'newest' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['createdAt'], ['desc']);
        }
        if (getSorter === 'random' && returnArray && returnArray.length) {
          returnArray = this._.shuffle(returnArray);
        }
        if (getSorter === 'rating' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['like_score'], ['desc']);
        }
        this.$store.commit('setHeimabendCounter', returnArray.length);
        return returnArray;
      }
      return [];
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getFilterTags() {
      return this.$store.getters.filterTags;
    },
    tags() {
      return this.$store.getters.tags;
    },
  },

  methods: {
    refresh() {
      this.items = [];
      this.getEvents();
    },
    getEvents() {
      const path = `${this.API_URL}basic/event/`;
      this.loading = true;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
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
      if (this.getFilterTags && this.getFilterTags.length) {
        const matches = eventTagArray.filter(element => this.getFilterTags.includes(element));
        return !!matches.length;
      }
      return true;
    },
  },

  created() {
    this.getEvents();
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: {},
    loading: true,
  }),
};
</script>

<template>
<div>
  <div class="col-sm-12">
    <heimabend-card
      :items="getItems"
      :isMobil="isMobil"
      @onUpdateClick="onUpdateClick"
    />
    <v-btn
      class="ma-10"
      v-if="!getItems.length"
      @click="onResetClick()"
    >
      Alle Filter zurücksetzen
    </v-btn>
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
        isPossibleInside,
        isPossibleOutside,
        withoutPreperation,
        justActive,
        withoutCosts,
        getSorter,
        levelFilter, // eslint-disable-line
      } = this.$store.getters;
      if (this.items && this.items.filter) {
        let returnArray = this.items
          .filter(item => item.description.toLowerCase().includes(this.searchInput.toLowerCase())
            || item.title.toLowerCase().includes(this.searchInput.toLowerCase())
            || item.material.toLowerCase().includes(this.searchInput.toLowerCase()))
          .filter(item => this.getFilterTags !== '13213' && this.isTagMatchToEvent(item))
          .filter(item => (isPossibleInside === item.isPossibleInside
            || isPossibleOutside === item.isPossibleOutside)
            && (isPossibleInside || isPossibleOutside))
          .filter((item) => {
            const allowOne = levelFilter.includes(0);
            const allowTwo = levelFilter.includes(1);
            const allowThree = levelFilter.includes(2);
            const allow = (allowOne && allowOne === item.isLvlOne)
              || (allowTwo && allowTwo === item.isLvlTwo)
              || (allowThree && allowThree === item.isLvlThree);
            return allow;
          })
          .filter(item => !withoutPreperation || item.isPrepairationNeeded === true)
          .filter(item => justActive === item.isActive)
          .filter(item => !withoutCosts || item.costsRating === 1);
        if (getSorter === 'alpha' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['title'], ['asc']);
        }
        if (getSorter === 'newest' && returnArray && returnArray.length) {
          returnArray = this._.orderBy(returnArray, ['createdAt'], ['desc']);
        }
        if (getSorter === 'random' && returnArray && returnArray.length) {
          returnArray = this._.shuffle(returnArray);
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
  },

  methods: {
    getEvents() {
      const path = `${this.API_URL}basic/event/`;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {
        });
    },
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.tags = res.data;
        })
        .catch(() => {
        })
        .finally(() => {
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
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
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
    this.getTags();
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    searchInput: '',
    tags: [],
    items: {},
    loading: true,
  }),
};


</script>

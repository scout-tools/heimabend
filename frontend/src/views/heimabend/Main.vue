/* eslint-disable no-underscore-dangle */
<template>
<div>
  <div>
    <heimabend-card
      ref="eventCards"
      v-if="items.length"
      @refresh="refresh()"
      @loadMore="loadMore()"
      :items="items"
      :loading="loading"
      :isMobil="isMobil"
    />
    <v-container
      v-if="!items.length && !loading"
    >
      <v-row justify="center">
      <v-card
        color="primary"
        class="mx-auto ma-2 pa-3 test-color whiteText"
        elevation=30
      >
        Deine Suche führte leider zu keinem Treffer.
        Wir würden uns freuen, wenn du uns hilfst neue Ideen hinzuzufügen.
      </v-card>
      </v-row>
      <v-row
        justify="center"
        class="pa-5"
      >
        <v-btn
          color="secondary"
          @click="onResetClick()"
        >
          Alle Filter zurücksetzen
        </v-btn>
      </v-row>
    </v-container>
    <v-progress-circular
      v-if="loading"
      color="primary"
      indeterminate
    />
    <!-- <v-btn
      class="ma-10"
      v-if="count > items.length"
      @click="onClickLoadMore()"
    >
      Mehr laden
    </v-btn> -->
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
      this.isFirstEventsLoaded = false;
      this.refresh();
    },
    getFilterTags() {
    },
  },
  computed: {
    ...mapGetters([
      'searchInput',
      'sorter',
      'filterTags',
      'tags',
      'isAuthenticated',
      'heimabendCounter',
      'mandatoryFilter',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    axiosParams() {
      const params = new URLSearchParams();
      if (this.mandatoryFilter && this.mandatoryFilter.length) {
        this.mandatoryFilter.forEach((filterTag) => {
          params.append('filterTags', filterTag);
        });
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
      return params;
    },
  },

  methods: {
    // onClickLoadMore() {
    //   this.isLoadingMore = false;
    //   this.loadMore();
    // },
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
          this.trackItems(res.data.results);
        })
        .catch(() => {
          this.loading = false;
          this.isLoadingMore = false;
        });
    },

    refresh() {
      if (this.saveFilterLastFilter.toString() !== this.axiosParams.toString()) {
        this.getAllEventItems();
        this.saveFilterLastFilter = this.axiosParams;
      }
    },

    getAllEventItems() {
      const path = `${this.API_URL}basic/event/`;
      this.loading = true;

      this.isFirstEventsLoaded = true;
      axios.get(path, {
        params: this.axiosParams,
      })
        .then((res) => {
          this.items = res.data.results;
          this.nextPath = res.data.next;
          this.count = res.data.count;
          this.$store.commit('setHeimabendCounter', this.count);
          this.loading = false;
          this.isLoadingMore = false;
          // eslint-disable-next-line no-undef
          this.trackItems(res.data.results);
        })
        .catch(() => {
          this.loading = false;
          this.isLoadingMore = false;
        });
    },

    onUpdateClick(item) {
      this.$emit('onUpdateClick', item);
    },
    trackItems(items) {
      items.forEach((item) => {
        // eslint-disable-next-line no-undef
        _paq.push(['trackContentImpression', item.title, item.id]);
      });
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
  },

  created() {
    this.refresh();
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: {},
    loading: true,
    nextPath: null,
    isLoadingMore: false,
    count: 0,
    saveFilterLastFilter: false,
  }),
};
</script>

<style scoped>

  .test-color {
    background-color: rgba(255, 254, 254, 0.952) !important;
  }
  .whiteText {
    color: white !important;
  }
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

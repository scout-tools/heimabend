/* eslint-disable no-underscore-dangle */
<template>
  <div>
    <heimabend-card
      ref="eventCards"
      @refresh="refresh()"
      @loadMore="loadMore()"
      :items="heimabendItems"
      :loading="loading"
      :isMobil="isMobil"
    />
    <v-container v-if="!heimabendItems.length && !loading">
      <v-row justify="center">
        <v-card
          color="primary"
          class="mx-auto ma-2 pa-3 test-color whiteText"
          elevation="30"
        >
          Deine Suche führte leider zu keinem Treffer. Wir würden uns freuen,
          wenn du uns hilfst neue Ideen hinzuzufügen.
        </v-card>
      </v-row>
      <v-row justify="center" class="pa-5">
        <v-btn color="secondary" @click="onResetClick()">
          Alle Filter zurücksetzen
        </v-btn>
      </v-row>
    </v-container>
    <v-progress-circular v-if="loading" color="primary" indeterminate />
    <v-snackbar v-model="showSuccess" color="success" top :timeout="timeout">
      Vielen Dank für deine Heimabend-Idee! <br />
      <br />
      Wir freuen unsüber deinen Beitrag zum Inspirator. <br />
      Das Team wird sich deiner Idee zeitnah widmen und sie veröffentlichen.
      <br />
      Bei Rückfragen dazu melden wir uns über die von dir angegebene
      E-Mail-Adresse bei dir. <br />
      Wenn du Fragen an uns hast, nutze gerne das Kontaktformular. <br />
    </v-snackbar>
    <!-- <v-btn
      class="ma-10"
      @click="loadMore()"
    >
      Mehr laden
    </v-btn> -->
    <span v-if="!isMobil" class="bg" />
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
      this.$store.commit('resetHeimabendItems');
      this.refresh();
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
      'isActive',
      'heimabendItems',
      'scollPosition',
      'nextPath',
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
      params.append('ordering', this.sorter);
      params.append('page', 1);
      params.append('timestamp', new Date().getTime());
      return params;
    },
    showSuccess() {
      return !!this.$route.params.showSuccess;
    },
  },

  methods: {
    loadMore() {
      const stillRunning = this.isLoadingMore;
      this.isLoadingMore = true;
      if (!stillRunning) {
        this.getMoreItems(this.axiosParams);
      }
    },

    async getMoreItems() {
      axios
        .get(this.nextPath.replace(/^http:\/\//i, 'https://')) //
        .then((res) => {
          this.$store.commit('extendHeimabendItems', res.data.results);
          this.$store.commit('setNextPath', res.data.next);
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
      if (
        this.saveFilterLastFilter.toString() !== this.axiosParams.toString()
      ) {
        this.getAllEventItems();
        this.saveFilterLastFilter = this.axiosParams;
      }
      this.$store.commit('setIsScoringMode', false);
    },

    getAllEventItems() {
      const path = `${this.API_URL}basic/event/`;
      this.loading = true;

      this.isFirstEventsLoaded = true;
      axios
        .get(path, {
          params: this.axiosParams,
        })
        .then((res) => {
          this.$store.commit('extendHeimabendItems', res.data.results);
          this.$store.commit('setNextPath', res.data.next);
          this.count = res.data.count;
          this.$store.commit('setHeimabendCounter', this.count);
          this.loading = false;
          this.isLoadingMore = false;
          // eslint-disable-next-line no-undef
          this.callTrackItems(res.data.results);
        })
        .catch(() => {
          this.loading = false;
          this.isLoadingMore = false;
        });
    },

    onUpdateClick(item) {
      this.$emit('onUpdateClick', item);
    },
    callTrackItems(items) {
      items.forEach((item) => {
        // eslint-disable-next-line no-undef
        _paq.push(['trackContentImpression', item.title, item.id]);
      });
    },
    onResetClick() {
      this.resetAllFilter();
    },
    resetAllFilter() {
      this.$store.commit('clearFilters');
    },
  },

  created() {
    setTimeout(() => {
      window.scrollTo(0, this.scollPosition);
    }, 500);
  },

  mounted() {
    this.$store.commit('setIsScoringMode', false);
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    loading: true,
    isLoadingMore: false,
    count: 0,
    timeout: 13000,
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
</style>

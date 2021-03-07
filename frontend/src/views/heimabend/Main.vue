/* eslint-disable no-underscore-dangle */
<template>
  <v-container fluid>
    <heimabend-card
      ref="eventCards"
      @refresh="refresh()"
      @loadMore="loadMore()"
      :items="items"
      :loading="loading"
      :isMobil="isMobil"
    />
    <v-container v-if="!items.length && !loading">
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
      v-if="count > items.length"
      @click="onClickLoadMore()"
    >
      Mehr laden
    </v-btn> -->
    <span v-if="!isMobil" class="bg" />
  </v-container>
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
    getFilterTags() {},
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

      if (!stillRunning && this.nextPath !== null) {
        this.getMoreItems(this.axiosParams);
      }
    },

    async getMoreItems() {
      axios
        .get(this.nextPath.replace(/^http:\/\//i, 'https://')) //
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
    onResetClick() {
      this.$store.commit('clearFilters');
    },
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(tag); // eslint-disable-line
      });
      if (this.filterTags && this.filterTags.length) {
        const matches = eventTagArray.filter((element) => // eslint-disable-line
          this.filterTags.includes(element) // eslint-disable-line
        ); // eslint-disable-line
        return !!matches.length;
      }
      return true;
    },
  },

  created() {
    this.refresh();
  },

  mounted() {
    this.$store.commit('setIsScoringMode', false);
    this.refresh();
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: [],
    loading: true,
    nextPath: null,
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

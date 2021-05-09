/* eslint-disable no-underscore-dangle */
<template>
  <v-container fluid>
    <v-row v-if="!isEventLoading || heimabendItems.length">
    <heimabend-card
      ref="eventCards"
      @refresh="refresh()"
      @loadMore="loadMore()"
      :items="heimabendItems"
      :loading="isEventLoading"
      :isMobil="isMobil"
    />
    <v-container fluid v-if="!heimabendItems.length && !isEventLoading" style="margin-right: 200px">
      <v-row justify="center">
        <v-img
          :src="require('@/assets/inspi/inspi_confused.png')"
          max-width="200"
          class="mt-4"
        />
      </v-row>

      <v-row justify="center" class="pa-5">
        <v-btn color="primary" @click="onResetClick()">
          <v-icon left>
            mdi-filter-remove
          </v-icon>
          Alle Filter zurücksetzen
        </v-btn>
      </v-row>
    </v-container>
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
    </v-row>
    <v-row class="mt-10" align="center" justify="center" v-else>
      <v-card flat >
        <div class="text-center ma-5">
          <p> Lade Daten ...</p>
          <v-progress-circular
            :size="80"
            :width="10"
            class="ma-5"
            color="primary"
            indeterminate
          ></v-progress-circular>
          <p> Bitte hab etwas Geduld.</p>
        </div>
      </v-card>
    </v-row>
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
      this.refresh();
    },
  },
  computed: {
    ...mapGetters([
      'searchInput',
      'filterTags',
      'tags',
      'isAuthenticated',
      'heimabendCounter',
      'mandatoryFilter',
      'isPublic',
      'heimabendItems',
      'scollPosition',
      'nextPath',
      'isEventLoading',
      'isFirstEventLoaded',
      'saveFilterLastFilter',
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
        this.getMoreItems();
      }
    },

    async getMoreItems() {
      let path = this.nextPath;
      if (process.env.VUE_APP_API !== 'http://localhost:8000/') {
        path = this.nextPath.replace(/^http:\/\//i, 'https://');
      }
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('extendHeimabendItems', res.data.results);
          this.$store.commit('setNextPath', res.data.next);
          this.$store.commit('setIsEventLoading', false);
          this.isLoadingMore = false;
          this.trackItems(res.data.results);
        })
        .catch(() => {
          this.$store.commit('setIsEventLoading', false);
          this.isLoadingMore = false;
        });
    },

    refresh() {
      if (
        this.saveFilterLastFilter !== this.axiosParams.toString()
        && !this.isFirstEventLoaded
      ) {
        if (this.nextPath) {
          this.getMoreItems();
        } else {
          this.getAllEventItems();
        }
        this.$store.commit('setSaveFilterLastFilter', this.axiosParams.toString());
      }
      this.$store.commit('setIsScoringMode', false);
    },

    getAllEventItems() {
      const path = `${this.API_URL}basic/event/`;
      this.$store.commit('setIsEventLoading', true);
      this.$store.commit('setIsFirstEventLoaded', true);
      axios
        .get(path, {
          params: this.axiosParams,
        })
        .then((res) => {
          this.$store.commit('extendHeimabendItems', res.data.results);
          this.$store.commit('setNextPath', res.data.next);
          this.count = res.data.count;
          this.$store.commit('setHeimabendCounter', this.count);
          this.$store.commit('setIsEventLoading', false);
          this.isLoadingMore = false;
          // eslint-disable-next-line no-undef
          this.callTrackItems(res.data.results);
          this.getTags();
        })
        .catch(() => {
          this.$store.commit('setIsEventLoading', false);
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
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(tag); // eslint-disable-line
      });
      if (this.filterTags && this.filterTags.length) {
        const matches = eventTagArray.filter(
          ( // eslint-disable-line
            element // eslint-disable-line
          ) => this.filterTags.includes(element) // eslint-disable-line
        ); // eslint-disable-line
        return !!matches.length;
      }
      return true;
    },
    resetAllFilter() {
      this.$store.commit('clearFilters');
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
    getTags() {
      const path = `${
        this.API_URL
      }basic/tag/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTags', res.data);
          this.getTagCategory();
        })
        .catch(() => {
          this.showError = true;
        });
    },
    getTagCategory() {
      const path = `${
        this.API_URL
      }basic/tag-category/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTagCategory', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
  },

  created() {
    this.$store.commit('setIsSubPage', false);
    setTimeout(() => {
      window.scrollTo(0, this.scollPosition);
    }, 500);
    if (!this.nextPath) {
      this.getAllEventItems();
    }
  },

  mounted() {
    this.$store.commit('setIsScoringMode', false);
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    isLoadingMore: false,
    count: 0,
    timeout: 13000,
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

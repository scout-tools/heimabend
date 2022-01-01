<template>
  <v-navigation-drawer
    app
    temporary
    v-bind:value="isExtended"
    :width="isMobil ? '99%': '50%'"
    right
    @input="test"
    class="mt-12"
  >
    <v-app-bar hide-on-scroll>
      <v-icon @click="onExpandClick" class="mr-1">mdi-close</v-icon>
        <h3 class="mx-2">{{heimabendCounter }} Heimabende gefunden</h3>
      <v-spacer/>
      <v-btn icon ml-1 @click="onClickRestore" color="black" :disabled="isFilterDefault">
        <v-icon>
          mdi-filter-remove
        </v-icon>
      </v-btn>
    </v-app-bar>
    <v-container fluid class="ml-4 pa-0 pb-12 my-12">
      <v-row
        v-for="category in getTopBarTagCategories"
        :key="category.id"
        class="ml-1 my-2"
      >
        <filter-tags :category="category" />
      </v-row>
      <v-row
        v-for="(numberFilterData, index) in scoreConfig"
        :key="`filter-${index}`"
      >
        <FilterButtomBar :data="numberFilterData" />
      </v-row>
    </v-container>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterTags from '@/views/components/dropdown/FilterTags.vue'; //eslint-disable-line
import FilterButtomBar from '@/views/components/button/FilterButtomBar.vue'; //eslint-disable-line
import { configData } from '@/mixins/configData.js'; //eslint-disable-line

export default {
  mixins: [configData],
  components: {
    FilterButtomBar,
    FilterTags,
  },
  data() {
    return {
    };
  },
  watch: {
  },
  created() {
    setTimeout(() => { // ugly work around
      this.$store.commit('setIsExtended', false);
    }, 50);
  },
  computed: {
    ...mapGetters([
      'isPrepairationNeeded',
      'withoutCosts',
      'searchInput',
      'sorter',
      'tags',
      'tagCategory',
      'isAuthenticated',
      'heimabendCounter',
      'mandatoryFilter',
      'isExtended',
      'numberFilter',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    getTopBarTagCategories() {
      if (this.tagCategory) {
        if (this.isMobil) {
          return this.tagCategory;
        }
        return this.tagCategory;
      }
      return [];
    },
    isFilterDefault() {
      return !(
        (this.mandatoryFilter && this.mandatoryFilter.length) || // eslint-disable-line
        this.getFilterTags.length || // eslint-disable-line
        (this.numberFilter && this.numberFilter.length)
      );
    },
  },
  methods: {
    onClickRestore() {
      this.$store.commit('clearFilters');
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
    test(value) {
      this.$store.commit('setIsExtended', value);
    },
    onExpandClick() {
      this.$store.commit('setIsExtended', false);
    },
  },
};
</script>

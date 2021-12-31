<template>
  <v-navigation-drawer
    app
    absolute
    temporary
    v-bind:value="isExtended"
    :width="isMobil ? '90%': '50%'"
    right
    @input="test"
    class="mt-20"
  >
    <v-container fluid class="ml-10 pa-0 mt-20">
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
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getTopBarTagCategories() {
      if (this.tagCategory) {
        if (this.isMobil) {
          return this.tagCategory;
        }
        return this.tagCategory.filter(item => item.isHeader);
      }
      return [];
    },
  },
  methods: {
    test(value) {
      this.$store.commit('setIsExtended', value);
    },
  },
};
</script>

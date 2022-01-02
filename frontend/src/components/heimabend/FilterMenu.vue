<template>
  <v-navigation-drawer
    app
    v-bind:value="isExtended"
    :width="isMobil ? '99%' : '350px'"
    right
    @input="test"
  >
    <v-app-bar dark color="inspiBlue">
      <v-icon v-show="isMobil" @click="onExpandClick" class="mr-1"
        >mdi-arrow-left</v-icon
      >
      <h3 class="mx-2">{{ heimabendCounter }} Heimabende gefunden</h3>
      <v-spacer />
      <v-btn
        icon
        ml-1
        @click="onClickRestore"
        dark
        :disabled="isFilterDefault"
      >
        <v-icon> mdi-filter-remove </v-icon>
      </v-btn>
    </v-app-bar>
    <v-container fluid class="pa-3">
      <v-row>
        <v-expansion-panels flat accordion>
          <v-expansion-panel
            v-for="category in getTopBarTagCategories"
            :key="category.id"
          >
            <v-expansion-panel-header>
              <v-container>
                <v-row>
                  <!-- <v-icon class="mx-1">{{
                    category.icon
                  }}</v-icon> -->
                  <h3>{{ category.name }}</h3>
                </v-row>
              </v-container>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <FilterCheckboxCategory :data="category" />
            </v-expansion-panel-content>
            <v-divider />
          </v-expansion-panel>
          <v-expansion-panel
            v-for="(numberFilterData, index) in scoreConfig"
            :key="`filter-${index}`"
          >
            <v-expansion-panel-header>
              <v-container>
                <v-row>
                  <!-- <v-icon class="mx-1">
                    {{ numberFilterData.icon }}
                  </v-icon> -->
                  <h3>{{ numberFilterData.name }}</h3>
                </v-row>
              </v-container>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <FilterCheckboxElement :data="numberFilterData" />
            </v-expansion-panel-content>
            <v-divider />
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>
    </v-container>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterTags from '@/views/components/dropdown/FilterTags.vue'; //eslint-disable-line
import FilterCheckboxElement from '@/views/components/button/FilterCheckboxElement.vue'; //eslint-disable-line
import FilterCheckboxCategory from '@/views/components/button/FilterCheckboxCategory.vue'; //eslint-disable-line
import { configData } from '@/mixins/configData.js'; //eslint-disable-line

export default {
  mixins: [configData],
  components: {
    FilterCheckboxElement,
    FilterCheckboxCategory,
  },
  data() {
    return {};
  },
  watch: {},
  created() {
    setTimeout(() => {
      // ugly work around
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
      this.$store.dispatch('resetFilters');
    },
    test(value) {
      this.$store.commit('setIsExtended', value);
    },
    onExpandClick() {
      this.$store.commit('setIsExtended', false);
    },
    getColor(id) {
      const colors = {
        1: 'inspiRed',
        2: 'inspiBlue',
        3: 'green',
        4: 'inspiRed',
        5: 'inspiBlue',
        8: 'inspiOrange',
        9: 'inspiOrange',
      };
      return colors[id];
    },
  },
};
</script>

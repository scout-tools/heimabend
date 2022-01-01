<template>
  <v-toolbar fixed flat color="#F6F6F6">
    <template>
      <!-- <h6 class="mx-2">{{heimabendCounter }} gefunden</h6> -->
      <active-filter />
      <v-spacer />
      <v-btn
        v-if="isMobil"
        icon
        ml-1
        @click="onClickRestore"
        color="black"
        :disabled="isFilterDefault"
      >
        <v-icon> mdi-filter-remove </v-icon>
      </v-btn>

      <v-tooltip v-if="isMobil" nudge-left="80" bottom>
        <template v-slot:activator="{ on }">
          <v-btn @click="onExpandClick()" fab v-on="on" text>
            <v-icon> mdi-filter-menu </v-icon>
          </v-btn>
        </template>
        <span> Filter </span>
      </v-tooltip>

      <v-container fluid v-if="!isMobil">
        <v-row align="center" justify="center">
          <v-col
            v-for="category in getTopBarTagCategories"
            :key="category.id"
            cols="1.4"
          >
            <filter-tags :category="category" />
          </v-col>
          <v-col cols="2" v-if="!isMobil"></v-col>
        </v-row>
      </v-container>
    </template>
  </v-toolbar>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterTags from '@/views/components/dropdown/FilterTags.vue'; //eslint-disable-line
import ActiveFilter from '@/views/components/button/ActiveFilter.vue'; //eslint-disable-line

export default {
  components: {
    FilterTags,
    ActiveFilter,
  },
  data() {
    return {};
  },
  methods: {
    onClickRestore() {
      this.$store.dispatch('resetFilters');
    },
    onExpandClick() {
      this.$store.commit('setIsExtended', true);
    },
    onChange() {
      this.$store.commit('changeFilterTags', this.filterTags);
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
    onCloseChip(value) {
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('removeOneFilter', value);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
  },
  watch: {
    getFilterTags() {},
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
    getTopBarTagCategories() {
      if (this.tagCategory) {
        if (this.isMobil) {
          return this.tagCategory;
        }
        return this.tagCategory.filter(item => item.isHeader);
      }
      return [];
    },
    extensionHeightNumber() {
      return this.isMobil ? '350px' : '50px';
    },
    isFilterDefault() {
      return !(
        (this.mandatoryFilter && this.mandatoryFilter.length) || // eslint-disable-line
        this.getFilterTags.length || // eslint-disable-line
        (this.numberFilter && this.numberFilter.length)
      );
    },
    isMobil() {
      return true;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
  },
};
</script>

<template>
  <v-toolbar
    fixed
    :extension-height="extensionHeightNumber"
    :extended="isExtended && isMobil"
  >
    <v-spacer/>
    <template>
        <v-tooltip
          v-if="isMobil"
          nudge-left="80"
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              @click="onExpandClick()"
              fab
              v-on="on"
              text
            >
              <v-icon
              v-if="!isExtended"
                >
                mdi-chevron-down
              </v-icon>
              <v-icon
              v-if="isExtended"
                >
                mdi-chevron-up
              </v-icon>
            </v-btn>
          </template>
          <span>
            Mehr Filter
          </span>
        </v-tooltip>

        <v-container fluid class="mx-5 pa-0" >
          <v-row
            align="center"
            class="ma-0 pa-0"
              justify="center">
              <v-col
                v-for="category in getTopBarTagCategories"
                :key="category.id"
                cols="1.5">
                <filter-button
                  :category="category"
                />
              </v-col>
              <v-col cols="1.5">
                <sorter/>
              </v-col>
              <v-col cols="1.5">
              <v-btn icon ml-1 @click="onClickRestore" :disabled="isFilterDefault">
                <v-icon>
                  mdi-restore
                </v-icon>
              </v-btn>
            </v-col>
              <v-col cols="1.5" v-if="!isMobil">
              </v-col>
          </v-row>
        </v-container>


    </template>
  <template
        #extension
        v-if="isExtended && isMobil"
      >
    <v-container class="pa-0" style="margin: 0px; width: 100%">
      <v-row v-if="isExtended && isMobil">
      <v-col cols="2">
        <filter-button
          :customIcon="'wolf'"
          :customText="'WÖ'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlOne"
          :customVariable="'isLvlOne'"
          :customMutation="'setIsLvlOne'"
        />
      </v-col>
      <v-col cols="2">
        <filter-button
          :customIcon="'scout'"
          :customText="'Pfadi'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlTwo"
          :customVariable="'isLvlTwo'"
          :customMutation="'setIsLvlTwo'"
        />
      </v-col>
      <v-col cols="2">
        <filter-button
          :customIcon="'rover'"
          :customText="'Rover'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlThree"
          :customVariable="'isLvlThree'"
          :customMutation="'setIsLvlThree'"
        />
      </v-col>
      <v-col cols="2">
        <div>
          <v-spacer/>
        </div>
      </v-col>
      </v-row>
      <v-layout wrap>
        <div class="pa-0">
          <v-chip-group
            multiple
            :column="isMobil"
            v-model="filterTags"
            @change="onChange()"
          >
            <v-chip
              filter
              x-small
              v-for="(tag, index) in tags"
              :value="tag.id"
              :key="index"
              :color="tag.color">
              {{ tag.name }}
            </v-chip>
          </v-chip-group>
        </div>
      </v-layout>
    </v-container>
      </template>
  </v-toolbar>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterButton from '@/views/components/button/FilterButton.vue'; //eslint-disable-line
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    FilterButton,
    Sorter,
  },
  data() {
    return {
      isExtended: false,
    };
  },
  methods: {
    onClickRestore() {
      this.$store.commit('clearFilters');
    },
    onExpandClick() {
      this.isExtended = !this.isExtended;
    },
    onChange() {
      this.$store.commit('changeFilterTags', this.filterTags);
    },
  },
  watch: {
    getFilterTags() {
    },
  },
  computed: {
    ...mapGetters([
      'isPossibleInside',
      'isPossibleOutside',
      'isPossibleAlone',
      'isPossibleDigital',
      'isPrepairationNeeded',
      'isActive',
      'withoutCosts',
      'searchInput',
      'sorter',
      'isLvlOne',
      'isLvlTwo',
      'isLvlThree',
      'tags',
      'tagCategory',
      'isAuthenticated',
      'heimabendCounter',
    ]),
    getTopBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory.filter(item => item.is_header);
      }
      return [];
    },
    extensionHeightNumber() {
      return this.isMobil ? '350px' : '50px';
    },
    isFilterDefault() {
      return this.isPossibleAlone === false
        && this.isPossibleDigital === false
        && this.isPrepairationNeeded === false
        && this.withoutCosts === false
        && this.searchInput === ''
        && this.filterTags.length < 1
        && this.isLvlOne === false
        && this.isLvlTwo === false
        && this.isLvlThree === false;
    },
    isIsActive: {
      get() {
        return this.$store.getters.isActive;
      },
      set() {
        return false;
      },
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
  },
};
</script>

<style scoped>
span {
  font-size: 12px !important;
}
</style>

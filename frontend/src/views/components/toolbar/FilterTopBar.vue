<template>
  <v-toolbar
    v-if="!isExtended"
    fixed
  >
    <template>
      <active-filter v-if="isMobil"/>

      <v-spacer/>

      <v-btn
        v-if="isMobil"
        icon
        ml-1
        @click="onClickRestore"
        color="black"
        :disabled="isFilterDefault"
      >
        <v-icon>
          mdi-filter-remove
        </v-icon>
      </v-btn>
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
            <v-icon>
              mdi-filter-menu
            </v-icon>
          </v-btn>
        </template>
        <span>
          Mehr Filter
        </span>
      </v-tooltip>

      <v-container fluid class="mx-5 pa-0" v-if="!isMobil">
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
            <v-btn
              icon
              ml-1
              @click="onClickRestore"
              color="black"
              :disabled="isFilterDefault">
              <v-icon>
                mdi-filter-remove
              </v-icon>
            </v-btn>
          </v-col>
            <v-col cols="1.5" v-if="!isMobil">
            </v-col>
        </v-row>
      </v-container>


    </template>
  </v-toolbar>
  <v-navigation-drawer absolute temporary v-model="isExtended" width="100%" right v-else>
    <v-app-bar hide-on-scroll>
      <v-icon @click="onExpandClick" class="mr-1">mdi-arrow-left</v-icon>
        <active-filter v-if="isMobil"/>
      <v-spacer/>
      <v-btn icon ml-1 @click="onClickRestore" color="black" :disabled="isFilterDefault">
        <v-icon>
          mdi-filter-remove
        </v-icon>
      </v-btn>
    </v-app-bar>
    <v-container fluid class="mx-5 pa-0">
      <v-row
        v-for="category in getTopBarTagCategories"
        :key="category.id"
        class="ml-1 mr-10 my-5">
        <filter-button
          :category="category"
        />
      </v-row>
      <v-row class="ml-1 mr-10 my-5">
        <sorter/>
      </v-row>
    </v-container>
 </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterButton from '@/views/components/button/FilterButton.vue'; //eslint-disable-line
import ActiveFilter from '@/views/components/button/ActiveFilter.vue'; //eslint-disable-line
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    FilterButton,
    ActiveFilter,
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
    onCloseChip(value) {
      this.$store.commit('removeOneFilter', value);
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
      'mandatoryFilter',
    ]),
    getTopBarTagCategories() {
      if (this.tagCategory) {
        if (this.isMobil) {
          return this.tagCategory;
        }
        return this.tagCategory.filter(item => item.is_header);
      }
      return [];
    },
    extensionHeightNumber() {
      return this.isMobil ? '350px' : '50px';
    },
    isFilterDefault() {
      return !((this.mandatoryFilter && this.mandatoryFilter.length) || this.getFilterTags.length);
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

<template>
  <v-toolbar
    class="top-toolbar"
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
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'mdi-robot'"
          :customColor="'red'"
          :customText="'Digital'"
          :customTooltip="'Zeigt Ideen an die mit deiner Sippe digitaldurchgeführt werden können.'"
          :customTrigger="isPossibleDigital"
          :customVariable="'isPossibleDigital'"
          :customMutation="'setPossibleDigital'"
        />
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'mdi-account-cowboy-hat'"
          :customColor="'black'"
          :customText="'Alleine'"
          :customTooltip="'Zeigt Heimabende an die alleine durchführbar sind'"
          :customTrigger="isPossibleAlone"
          :customVariable="'isPossibleAlone'"
          :customMutation="'setPossibleAlone'"
        />
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'mdi-card-bulleted-off-outline'"
          :customColor="'black'"
          :customText="'Arbeit.'"
          :customTooltip="'Zeigt nur Heimabende an die keine Vorbereitung benötigen'"
          :customTrigger="isPrepairationNeeded"
          :customVariable="'isPrepairationNeeded'"
          :customMutation="'setIsPreperationNeeded'"
        />
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'mdi-currency-usd-off'"
          :customColor="'red'"
          :customText="'Kosten'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="withoutCosts"
          :customVariable="'withoutCosts'"
          :customMutation="'setWithoutCosts'"
        />
      <v-divider v-if="!isMobil" class="mx-0" vertical/>
        <filter-button
          v-if="!isMobil"
          :customIcon="'wolf'"
          :customText="'WÖ'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlOne"
          :customVariable="'isLvlOne'"
          :customMutation="'setIsLvlOne'"
        />
      <v-divider v-if="!isMobil" class="mx-0" vertical/>
        <filter-button
          v-if="!isMobil"
          :customIcon="'scout'"
          :customText="'Pfadi'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlTwo"
          :customVariable="'isLvlTwo'"
          :customMutation="'setIsLvlTwo'"
        />
      <v-divider v-if="!isMobil" class="mx-0" vertical/>
        <filter-button
          v-if="!isMobil"
          :customIcon="'rover'"
          :customText="'Rover'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlThree"
          :customVariable="'isLvlThree'"
          :customMutation="'setIsLvlThree'"
        />
      <v-divider class="mx-0" vertical/>
      <v-btn icon @click="onClickRestore" v-if="!isFilterDefault">
        <v-icon>
          mdi-restore
        </v-icon>
      </v-btn>
    </template>
  <template
        #extension
        v-if="isExtended && isMobil"
      >
    <v-container class="pa-0" style="margin: 0px; width: 100%">
      <v-row v-if="isExtended && isMobil">
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'wolf'"
          :customText="'WÖ'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlOne"
          :customVariable="'isLvlOne'"
          :customMutation="'setIsLvlOne'"
        />
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'scout'"
          :customText="'Pfadi'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlTwo"
          :customVariable="'isLvlTwo'"
          :customMutation="'setIsLvlTwo'"
        />
      <v-divider class="mx-0" vertical/>
        <filter-button
          :customIcon="'rover'"
          :customText="'Rover'"
          :customTooltip="'Zeigt Heimabende an für die keine Kosten entstehen.'"
          :customTrigger="isLvlThree"
          :customVariable="'isLvlThree'"
          :customMutation="'setIsLvlThree'"
        />
      <v-divider class="mx-0" vertical/>
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
  <v-spacer class="right-menu-margin"/>
  </v-toolbar>
</template>

<script>
import { mapGetters } from 'vuex';

import FilterButton from '@/views/components/button/FilterButton.vue'; //eslint-disable-line

export default {
  components: {
    FilterButton,
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
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', this.filterTags);
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', []);
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
      'filterTags',
      'tags',
      'isAuthenticated',
      'heimabendCounter',
    ]),
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

.v-btn {
  padding-left: 6px !important;
  padding-right: 6px !important;
}

.right-menu-margin {
  margin-right: 240px;
}
span {
  font-size: 12px !important;
}
</style>

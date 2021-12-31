<template>
  <v-container class="ma-0 pr-12" fluid>
    <v-select
      v-model="selectedFilter"
      :items="filterTagByCategory"
      :label="`${category.name}`"
      item-value="id"
      item-text="name"
      multiple
      dense
      hide-details
      single-line
      solo-inverted
      :prepend-inner-icon="category.icon"
      @change="onFilterChanged"
    >
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="index === 0" :color="item.color" small>
          <span>{{ item.name }}</span>
        </v-chip>
        <span
          v-if="index === 1"
          class="grey--text caption"
        >
          (+ ...)
        </span>
      </template>
    </v-select>
  </v-container>
</template>
<script>
import { mapGetters } from 'vuex';

export default {
  props: {
    category: {
      type: Object,
    },
  },
  data() {
    return {
      selectedFilter: [],
      lastFilter: [],
      isPublicState: false,
      value: [],
    };
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
    ]),
    filterTagByCategory() {
      return this.tags.filter(item => item.category === this.category.id);
    },
  },
  watch: {
    mandatoryFilter(value) {
      this.lastFilter = value;
      this.selectedFilter = value;
    },
  },
  methods: {
    getDivClass() {
      return !this.isMobil ? 'mx-2' : 'mx-0';
    },
    updateState() {
      this.isPublicState = this.$store.getters[this.customVariable];
    },
    // eslint-disable-next-line no-unused-vars
    onFilterChanged(newValue) {
      if (newValue) {
        if (newValue.length > this.lastFilter.length) {
          const difference = newValue.filter(x => !this.lastFilter.includes(x));
          const oldFilter = this.mandatoryFilter;
          oldFilter.push(difference[0]);
          this.$store.commit('changeMandatoryFilter', oldFilter);
          this.$store.commit('setNextPath', false);
          this.$store.commit('resetHeimabendItems', []);
          this.$store.commit('setIsFirstEventLoaded', false);
        } else {
          // const oldFilter = this.mandatoryFilter;
          const categoryItems = this.filterTagByCategory;
          const difference = categoryItems.filter(x => this.lastFilter.includes(x.id))[0].id;
          const oldFilter = this.mandatoryFilter;
          const index = oldFilter.indexOf(difference);
          oldFilter.splice(index, 1);
          this.$store.commit('changeMandatoryFilter', oldFilter);
          this.$store.commit('setNextPath', false);
          this.$store.commit('resetHeimabendItems', []);
          this.$store.commit('setIsFirstEventLoaded', false);
        }
      }
      this.lastFilter = newValue;
    },
  },
  mounted() {
    this.updateState();
  },
};
</script>

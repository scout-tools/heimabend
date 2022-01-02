<template>
  <v-container>
    <v-row align="center">
      <v-col
        v-for="(filter, index) in data.rankings"
        :key="index"
        cols="6"
        sm="6"
        md="6"
        class="pa-0"
      >
        <v-checkbox
          v-model="value"
          :label="filter.name"
          color="green"
          :value="filter.score"
          hide-details
          @click="onButtonClicked(filter)"
        ></v-checkbox>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  props: {
    data: Object,
  },
  methods: {
    onButtonClicked(filter) {
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
      if (!this.value.includes(filter.score)) {
        this.$store.commit('addNumberFilter', filter);
      } else {
        this.$store.commit('removeNumberFilter', filter);
      }
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    ...mapGetters(['tags', 'tagCategory', 'mandatoryFilter', 'numberFilter', 'filterTags']),
    value() {
      if (this.mandatoryFilter || this.filterTags || this.numberFilter) {
        return this.numberFilter.filter(
          item => item.techname === this.data.techname,
        ).map(a => a.score);
      }
      return this.numberFilter;
    },
  },
};
</script>

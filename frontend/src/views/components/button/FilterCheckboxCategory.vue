<template>
  <v-container>
    <v-row align="center">
      <v-col
        v-for="(filter, index) in filterTagByCategory"
        :key="index"
        cols="6"
        sm="6"
        md="6"
        class="pa-0"
      >
        <v-checkbox
          v-model="currentValues"
          :label="filter.name"
          :value="filter.id"
          color="green"
          hide-details
          @click="onFilterChanged(filter)"
        ></v-checkbox>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data: () => ({
  }),
  props: {
    data: Object,
  },
  methods: {
    onFilterChanged(filter) {
      if (!this.currentValues.includes(filter.id)) {
        this.$store.commit('addMandatoryFilter', filter.id);
      } else {
        this.$store.commit('removeMandatoryFilter', filter.id);
      }
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    filterTagByCategory() {
      return this.tags.filter(item => item.category === this.data.id);
    },
    ...mapGetters(['tags', 'tagCategory', 'mandatoryFilter', 'numberFilter']),
    currentValues() {
      return this.mandatoryFilter;
    },
  },
};
</script>

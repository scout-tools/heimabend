<template>
  <v-container>
    <v-row align="center" justify="center" class="ma-0 pa-0">
      <v-col :cols="isMobil ? 3 : 1">
        <v-icon large :color="data.color">
          {{ data.icon }}
        </v-icon>
      </v-col>
      <v-col :cols="isMobil ? 7 : 3" class="ma-0 pa-0">
        <p class="text-left title ma-3" :color="data.color">{{ data.name }}</p>
      </v-col>
    </v-row>
    <v-row align="center">
      <v-btn-toggle :value="value" :small="isMobil" borderless tile group>
        <v-btn :small="isMobil" @click="onAllButtonClicked" value="-1">
          Alle
        </v-btn>
        <v-btn
          :small="isMobil"
          :value="filter.score"
          v-for="(filter, index) in data.rankings"
          :key="index"
          @click="onButtonClicked(filter)"
        >
          {{ filter.name }}
        </v-btn>
      </v-btn-toggle>
    </v-row>
    <v-divider class="my-3" />
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
      if (this.value !== filter.score) {
        this.$store.commit('addNumberFilter', filter);
      } else {
        this.$store.commit('removeNumberFilter', filter);
      }
    },
    onAllButtonClicked() {
      this.data.rankings.forEach((element) => {
        this.$store.commit('removeNumberFilter', element);
      });
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    ...mapGetters(['tags', 'tagCategory', 'mandatoryFilter', 'numberFilter']),
    value() {
      let newValueArray = null;
      const selfObj = this.numberFilter.filter(
        (item) => item.techname === this.data.techname // eslint-disable-line
      )[0];
      if (selfObj) {
        newValueArray = selfObj.score;
      } else {
        newValueArray = '-1';
      }
      return newValueArray;
    },
  },
};
</script>

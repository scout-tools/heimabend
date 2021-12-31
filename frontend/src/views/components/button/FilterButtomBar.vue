<template>
  <v-container class="py-0">
    <v-row align="center" justify="center" class="ma-0 pa-0">
      <v-col cols="1">
        <v-icon large :color="data.color" >
          {{ data.icon }}
        </v-icon>
      </v-col>
      <v-col cols="3" class="ma-0 pa-0">
        <p class="text-left title ma-3" :color="data.color">{{ data.name }}</p>
      </v-col>
    </v-row>
    <v-row align="center">
      <v-btn-toggle :value="value" borderless tile group multiple>
        <v-btn @click="onAllButtonClicked" value="-1"> Alle </v-btn>
        <v-btn
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
      this.$store.commit('addNumberFilter', filter);
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
      let newValueArray = [];
      const selfObj = this.numberFilter.filter(
        (item) => item.techname === this.data.techname // eslint-disable-line
      );
      if (selfObj.length) {
        selfObj.forEach((item) => newValueArray.push(item.score)); // eslint-disable-line
      } else {
        newValueArray = ['-1'];
      }
      return newValueArray;
    },
  },
};
</script>

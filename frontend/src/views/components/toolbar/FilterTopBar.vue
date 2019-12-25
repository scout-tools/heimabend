<template>
  <v-toolbar
    dense
    fixed
  >
    <template>
      <v-spacer v-if="$vuetify.breakpoint.mdAndUp"></v-spacer>

      <div v-if="$vuetify.breakpoint.mdAndUp" class="mx-4"></div>
        <v-btn-toggle
          v-model="toggle_exclusive"
          multiple
          group
          dense
        >
        <v-btn
          @click="onIsPossibleInside()"
          text
        >
          <v-icon color="darkgrey darken-2">
            mdi-home
          </v-icon>
          <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
            Drinnen
          </span>
        </v-btn>

        <v-btn
          @click="onIsPossibleOutside()"
          text
        >
          <v-icon color="green darken-2">
            mdi-nature-people
          </v-icon>
          <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
            Draußen
          </span>
        </v-btn>

        <v-btn
          @click="onWithoutPreperation()"
          text
        >
          <v-icon color="black">
            mdi-clipboard-list-outline
          </v-icon>
          <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
            Ohne Vorbereitung
          </span>
        </v-btn>

        <v-btn
          @click="onWithoutCosts()"
          text
        >
          <v-icon color="orange darken-2">
            mdi-currency-eur
          </v-icon>
            <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
              Ohne Kosten
            </span>
        </v-btn>
      </v-btn-toggle>
      <v-divider v-if="$vuetify.breakpoint.mdAndUp" class="mx-2" vertical/>

        <v-btn-toggle
          v-model="levelFilter"
          @change="onChangeLevelFilter"
          multiple
          mandatory
          group
          dense
        >
          <v-btn>
            <v-img
              v-if="getOrange"
              :src="require('@/assets/knot_orange.png')"
              max-width="28"
            />
            <v-img
              v-if="!getOrange"
              :src="require('../../../assets/knot_grey.png')"
              max-width="28"
            />
            <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
              Anfänger
            </span>
          </v-btn>
          <v-btn>
            <v-img
              v-if="getBlue"
              :src="require('../../../assets/knot_blue.png')"
              max-width="28"
            ></v-img>
            <v-img
              v-if="!getBlue"
              :src="require('../../../assets/knot_grey.png')"
              max-width="28"
            ></v-img>
            <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
              Erfahren
            </span>
          </v-btn>
          <v-btn>
            <v-img
              v-if="getRed"
              :src="require('../../../assets/knot_red.png')"
              max-width="28"
            ></v-img>
            <v-img
              v-if="!getRed"
              :src="require('../../../assets/knot_grey.png')"
              max-width="28"
            ></v-img>
          <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
            Experten
          </span>
          </v-btn>
        </v-btn-toggle>

      <v-divider v-if="$vuetify.breakpoint.mdAndUp" class="mx-2" vertical/>
      <Sorter v-if="$vuetify.breakpoint.mdAndUp"/>
    </template>
  </v-toolbar>
</template>

<script>
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    Sorter,
  },
  props: {
    levelFilter: Array,
    tags: Array,
  },
  methods: {
    onChangeLevelFilter() {
      this.$emit('onLevelFilterChanged', this.levelFilter);
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
    },
    onIsPossibleInside() {
      this.$store.commit('tooglePossibleInside');
    },
    onIsPossibleOutside() {
      this.$store.commit('tooglePossibleOutside');
    },
    onWithoutPreperation() {
      this.$store.commit('toogleWithoutPreperation');
    },
    onWithoutCosts() {
      this.$store.commit('toogleWithoutCosts');
    },
  },
  computed: {
    getOrange() {
      if (this.levelFilter) {
        return this.levelFilter.includes(0);
      }
      return false;
    },
    getBlue() {
      if (this.levelFilter) {
        return this.levelFilter.includes(1);
      }
      return false;
    },
    getRed() {
      if (this.levelFilter) {
        return this.levelFilter.includes(2);
      }
      return false;
    },
    isPossibleInside: {
      get() {
        return this.$store.getters.isPossibleInside;
      },
      set() {
        return false;
      },
    },
    isPossibleOutside: {
      get() {
        return this.$store.getters.isPossibleOutside;
      },
      set() {
        return false;
      },
    },
    toggle_exclusive: {
      get() {
        const output = [];
        if (this.isPossibleInside) {
          output.push(0);
        }
        if (this.isPossibleOutside) {
          output.push(1);
        }
        return output;
      },
      set() {
        return false;
      },
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
.v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
</style>

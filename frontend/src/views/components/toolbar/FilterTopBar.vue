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
          <!-- Drinnen -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onIsPossibleInside()"
                v-on="on"
                text
                :class="isPossibleInsideButtonActive"
              >
                <v-icon color="darkgrey darken-2">
                  mdi-home
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Drinnen
                </span>
              </v-btn>
            </template>
            <span>
              Ist für Drinnen geeignet
            </span>
          </v-tooltip>

          <!-- Draußen -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onIsPossibleOutside()"
                v-on="on"
                text
                :class="isPossibleOutsideButtonActive"
              >
                <v-icon
                  :color="isPossibleOutside ? 'green darken-2' : 'darkgrey'"
                >
                  mdi-nature-people
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Draußen
                </span>
              </v-btn>
            </template>
            <span>
              Ist für Drau0en geeignet
            </span>
          </v-tooltip>

          <!-- Ohne Vorbereitung -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onWithoutPreperation()"
                v-on="on"
                text
                :class="isWithoutPreperationButtonActive"
              >
                <v-icon
                  :color="withoutPreperation ? 'black' : 'darkgrey'"
                >
                  mdi-card-bulleted-off-outline
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Ohne Vorbereitung
                </span>
              </v-btn>
            </template>
            <span>
              Ist ohne weitere Vorbereitung durchführbar
            </span>
          </v-tooltip>

          <!-- Ohne Kosten -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onWithoutCosts()"
                v-model="withoutCosts"
                v-on="on"
                text
                :class="isWithoutCostsButtonActive"
              >
                <v-icon
                :color="withoutCosts ? 'orange darken-2' : 'darkgrey'"
                >
                  mdi-currency-usd-off
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Ohne Kosten
                </span>
              </v-btn>
            </template>
            <span>
              Ohne Kosten durchführbar
            </span>
          </v-tooltip>
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
          <!-- orange -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
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
                <span
                  v-if="$vuetify.breakpoint.mdAndUp"
                  class="mx-1"
                >
                  Anfänger
                </span>
              </v-btn>
            </template>
            <span>
              Dieser Heimabend ist für Anfänger geeignet
            </span>
          </v-tooltip>

          <!-- blue -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
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
            </template>
            <span>
              Dieser Heimabend ist für erfahre Sipplinge geeignet
            </span>
          </v-tooltip>

          <!-- red -->
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
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
            </template>
            <span>
              Dieser Heimabend ist für Experten geeignet
            </span>
          </v-tooltip>
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
    tags: Array,
  },
  data() {
    return {
      levelFilter: [0, 1, 2],
    };
  },
  methods: {
    onChangeLevelFilter() {
      this.$store.commit('setLevelFilter', this.levelFilter);
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
    withoutPreperation: {
      get() {
        return this.$store.getters.withoutPreperation;
      },
      set() {
        return false;
      },
    },
    withoutCosts: {
      get() {
        return this.$store.getters.withoutCosts;
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
    isPossibleInsideButtonActive() {
      if (!this.isPossibleInside) {
        return 'btn-disabled';
      }
      return '';
    },
    isPossibleOutsideButtonActive() {
      if (!this.isPossibleOutside) {
        return 'btn-disabled';
      }
      return '';
    },
    isWithoutPreperationButtonActive() {
      if (!this.withoutPreperation) {
        return 'btn-disabled';
      }
      return '';
    },
    isWithoutCostsButtonActive() {
      if (!this.withoutCosts) {
        return 'btn-disabled';
      }
      return '';
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

.btn-disabled  {
  color: gray !important;
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
  opacity: 0.3;
}
</style>

<template>
  <v-toolbar
    class="top-toolbar"
    dense
    fixed
    :extension-height="extensionHeightNumber"
    :extended="isExtended && isMobil">
  <v-spacer/>
    <template>
      <v-spacer v-if="$vuetify.breakpoint.mdAndUp"></v-spacer>
        <v-btn-toggle
          v-model="toggle_exclusive"
          multiple
          group
          dense
        >
          <v-tooltip
            v-if="isMobil"
            nudge-left="80"
            bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onExpandClick()"
                dense
                class="pa-0"
                v-on="on"
                text
              >
                <v-icon>
                  mdi-tune
                </v-icon>
              </v-btn>
            </template>
            <span>
              Mehr Filter
            </span>
          </v-tooltip>
        </v-btn-toggle>
        <v-btn-toggle
          v-model="toggle_exclusive"
          multiple
          group
          dense
        >

          <v-tooltip
            bottom
            nudge-left="80"
            >
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onIsPossibleDigital()"
                v-on="on"
                text
                :class="isPossibleDigitalButtonActive"
              >
                <v-icon
                  :color="isPossibleDigital ? 'red darken-2' : 'grey'"
                >
                  mdi-robot
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Digital
                </span>
              </v-btn>
            </template>
            <span>
              Zeigt Heimabende an die mit deiner Sippe digital durchgeführt werden können.
            </span>
          </v-tooltip>


          <!-- Drinnen -->
          <v-tooltip
            nudge-left="80"
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onIsPossibleAlone()"
                v-on="on"
                text
                :class="isPossibleAloneButtonActive"
              >
                <v-icon
                  :color="isPossibleAlone ? 'black' : 'grey'"
                >
                  mdi-account-cowboy-hat
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Alleine
                </span>
              </v-btn>
            </template>
            <span>
              Zeigt Heimabende an die alleine durchführbar sind
            </span>
          </v-tooltip>

          <!-- Draußen -->


          <!-- Ohne Vorbereitung -->
          <v-tooltip
            nudge-left="80"
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onWithoutPreperation()"
                v-on="on"
                text
                tile
                dense
                :class="isWithoutPreperationButtonActive"
              >
                <v-icon
                  :color="withoutPreperation ? 'black' : 'grey'"
                >
                  mdi-card-bulleted-off-outline
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  Ohne Vorbe.
                </span>
              </v-btn>
            </template>
            <span>
              Zeigt nur Heimabende an die keine Vorbereitung benötigen
            </span>
          </v-tooltip>

          <!-- Ohne Kosten -->
          <v-tooltip
            nudge-left="80"
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn
                @click="onWithoutCosts()"
                v-on="on"
                text
                tile
                dense
                :class="isWithoutCostsButtonActive"
              >
                <v-icon
                :color="withoutCosts ? 'red darken-2' : 'grey'"
                >
                  mdi-currency-usd-off
                </v-icon>
                <span v-if="$vuetify.breakpoint.mdAndUp" class="mx-1">
                  0 €
                </span>
              </v-btn>
            </template>
            <span>
              Zeigt Heimabende an für die keine Kosten entstehen.
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
          <v-tooltip
            bottom
            nudge-left="80"
          >
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
                <v-img
                  :src="require('@/assets/wolfskopf.png')"
                  max-width="28"
                />
              </v-btn>
            </template>
            <span>
              Dieser Heimabend ist für Wölflinge geeignet
            </span>
          </v-tooltip>

          <!-- blue -->
          <v-tooltip
            bottom
            nudge-left="80"
            >
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
                <v-img
                  :src="require('../../../assets/knot_blue.png')"
                  max-width="28"
                ></v-img>
              </v-btn>
            </template>
            <span>
              Dieser Heimabend ist für Sipplinge geeignet
            </span>
          </v-tooltip>

          <!-- red -->
          <v-tooltip
            nudge-left="80"
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
              >
                <v-img
                  :src="require('../../../assets/knot_red.png')"
                  max-width="28"
                ></v-img>
              </v-btn>
            </template>
            <span>
              Dieser Heimabend ist für Rover geeignet
            </span>
          </v-tooltip>
        </v-btn-toggle>
        <div class="mr-12"></div>
      <!-- <v-divider v-if="$vuetify.breakpoint.mdAndUp" class="mx-2" vertical/>
      <Sorter
        v-if="$vuetify.breakpoint.mdAndUp"
        style="max-width: 250px"
      /> -->

    </template>
  <template
        #extension
        v-if="isExtended && isMobil"
      >
    <v-container class="pa-0" style="margin: 0px; width: 100%">

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
              small
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
  <v-spacer/>
  </v-toolbar>
</template>

<script>
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    // Sorter,
  },
  data() {
    return {
      levelFilter: [0, 1, 2],
      isExtended: false,
      filterTags: [],
    };
  },
  methods: {
    onExpandClick() {
      this.isExtended = !this.isExtended;
    },
    onChangeLevelFilter() {
      this.$store.commit('setLevelFilter', this.levelFilter);
    },
    onIsPossibleInside() {
      this.$store.commit('tooglePossibleInside');
    },
    onIsPossibleOutside() {
      this.$store.commit('tooglePossibleOutside');
    },
    onIsPossibleDigital() {
      this.$store.commit('tooglePossibleDigital');
    },
    onIsPossibleAlone() {
      this.$store.commit('tooglePossibleAlone');
    },
    onWithoutPreperation() {
      this.$store.commit('toogleWithoutPreperation');
    },
    onWithoutCosts() {
      this.$store.commit('toogleWithoutCosts');
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
    onClickTags() {
      this.$router.push({ name: 'tags' });
    },
  },
  computed: {
    extensionHeightNumber() {
      return this.isMobil ? '350px' : '50px';
    },
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
    isPossibleInside() {
      return this.$store.getters.isPossibleInside;
    },
    isPossibleOutside() {
      return this.$store.getters.isPossibleOutside;
    },
    isPossibleDigital() {
      return this.$store.getters.isPossibleDigital;
    },
    isPossibleAlone() {
      return this.$store.getters.isPossibleAlone;
    },
    withoutPreperation() {
      return this.$store.getters.withoutPreperation;
    },
    withoutCosts() {
      return this.$store.getters.withoutCosts;
    },
    toggle_exclusive: {
      get() {
        const output = [];
        if (this.isPossibleDigital) {
          output.push(0);
        }
        if (this.isPossibleAlone) {
          output.push(1);
        }
        if (this.withoutPreperation) {
          output.push(2);
        }
        if (this.withoutCosts) {
          output.push(3);
        }
        return output;
      },
      set() {
        return false;
      },
    },
    // isPossibleInsideButtonActive() {
    //   if (!this.isPossibleInside) {
    //     return 'btn-disabled';
    //   }
    //   return '';
    // },
    // isPossibleOutsideButtonActive() {
    //   if (!this.isPossibleOutside) {
    //     return 'btn-disabled';
    //   }
    //   return '';
    // },
    isPossibleDigitalButtonActive() {
      if (!this.isPossibleDigital) {
        return 'btn-disabled';
      }
      return '';
    },
    isPossibleAloneButtonActive() {
      if (!this.isPossibleAlone) {
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
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isJustActive: {
      get() {
        return this.$store.getters.justActive;
      },
      set() {
        return false;
      },
    },
    tags() {
      return this.$store.getters.tags;
    },
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(40, 158, 40)
}
.v-btn--active:before {
    opacity: 0.4;
    color: rgb(40, 158, 40)
}

.v-btn {
  padding-left: 6px !important;
  padding-right: 6px !important;
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
    opacity: 0.3;
}
.top-toolbar {
  /* margin-right: 240px; */
}
span {
  font-size: 12px !important;
}
</style>

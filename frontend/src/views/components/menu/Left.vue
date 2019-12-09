<template>
<div>
    <v-navigation-drawer
      v-model="isDrawer"
      app
      clipped
      width="300"
      color="accent"
    >
      <v-list
        dense
        class="accent"
      >
      <v-toolbar v-if="isAuthenticated" dense class="lightPrimary mx-4 mb-3">
        <v-spacer/>
          <v-btn icon>
            <v-icon>mdi-account-group-outline</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-tag-text-outline</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-earth</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-message-text-outline</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-archive-outline</v-icon>
          </v-btn>
        <v-spacer/>
        </v-toolbar>
        <template>
          <v-row align="center">
            <v-card
              width="270"
              class="mx-auto"
              shaped
            >
              <v-list-item class="lightPrimary pa-0 ma-0">
                <v-list-item-content>
                  <v-list-item-title>Filter</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-container>
                <v-row class="px-2 pb-2">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.isPossibleInside"
                    label="Nur im Haus"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="darkgrey">
                      mdi-home
                    </v-icon>
                  </v-col>
                </v-row>
                <v-divider/>
                <v-row class="px-2 pb-2">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.isPossibleOutside"
                    label="Nur Draußen"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col class="pa-0 ma-0" align-self="center">
                    <v-icon cols="2" color="green">
                      mdi-nature-people
                    </v-icon>
                  </v-col>
                </v-row>
                <v-divider/>
                <v-row class="px-2 pb-2">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.withoutPreperation"
                    label="Nur ohne Vorbereitung"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="black">
                      mdi-clipboard-list-outline
                    </v-icon>
                  </v-col>
                </v-row>
                <v-divider/>
                <v-row class="px-2 pb-2">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.withoutCosts"
                    label="Nur ohne Kosten"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="orange">
                      mdi-currency-eur
                    </v-icon>
                  </v-col>
                </v-row>
                <v-divider v-if="isAuthenticated"/>
                <v-row class="px-2 pb-2" v-if="isAuthenticated">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.justActive"
                    label="Nur Veröffentlicht"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="red">
                      mdi-eye-off-outline
                    </v-icon>
                  </v-col>
                </v-row>
                </v-container>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <v-row>
            <v-card
              width="270"
              class="mx-auto"
              shaped
            >
              <v-list-item class="lightPrimary pa-0 ma-0">
                <v-list-item-content>
                  <v-list-item-title>StufenA</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
      <v-row
        align="center"
        justify="center"
        class="my-5"
      >
        <v-btn-toggle
          v-model="levelFilter"
          @change="onChangeLevelFilter"
          multiple
          shaped
          mandatory
        >
          <v-btn>
            <v-img
              v-if="getOrange"
              class="mx-1"
              :src="require('../../../assets/knot_orange.png')"
              max-width="40"
            />
            <v-img
              v-if="!getOrange"
              class="mx-1"
              :src="require('../../../assets/knot_grey.png')"
              max-width="40"
            ></v-img>
          </v-btn>
          <v-btn>
            <v-img
              v-if="getBlue"
              class="mx-1"
              :src="require('../../../assets/knot_blue.png')"
              max-width="40"
            ></v-img>
            <v-img
              v-if="!getBlue"
              class="mx-1"
              :src="require('../../../assets/knot_grey.png')"
              max-width="40"
            ></v-img>
          </v-btn>
          <v-btn>
            <v-img
              v-if="getRed"
              class="mx-1"
              :src="require('../../../assets/knot_red.png')"
              max-width="40"
            ></v-img>
            <v-img
              v-if="!getRed"
              class="mx-1"
              :src="require('../../../assets/knot_grey.png')"
              max-width="40"
            ></v-img>
          </v-btn>
        </v-btn-toggle>
      </v-row>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <v-row>
            <v-card
              width="270"
              class="mx-auto"
              shaped
            >
              <v-list-item class="lightPrimary">
                <v-list-item-content>
                  <v-list-item-title>
                    Themen-Auswahl
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-row class="px-2">
                  <v-chip-group
                    multiple
                    column
                    v-model="filterTags"
                    @change="onChange()"
                  >
                    <v-chip
                      filter
                      small
                      v-for="(tag, index) in tags"
                      :key="index"
                      :color="tag.color">
                      {{ tag.name }}
                    </v-chip>
                  </v-chip-group>
                </v-row>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <!-- <v-row>
            <v-card
              width="200"
              class="mx-auto"
              shaped
            >
              <v-list-item class="secondary">
                <v-list-item-content>
                  <v-list-item-title>Likes</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-card-text mx-5>
                  <v-col cols="12">
                    Minimale Anzahl von Likes
                    <v-slider
                      prepend-icon="mdi-thumb-up"
                      icon-color="secondary"
                      thumb-label
                      dense
                      max="20"
                    ></v-slider>
                  </v-col>
                </v-card-text>
              </v-list-item>
            </v-card>
          </v-row> -->
          <!-- <v-spacer dark class="my-6"/> -->
        </template>
      </v-list>

      <v-list dense bottom>
        <v-list-item link bottom>
          <v-list-item-icon>
            <v-icon>mdi-help-circle-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content @click="onClickAboutProjectItem()">
            <v-list-item-title>Über das Projekt</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-information-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content @click="onClickImpressumItem()">
            <v-list-item-title>Impressum/Datenschutz</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</div>
</template>

<script>
export default {
  props: {
    filterStatus: Object,
    levelFilter: Array,
    tags: Array,
  },
  data: () => ({
    filterTags: [],
    mini: true,
  }),
  methods: {
    onChange() {
      this.$emit('onTagFilterChanged', this.filterTags);
    },
    onChangeLevelFilter() {
      this.$emit('onLevelFilterChanged', this.levelFilter);
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
    },
    onClickImpressumItem() {
      this.$emit('openImpressum');
    },
    onClickAboutProjectItem() {
      this.$emit('openAboutProject');
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
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isDrawer: {
      get() {
        return this.$store.getters.isDrawer;
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
</style>

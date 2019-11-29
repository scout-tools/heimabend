<template>
<div>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="300"
      color="grey lighten-3"
      z-index="-10000"
    >
      <v-list
        dense
        class="grey lighten-3"
      >
        <template>
          <v-row align="center">
            <v-card
              width="270"
              class="mx-auto"
              shaped
            >
              <v-list-item class="blue lighten-4 pa-0 ma-0">
                <v-list-item-content>
                  <v-list-item-title small>Filter</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-container>
                <v-row class="px-2 pb-2">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="filterStatus.onlyInside"
                    label="Nur im Haus"
                    dense
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
                    v-model="filterStatus.onlyOutside"
                    label="Nur Draußen"
                    dense
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
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="red">
                      mdi-clock
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
                    hide-details
                  />
                  </v-col>
                  <v-col cols="2" class="pa-0 ma-0" align-self="center">
                    <v-icon color="orange">
                      mdi-currency-eur
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
              <v-list-item class="blue lighten-4">
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
              <v-list-item class="blue lighten-4">
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
                      icon-color="blue lighten-2"
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
    </v-navigation-drawer>
</div>
</template>

<script>
export default {
  props: {
    drawer: Boolean,
    filterStatus: Object,
    tags: Array,
  },
  data: () => ({
    filterTags: [],
  }),
  methods: {
    onChange() {
      this.$emit('onTagFilterChanged', this.filterTags);
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
    },
  },
};
</script>

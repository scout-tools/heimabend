<template>
  <v-app id="keep" >
    <v-app-bar
      app
      clipped-left
      color="#1a4b7e"
      dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"/>
      <span class="title ml-3 mr-5" v-if="!isMobil">
        Heimabend&nbsp;
        <span class="font-weight-light">
          Inspirator
        </span>
      </span>

      <v-text-field
        class="px-3"
        v-model="searchInput"
        outlined
        hide-details
        label="Suche"
        prepend-inner-icon="mdi-magnify"
        clearable
        :dense="isMobil"
      />
      <v-btn
        v-if="!isMobil"
        disabled
        icon
        fab
        large
        @click="onNewClick()"
      >
        <v-icon color="green">mdi-pencil-plus</v-icon>
      </v-btn>
      <v-spacer />
      <img class="mr-2" :src="require('../assets/logo.gif')" height="50"/>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="300"
      color="grey lighten-3"
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
                    v-model="onlyInside"
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
                    v-model="onlyOutside"
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
                    v-model="withoutPreperation"
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
                    v-model="withoutCosts"
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

    <v-content id="lateral">
      <div class="row mx-2" justify="center">
        <div class="col-sm-12">
          <v-card max-width="800"
            shaped
            class="mx-auto ma-5"
            color="lightgrey"
            v-for="(item, index) in getItems" :key="index">
              <v-list-item class="blue lighten-4 pl-6 pr-0">
                <v-list-item-content>
                  <v-list-item-title :class="titleClass">
                    {{ item.title }}
                  </v-list-item-title>
                </v-list-item-content>
                <v-divider class="mx-2" vertical></v-divider>
                <v-btn class="ma-1 ml-0" text icon color="gray lighten-2"
                  @click="onUpdateClick(item)">
                  <v-icon>mdi-eye</v-icon>
                </v-btn>
              </v-list-item>
            <v-divider/>
            <v-card-text big class="text--primary">
              {{ item.shortDescription}}
            </v-card-text>
            <v-card-text>
              {{ `Material: ${item.material}` }}
            </v-card-text>
            <v-container>
              <v-chip
                class="ma-2"
                :color="getTagById(tag).color"
                v-for="(tag, index2) in item.tags" :key="index2">
                  {{ getTagById(tag).name }}
              </v-chip>
            </v-container>
            <v-divider/>
            <v-card-actions class="grey lighten-4">
              <div class="caption mr-1">
                {{ item.createdAt}}
              </div>
              <v-divider :class="verticalMargin" vertical v-if="item.outside"/>
                <v-tooltip open-on-hover bottom v-if="item.outside">
                  <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on">
                      <v-icon color="green" v-if="item.outside">
                        mdi-nature-people
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>Für Draußen geeignet</span>
                </v-tooltip>
              <v-divider :class="verticalMargin" vertical v-if="item.inside"/>
                <v-tooltip open-on-hover bottom v-if="item.inside">
                  <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on">
                      <v-icon v-if="item.inside">
                        mdi-home
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>Für das Haus geeignet</span>
                </v-tooltip>
              <v-divider :class="verticalMargin" vertical/>
                <v-tooltip open-on-hover bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="lightgrey"
                      v-on="on">
                      <v-rating
                        v-model="item.costsRating"
                        emptyIcon="mdi-currency-eur"
                        fullIcon="mdi-currency-eur"
                        color="orange"
                        background-color="grey"
                        dense
                        length="3"
                        :size="ratingSize"
                        readonly
                      />
                    </v-btn>
                  </template>
                  <span>Kosten</span>
                </v-tooltip>
              <v-divider :class="verticalMargin" vertical/>
                <v-tooltip open-on-hover bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="lightgrey"
                      v-on="on"
                    >
                      <v-rating
                        v-model="item.prepairationRating"
                        emptyIcon="mdi-clock"
                        fullIcon="mdi-clock"
                        color="red"
                        background-color="grey"
                        dense
                        length="3"
                        :size="ratingSize"
                        readonly
                      />
                    </v-btn>
                  </template>
                  <span>Vorbereitungszeit</span>
                </v-tooltip>
              <v-divider class="mx-2" vertical/>
              <v-spacer/>
            <!-- <v-divider vertical></v-divider>
            <div>
              <v-btn class="ma-2" text icon color="green lighten-2">
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>
            </div> -->
            </v-card-actions>
          </v-card>
        </div>
      </div>
    </v-content>
  <v-footer color="#1a4b7e" dark>
    <v-spacer></v-spacer>
    <div>&copy; </div>
      <span class="title ml-3 mr-5">
        {{ new Date().getFullYear() }}
      </span>
    <v-spacer/>
    </v-footer>
    <CreateDialog ref="createGroupClassModal" v-on:dialogClose="onDialogClose" :tags="tags"/>
  </v-app>
</template>

<script>
import CreateDialog from './components/Dialogs/CreateDialog.vue';

export default {
  components: {
    CreateDialog,
  },
  props: {
    source: String,
  },
  mounted() {
    this.isMobil = this.$vuetify.breakpoint.smAndDown;
  },
  computed: {
    getItems() {
      return this.items
        .filter(item => item.shortDescription.includes(this.searchInput)
          || item.title.includes(this.searchInput))
        .filter(item => this.filterTags.filter(element => item.tags.includes(element)).length
        || !this.filterTags.length)
        .filter(item => !this.onlyInside || item.inside === this.onlyInside)
        .filter(item => !this.onlyOutside || item.outside === this.onlyOutside)
        .filter(item => !this.withoutPreperation || item.prepairationRating === 1)
        .filter(item => !this.withoutCosts || item.costsRating === 1);
    },
    titleClass() {
      return !this.isMobil ? 'headline' : 'subtitle-1';
    },
    ratingSize() {
      return !this.isMobil ? 20 : 12;
    },
    verticalMargin() {
      return !this.isMobil ? 'mx-2' : 'mx-0';
    },
  },
  methods: {
    onNewClick() {
      this.$refs.createGroupClassModal.show();
    },
    onUpdateClick(item) {
      this.$refs.createGroupClassModal.show(item);
    },
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
    },
    onDialogClose() {
      // reload
    },
  },
  data: () => ({
    filterTags: [],
    drawer: null,
    onlyInside: false,
    onlyOutside: false,
    withoutPreperation: false,
    withoutCosts: false,
    searchInput: '',
    fab: false,
    hidden: false,
    colorFab: 'green',
    iconFab: 'mdi-plus',
    isMobil: false,
    tags: [
      {
        id: 0,
        name: 'Schnitzen',
        color: '#C0FF97',
      },
      {
        id: 1,
        name: 'Backen',
        color: '#FFBBBB',
      },
      {
        id: 2,
        name: 'Unsere Erde',
        color: '#BBEBFF',
      },
      {
        id: 3,
        name: 'D. Pfadfindergesch.',
        color: '#D7D1F8',
      },
      {
        id: 4,
        name: 'Int. Pfadfindergesch.',
        color: '#A3FEBA',
      },
      {
        id: 5,
        name: 'Unser Bund',
        color: '#FFFFB5',
      },
      {
        id: 6,
        name: '1. Hilfe',
        color: '#FFCFA4',
      },
      {
        id: 7,
        name: 'Feuer machen',
        color: '#F1F1B1',
      },
      {
        id: 8,
        name: 'Versprechen',
        color: '#DEB19E',
      },
      {
        id: 9,
        name: 'Karte Kompass',
        color: '#F4CAD6',
      },
      {
        id: 10,
        name: 'Kim-Spiele',
        color: '#C6C6FF',
      },
      {
        id: 11,
        name: 'Symbolik',
        color: '#DCEDEA',
      },
      {
        id: 12,
        name: 'Knoten',
        color: '#B4D1B6',
      },
      {
        id: 13,
        name: 'Küche',
        color: '#B5FFFC',
      },
      {
        id: 14,
        name: 'Lagerbauten',
        color: '#EDDFFB',
      },
      {
        id: 15,
        name: 'Schwarzzelte',
        color: '#DDCEFF',
      },
      {
        id: 16,
        name: 'Schätzen',
        color: '#FFBBF7',
      },
      {
        id: 16,
        name: 'Musisches',
        color: '#FFC895',
      },
      {
        id: 17,
        name: 'Packen',
        color: '#D7ACAC',
      },
      {
        id: 18,
        name: 'Haik',
        color: '#E994AB',
      },
      {
        id: 19,
        name: 'Lebensraum Baum',
        color: '#D5AAFF',
      },
    ],
    items: [
      {
        title: 'Brot backen auf dem Lagerfeuer',
        shortDescription: 'Sipplinge können viele unterschiedliche Arten ausprobiert und verglichen werden, wie man am besten auf dem Feuer Brot backen kann. z.b. Im Hordentopf.',
        tags: [13, 7, 1],
        material: 'Mehl, Wasser, Backpulver, Alufolie, Hordentopf, Steine, Stöcke, Brennholz, Streichhölzer',
        createdAt: '17.11.2019',
        costsRating: 2,
        outside: true,
        inside: false,
        prepairationRating: 2,
      },
      {
        title: 'Bündisch oder Scoutistisch?',
        shortDescription: 'Sipplinge können verschiedene Situationen aus dem Stammesleben erzählt werden und die Sipplinge sollen jeweils einschätzen ob die Sache Bündisch oder Scoutistisch ist.',
        tags: [11, 5, 3],
        material: '-',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: true,
        prepairationRating: 1,
      },
      {
        title: 'Trage bauen',
        shortDescription: 'Sipplinge können in den Wald gehen und dort nur aus Seil und gefundenen Holz eine Trage bauen, welche einen Sippling tragen kann.',
        tags: [14, 6],
        material: 'Seile, Dreckeckstücher',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: false,
        prepairationRating: 1,
      },
      {
        title: 'Rucksack packen',
        shortDescription: 'Sipplinge können ihren Rucksack mitbringen und über jedes Teil wird geredet.',
        material: 'kein Material',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: true,
        prepairationRating: 2,
        tags: [17, 18],
      },
      {
        title: 'Holzbrettchen erstellen',
        shortDescription: 'Sipplinge können blanke Holzbrettchen verschönern und mit Namen versehen. Dazu können Sie beliebige Werkzeuge wie Messer oder Lötkolben verwenden.',
        tags: [0],
        material: 'Holzbrettchen, Lötkolben',
        createdAt: '17.11.2019',
        costsRating: 3,
        outside: false,
        inside: true,
        prepairationRating: 2,
      },
      {
        title: 'Blattbuch erstellen',
        shortDescription: 'Die Sipplinge sollen ein Blattbuch erstellen. Dafür sollen Sie Blätter sammeln, trocknen und in ein Buch einkleben. Blüten und Rinde sollen ebenfalls hinzukommen, sowie eine Beschriftung.',
        tags: [19],
        material: 'leere A6-Hefte',
        createdAt: '17.11.2019',
        costsRating: 2,
        outside: true,
        inside: false,
        prepairationRating: 2,
      },
      {
        title: 'Wildpflanzen suchen',
        shortDescription: 'Die Sipplinge sollen die 5 der 10 häufigsten Wildpflanzen finden und ins Heim bringen.',
        tags: [19, 18, 13],
        material: '-',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: false,
        prepairationRating: 1,
      },
      {
        title: 'Kompass selber bauen',
        shortDescription: 'Die Sipplinge sollen einen Kompass selber bauen.',
        tags: [18, 9],
        material: 'Nadel, Magnet, Schale mit Wasser',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: true,
        prepairationRating: 2,
      },
      {
        title: '1. Hilfe Fallbeispiele',
        shortDescription: 'Die Sipplinge sollen typische Pfadfinder-Erste-Hilfe Fälle realistisch nachspielen.',
        tags: [6],
        material: 'Erste Hilfe Rucksack/Tasche',
        createdAt: '17.11.2019',
        costsRating: 2,
        outside: true,
        inside: true,
        prepairationRating: 2,
      },
      {
        title: 'Sonnenuhr bauen',
        shortDescription: 'Die Sipplinge sollen eine Sonnenuhr selber bauen.',
        tags: [2, 9],
        material: 'Stock, Kompass',
        createdAt: '17.11.2019',
        costsRating: 1,
        outside: true,
        inside: false,
        prepairationRating: 2,
      },
      {
        title: 'Gewürze erschmecken',
        shortDescription: 'Die Sipplinge sollen Gewürze erschmecken.',
        tags: [10],
        material: 'Gewürze',
        createdAt: '17.11.2019',
        costsRating: 3,
        outside: true,
        inside: true,
        prepairationRating: 3,
      },
    ],
  }),
};

</script>

<style scoped>
  #lateral .v-btn--example {
    bottom: 0;
    position: absolute;
    margin: 0 0 16px 16px;
  }

</style>

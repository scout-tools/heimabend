<template>
<div>
  <v-app id="keep">
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

    <MenuLeft
      ref="mainMenuLeft"
      :filterStatus="filterStatus"
      :tags="tags"
      @onTagFilterChanged="onTagFilterChanged"
      :drawer="drawer"
    />

    <v-content id="lateral">
      <div class="row mx-2" justify="center">
        <div class="col-sm-12">
          <HeimabendCard
            :items="getItems"
            :isMobil="isMobil"
            :tags="tags"
          />
          <v-btn
            class="ma-10"
            v-if="!getItems.length"
            @click="onResetClick()"
          >
            Alle Filter zurücksetzen
          </v-btn>
        </div>
      </div>
    </v-content>
  <v-footer
    color="#1a4b7e"
    dark
    fixed
  >
    <v-spacer></v-spacer>
    <div>&copy; </div>
      <span class="title ml-3 mr-5">
        {{ new Date().getFullYear() }}
      </span>
    <v-spacer/>
  </v-footer>
    <CreateDialog
      ref="createGroupClassModal"
      v-on:dialogClose="onDialogClose"
      :tags="tags"
    />
  </v-app>
</div>
</template>

<script>
import CreateDialog from './components/dialogs/CreateDialog.vue';
import HeimabendCard from './components/cards/Heimabend.vue';
import MenuLeft from './components/menu/Left.vue';

export default {
  components: {
    CreateDialog,
    HeimabendCard,
    MenuLeft,
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
        .filter(item => !this.filterStatus.onlyInside
          || item.inside === this.filterStatus.onlyInside)
        .filter(item => !this.filterStatus.onlyOutside
          || item.outside === this.filterStatus.onlyOutside)
        .filter(item => !this.filterStatus.withoutPreperation || item.prepairationRating === 1)
        .filter(item => !this.filterStatus.withoutCosts || item.costsRating === 1);
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
    onTagFilterChanged(data) {
      this.filterTags = data;
    },
    onResetClick() {
      this.filterStatus = {
        onlyInside: false,
        onlyOutside: false,
        withoutPreperation: false,
        withoutCosts: false,
      };
      this.$refs.mainMenuLeft.resetTags();
    },
  },
  data: () => ({
    filterTags: [],
    drawer: null,
    filterStatus: {
      onlyInside: false,
      onlyOutside: false,
      withoutPreperation: false,
      withoutCosts: false,
    },
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

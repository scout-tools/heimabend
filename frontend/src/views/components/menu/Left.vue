<template>
  <v-navigation-drawer
    v-bind:value="isDrawer"
    app
    clipped
  >
    <v-list>
      <v-list-item link bottom :to="{ name: 'inspirations' }">
        <v-list-item-icon>
          <v-icon color="yellow darken-1"> mdi-lightbulb-on </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Inspirationen </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item link bottom :to="{ name: 'ranking-overview' }">
        <v-list-item-icon>
          <v-icon color="blue"> mdi-calculator-variant-outline </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Fakten </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider />
      <v-list-item link bottom :to="{ name: 'faq' }">
        <v-list-item-icon>
          <v-icon color="green"> mdi-frequently-asked-questions </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Fragen / Antworten </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider />

      <v-list-item link bottom :to="{ name: 'scoring-start' }">
        <v-list-item-icon>
          <v-icon color="red"> mdi-food-apple </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Hilf Inspi</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider v-if="isAuthenticated" />

      <v-list-item v-if="isAuthenticated" link bottom :to="{ name: 'admin' }">
        <v-list-item-icon>
          <v-icon color="orange"> mdi-tools </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Sheldon Panel</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider />
      <v-spacer dark class="my-6" />
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  data: () => ({
    API_URL: process.env.VUE_APP_API,
  }),
  methods: {
    reloadServices() {
      this.getTags();
      this.getTagCategory();
    },
    getTags() {
      const path = `${
        this.API_URL
      }basic/tag/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTags', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
    getTagCategory() {
      const path = `${
        this.API_URL
      }basic/tag-category/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setTagCategory', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
  },
  computed: {
    ...mapGetters([
      'isAuthenticated',
      'searchInput',
      'tags',
      'isScoringMode',
      'headerString',
      'isSubPage',
      'isDrawer',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    watch: {
      searchText(value) {
        console.log(value);
        debugger;
      },
    },
  },
};
</script>

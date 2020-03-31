<template>
  <v-toolbar
    dense
    fixed
    color="accent"
  >
    <v-btn icon @click="onBackClick()">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>
    <v-toolbar-title>
      {{ currentRouteName }}
    </v-toolbar-title>
    <v-spacer></v-spacer>
  </v-toolbar>
</template>

<script>

export default {
  data() {
    return {
      levelFilter: [0, 1, 2],
    };
  },
  methods: {
    onBackClick() {
      if (this.$route.name === 'heimabendDetails') {
        this.$router.push({ name: 'overview-id', params: this.$route.params.id });
      } else {
        this.$router.push('overview');
      }
    },
  },

  computed: {
    currentRouteName() {
      const route = this.$route.name;
      if (route === 'aboutProject') {
        return 'Über das Projekt';
      }
      if (route === 'impressum') {
        return 'Impressum';
      }
      if (route === 'heimabendUpdate') {
        return 'Heimabend Bearbeiten';
      }
      if (route === 'heimabendCreate') {
        return 'Neuen Heimabend erstellen';
      }
      if (route === 'tags') {
        return 'Themen Übersicht';
      }
      if (route === 'message') {
        return 'Kontakt Formular';
      }
      if (route === 'messageOverview') {
        return 'Nachrichten';
      }
      if (route === 'heimabendDetails') {
        return 'Zurück zur Übersicht';
      }
      return route;
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(192, 214, 192)
}
.v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
  opacity: 0.3;
}
</style>

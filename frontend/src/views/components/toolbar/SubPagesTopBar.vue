<template>
  <v-toolbar
    dense
    fixed
  >
    <v-btn icon @click="onBackClick()">
      <v-icon>mdi-close</v-icon>
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
        this.$router.replace({ name: 'overview-id', params: this.$route.params.id });
      } else {
        this.$router.push({ path: '/' });
      }
    },
  },

  computed: {
    currentRouteName() {
      const route = this.$route.name;
      if (route === 'heimabendUpdate') {
        return 'Heimabend Bearbeiten';
      }
      if (route === 'heimabendCreate') {
        return 'Neue Heimabendidee erstellen';
      }
      if (route === 'message') {
        return 'Kontakt Formular';
      }
      return 'Zurück zur Übersicht';
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
    color: rgb(149, 201, 240)
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
  opacity: 0.3;
}
</style>

<template>
  <v-bottom-navigation app horizontal :value="value" color="inspiBlue" grow>
    <v-btn :to="{ name: 'overview' }">
      <h3>Liste</h3>

      <v-icon>mdi-format-list-bulleted-square</v-icon>
    </v-btn>

    <v-btn :to="{ name: 'inspirations' }">
      <h3>Inspirationen</h3>

      <v-icon>mdi-lightbulb-on-outline</v-icon>
    </v-btn>

    <v-btn @click="openBottomMenu">
      <h3>Sonstige</h3>

      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data: () => ({ value: 1 }),
  methods: {
    openBottomMenu() {
      this.$emit('openBottomMenu');
    },
  },
  computed: {
    ...mapGetters([
      'isAuthenticated',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
  },
};
</script>

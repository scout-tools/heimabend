<template>
  <v-bottom-navigation app horizontal :value="value" color="inspiBlue" grow>
    <v-btn :to="{ name: 'overview' }">
      <span>Liste</span>

      <v-icon>mdi-format-list-bulleted-square</v-icon>
    </v-btn>

    <v-btn :to="{ name: 'inspirations' }">
      <span>Inspirationen</span>

      <v-icon>mdi-lightbulb-on-outline</v-icon>
    </v-btn>

    <v-btn @click="openBottomMenu">
      <span>Sonstige</span>

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

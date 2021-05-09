<template>
  <div>
    <v-speed-dial
      id="options-fab"
      v-model="fab"
      bottom
      right
      direction="left"
      transition="slide-x-reverse-transition"
      fixed
    >
      <template v-slot:activator>
        <router-link :to="{ name: 'overview' }" class="no-underline">
          <v-btn color="green darken-1" dark fab>
            <v-icon v-if="fab">mdi-close</v-icon>
            <v-icon v-else>mdi-plus</v-icon>
          </v-btn>
        </router-link>
      </template>
      <v-tooltip top nudge-top="30">
        <template v-slot:activator="{ on }">
          <router-link :to="{ name: 'heimabendCreate' }" class="no-underline">
            <v-btn @click="onNewEventClick" fab dark color="blue" v-on="on">
              <v-icon>mdi-calendar-heart</v-icon>
            </v-btn>
          </router-link>
        </template>
        <span class="subtitle-1">
          Hiermit kannst du eine neue Heimabend-Idee hinzufügen.
        </span>
      </v-tooltip>
      <v-tooltip top nudge-top="30">
        <template v-slot:activator="{ on }">
          <router-link :to="{ name: 'message' }" class="no-underline">
            <v-btn @click="onNewMessageClick" fab dark color="orange" v-on="on">
              <v-icon>mdi-message-text</v-icon>
            </v-btn>
          </router-link>
        </template>
        <span class="subtitle-1">
          Hiermit kannst du uns eine Nachricht senden.
        </span>
      </v-tooltip>
    </v-speed-dial>

    <v-speed-dial
      v-if="isPageScrolled"
      id="fab-scroll-to-top"
      bottom
      right
      direction="top"
      transition="slide-y-reverse-transition"
      fixed
      class="main mb-16"
    >
      <template v-slot:activator>
        <v-btn color="secondary" fab @click="scrollToTop">
          <v-icon> mdi-chevron-up</v-icon>
        </v-btn>
      </template>
    </v-speed-dial>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data: () => ({
    fab: false,
  }),
  computed: {
    ...mapGetters(['isPageScrolled']),
  },
  methods: {
    onNewEventClick() {
      // eslint-disable-next-line no-undef
      _paq.push(['trackEvent', 'create', 'heimabendCreate']);
    },
    onNewMessageClick() {
      // eslint-disable-next-line no-undef
      _paq.push(['trackEvent', 'create', 'message']);
    },
    async scrollToTop() {
      await this.$vuetify.goTo(0);
      this.$store.commit('setPageScrolled', false);
    },
  },
};
</script>

<style>
/* This is for documentation purposes and will not be needed in your application */
#create .v-speed-dial {
  position: absolute;
}

#create .v-btn--floating {
  position: relative;
}

.main {
  z-index: 100000000000;
}

.no-underline {
  text-decoration: none !important;
}
</style>

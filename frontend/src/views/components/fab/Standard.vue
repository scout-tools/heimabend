<template>
    <v-speed-dial
      v-model="fab"
      bottom
      right
      direction="top"
      transition="slide-y-reverse-transition"
      fixed
      class="main"
    >
      <template v-slot:activator>
        <router-link
          :to="{ name: 'overview'}"
          class="no-underline"
        >
          <v-btn
            color="green darken-1"
            dark
            fab>
            <v-icon v-if="fab">mdi-close</v-icon>
            <v-icon v-else>mdi-plus</v-icon>
          </v-btn>
        </router-link>
      </template>
      <v-tooltip bottom nudge-left="80">
        <template v-slot:activator="{ on }">
          <router-link
            :to="{ name: 'heimabendCreate'}"
            class="no-underline"
          >
            <v-btn
              @click="onNewEventClick"
              fab
              dark
              color="blue"
              v-on="on"
            >
              <v-icon>mdi-calendar-heart</v-icon>
            </v-btn>
          </router-link>
        </template>
       <span class="subtitle-1">
          Hiermit kannst du eine neue Heimabend-Idee hinzufügen.
        </span>
      </v-tooltip>
      <v-tooltip bottom nudge-left="80">
        <template v-slot:activator="{ on }">
          <router-link
            :to="{ name: 'message'}"
            class="no-underline"
          >
            <v-btn
              @click="onNewMessageClick"
              fab
              dark
              color="orange"
              v-on="on"
            >
              <v-icon>mdi-message-text</v-icon>
            </v-btn>
          </router-link>
        </template>
        <span class="subtitle-1">
          Hiermit kannst du uns eine Nachricht senden.
        </span>
      </v-tooltip>
    </v-speed-dial>
</template>

<script>
export default {
  data: () => ({
    fab: false,
  }),
  methods: {
    onNewEventClick() {
      // eslint-disable-next-line no-undef
      _paq.push(['trackEvent', 'create', 'heimabendCreate']);
    },
    onNewMessageClick() {
      // eslint-disable-next-line no-undef
      _paq.push(['trackEvent', 'create', 'message']);
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

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
        <v-btn
          color="green darken-1"
          dark
          fab>
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-plus</v-icon>
        </v-btn>
      </template>
      <v-tooltip bottom nudge-left="80">
        <template v-slot:activator="{ on }">
          <v-btn
            @click="onNewEventClick"
            fab
            dark
            color="blue"
            v-on="on"
          >
            <v-icon>mdi-calendar-heart</v-icon>
          </v-btn>
        </template>
       <span class="subtitle-1">
          Hiermit kannst du einen neuen Heimabend anlegen
        </span>
      </v-tooltip>
      <v-tooltip bottom nudge-left="80">
        <template v-slot:activator="{ on }">
          <v-btn
            @click="onNewMessageClick"
            fab
            dark
            color="orange"
            v-on="on"
          >
            <v-icon>mdi-message-text</v-icon>
          </v-btn>
        </template>
        <span class="subtitle-1">
          Hiermit kannst du uns eine Nachricht schicken
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
      this.$router.push({ name: 'heimabendCreate' });
    },
    onNewMessageClick() {
      this.$router.push({ name: 'message' });
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
</style>

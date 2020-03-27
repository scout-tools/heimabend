<template>
    <v-speed-dial
      v-model="fab"
      bottom
      right
      direction="top"
      transition="slide-y-reverse-transition"
      fixed
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
      <v-btn
        @click="onNewEventClick"
        fab
        dark
        color="blue">
        <v-icon>mdi-calendar-heart</v-icon>
      </v-btn>
      <v-btn
        @click="onNewMessageClick"
        fab
        dark
        color="orange">
        <v-icon>mdi-message-text</v-icon>
      </v-btn>
    </v-speed-dial>
</template>

<script>
export default {
  data: () => ({
    fab: true,
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
</style>

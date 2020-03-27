<template>
  <v-dialog v-model="dialog" max-width="800px">
    <v-card >
      <v-card-title>
        <span class="headline">Nachricht</span>
      </v-card-title>
      <v-card-text>
        <p
          class="text-left subtitle-1"
          v-html="message"
        >
        </p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="cancel">Schließen</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    show(item) {
      this.dialog = true;
      this.message = item.messageBody;
    },
    cancel() {
      this.dialog = false;
    },
  },
};
</script>

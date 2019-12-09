<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-top-transition">
      <v-card >
      <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Impressum</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: [],

  data: () => ({
    dialog: false,
    data: [],
  }),

  methods: {
    show() {
      this.dialog = true;
    },
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
  },
};
</script>

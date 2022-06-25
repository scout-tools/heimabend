<template>
  <div>
    <v-row justify="center">
      <v-dialog v-model="dialog" max-width="400">
        <v-card>
          <v-card-title class="headline">{{ headerText }}</v-card-title>

          <v-card-text>
            {{ textPart }}
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="grey darken-1" text @click="cancel()">
              Abbrechen
            </v-btn>

            <v-btn color="red darken-1" text @click="onDeleteClick()">
              {{ buttonText }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
    <v-snackbar v-model="showError" color="error" y="top" :timeout="timeout">
      {{ 'Es ist ein  Fehler aufgetreten' }}
    </v-snackbar>
    <v-snackbar
      v-model="showSuccess"
      color="success"
      y="top"
      :timeout="timeout"
    >
      {{ 'Diese Idee wurde erfolgreich gelöscht' }}
    </v-snackbar>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    timeout: 3000,
    data: {
      id: null,
    },
  }),
  computed: {
    buttonText() {
      return this.data.isPublic ? 'Offline nehmen' : 'Online nehmen';
    },
    headerText() {
      return this.data.isPublic
        ? 'Heimabend unveröffentlichen'
        : 'Heimabend veröffentlichen';
    },
    textPart() {
      return `Willst du Idee "${this.data.title}" ${
        this.data.isPublic ? 'unveröffentlichen' : 'veröffentlichen'
      }?`;
    },
  },
  methods: {
    onDeleteClick() {
      axios
        .post(`${this.API_URL}event-publish/`, {
          setActive: !this.data.isPublic,
          event: this.data.id,
        })
        .then(() => {
          this.showSuccess = true;
          this.dialog = false;
          this.$emit('refresh');
        })
        .catch(() => {
          this.showError = true;
        });
    },
    show(item) {
      this.dialog = true;
      this.data = item;
    },

    cancel() {
      this.dialog = false;
    },
  },
};
</script>

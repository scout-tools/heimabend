<template>
<div>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Kategorie löschen</v-card-title>

        <v-card-text>
          Willst du echt diese Kategorie löschen?
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="grey darken-1"
            text
            @click="cancel()"
          >
            Abbrechen
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="onDeleteClick()"
          >
            Löschen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
      :timeout="timeout"
    >
      {{ 'Es ist ein  Fehler aufgetreten' }}
    </v-snackbar>
    <v-snackbar
      v-model="showSuccess"
      color="success"
      y='top'
      :timeout="timeout"
    >
      {{ 'Der Tag wurde erfolgreich gelöscht' }}
    </v-snackbar>
</div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['tags'],

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    responseObj: null,
    timeout: 3000,
    data: {
      id: null,
      name: null,
      description: null,
      color: null,
    },
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
  },

  methods: {
    onDeleteClick() {
      axios.delete(`${this.API_URL}basic/tag/${this.data.id}/`)
        .then(() => {
          this.dialog = false;
          this.$emit('dialogClose');
          this.$emit('refresh');
          this.showSuccess = true;
        })
        .catch(() => {
          this.showError = true;
        });
    },
    show(item) {
      this.dialog = true;
      if (item) {
        this.isCreate = false;
        this.isUpdate = true;
        this.data = item;
      } else {
        this.isCreate = true;
        this.isUpdate = false;
      }
    },

    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
  },
};
</script>

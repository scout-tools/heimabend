<template>
  <form ref="form">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="3">
          <v-autocomplete
            v-model="eventId"
            label="Heimabend der Woche*"
            item-value="id"
            :item-text="formatEventText"
            :items="eventList"
            :error-messages="eventIdErrors"
          ></v-autocomplete>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-date-picker
          v-model="releaseDate"
          :allowed-dates="allowedDates"
          class="mt-4"
          min="2021-06-21"
        ></v-date-picker>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="3">
          <v-text-field
            readonly
            label="Veröffentlichungs-Datum*"
            v-model="releaseDate"
            :error-messages="releaseDateErrors"
          >
          </v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="3">
          <v-textarea v-model="comment" label="Kommentar"> </v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-divider class="my-4" />
      </v-row>
      <v-row justify="end" class="mb-2">
        <v-btn class="mx-2" @click="onCancelClicked" tile>
          <v-icon left> mdi-cancel </v-icon>
          Abbrechen
        </v-btn>
        <v-btn class="mx-2" @click="onConfirmClicked" tile color="success">
          <v-icon left> mdi-content-save </v-icon>
          Speichern
        </v-btn>
      </v-row>
    </v-container>
    <v-snackbar v-model="snackbar">
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn color="indigo" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </form>
</template>

<script>
import axios from 'axios'; // eslint-disable-line

import { validationMixin } from 'vuelidate';
import { required } from 'vuelidate/lib/validators';

export default {
  mixins: [validationMixin],
  data() {
    return {
      loading: true,
      eventList: [],
      eventId: null,
      API_URL: process.env.VUE_APP_API,
      releaseDate: null,
      valid: false,
      snackbar: false,
      comment: null,
      text: '',
    };
  },
  validations: {
    releaseDate: {
      required,
    },
    eventId: {
      required,
    },
  },
  created() {
    this.getCallHighscoreService();
  },
  computed: {
    eventIdErrors() {
      const errors = [];
      if (!this.$v.eventId.$dirty) return errors;
      !this.$v.eventId.required && errors.push('Heimabend auswählen.'); // eslint-disable-line
      return errors;
    },
    releaseDateErrors() {
      const errors = [];
      if (!this.$v.releaseDate.$dirty) return errors;
      !this.$v.releaseDate.required && errors.push('Datum auswählen.'); // eslint-disable-line
      return errors;
    },
  },
  methods: {
    validate() {
      this.$v.$touch();
      this.valid = !this.$v.$error;
    },
    formatEventText(item) {
      return `${item.title} - ${item.createdBy} - ${
        !item.isPublic ? 'Nicht Fertig' : 'Fertig'
      }`;
    },
    allowedDates: val => new Date(val).getDay() === 1,
    getCallHighscoreService() {
      this.loading = true;
      const path = `${
        this.API_URL
      }basic/admin-event/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((response) => {
          this.eventList = response.data;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
    onConfirmClicked() {
      this.createMethod();
    },
    createMethod() {
      this.validate();
      if (!this.valid) {
        return;
      }
      axios
        .post(`${this.API_URL}basic/event-of-the-week/`, {
          eventId: this.eventId,
          event: this.eventId,
          event_id: this.eventId,
          releaseDate: this.releaseDate,
          comment: this.comment,
        })
        .then(() => {
          this.showSuccess = true;
          this.$router.go(-1);
        })
        .catch(() => {
          this.loading = false;
          this.text = 'Datum oder Heimabend bereits verwendet.';
          this.snackbar = true;
        });
    },
    onCancelClicked() {
      this.$router.go(-1);
    },
  },
};
</script>

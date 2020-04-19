<template>
  <v-container>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <div :class="divClass">
          Kontakt
        </div>
        <v-card :class="cardClass">
          <form>
            <v-text-field
              v-model="name"
              :error-messages="nameErrors"
              :counter="10"
              solo
              label="Dein Name"
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
            ></v-text-field>
            <v-text-field
              v-model="email"
              solo
              :error-messages="emailErrors"
              label="Deine E-Mail Adresse"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
            <v-select
              v-model="topic"
              :items="items"
              solo
              :error-messages="topicErrors"
              label="Art der Nachricht"
              required
              @change="$v.topic.$touch()"
              @blur="$v.topic.$touch()"
            ></v-select>
            <v-textarea
              v-model="messageBody"
              label="Nachricht"
              solo
              required
              :error-messages="messageBodyErrors"
              @change="$v.messageBody.$touch()"
              @blur="$v.messageBody.$touch()"
              hint="Hier keine Nachricht eintippen."></v-textarea>

            <v-btn class="mr-4" @click="submit">Absenden</v-btn>
          </form>
        </v-card>
      </v-flex>
    </v-row>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
    >
      {{ 'Fehler beim Sender der Nachricht' }}
    </v-snackbar>
    <v-snackbar
      v-model="showSuccess"
      color="success"
      y='top'
    >
      {{ 'Die Nachricht wurde erfolgreich an uns gesendet' }}
    </v-snackbar>
  </v-container>
</template>

<script>
import { validationMixin } from 'vuelidate';
import {
  required,
  minLength,
  maxLength,
  email,
} from 'vuelidate/lib/validators';
import axios from 'axios';

export default {
  mixins: [validationMixin],

  validations: {
    name: { required, minLength: minLength(3), maxLength: maxLength(20) },
    email: { email },
    topic: { required },
    messageBody: { required, minLength: minLength(10), maxLength: maxLength(5000) },
  },

  data: () => ({
    name: '',
    email: '',
    topic: null,
    messageBody: '',
    showError: false,
    API_URL: process.env.VUE_APP_API,
    showSuccess: false,
    items: [
      'Heimabend Idee',
      'Verbesserungsvorschlag',
      'Fehlermeldung',
      'Ich möchte mitmachen',
      'Kontakt',
      'Sonstiges',
    ],
    checkbox: false,
  }),

  computed: {
    cardClass() {
      if (!this.isMobil) {
        return 'ma-10 pa-10';
      }
      return 'ma-2 pa-2';
    },
    divClass() {
      if (!this.isMobil) {
        return 'display-3 ma-10';
      }
      return 'display-1 ma-2';
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.minLength && errors.push('Der Name ist zu kurz'); // eslint-disable-line
      !this.$v.name.maxLength && errors.push('Der Name ist zu lang'); // eslint-disable-line
      !this.$v.name.required && errors.push("Dein Name wird benötigt."); // eslint-disable-line
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Bitte prüfe die Adresse nochmal"); // eslint-disable-line
      return errors;
    },
    topicErrors() {
      const errors = [];
      if (!this.$v.topic.$dirty) return errors;
      !this.$v.topic.required && errors.push("Wir müssen wissen welcher Art dein Anliegen ist."); // eslint-disable-line
      return errors;
    },
    messageBodyErrors() {
      const errors = [];
      if (!this.$v.messageBody.$dirty) return errors;
      !this.$v.messageBody.minLength && errors.push('Nachricht ist zu kurz'); // eslint-disable-line
      !this.$v.messageBody.maxLength && errors.push('Nachricht ist zu lang'); // eslint-disable-line
      return errors;
    },
  },

  methods: {
    submit() {
      this.$v.$touch();

      axios
        .post(`${this.API_URL}basic/message/`, {
          name: this.name,
          email: this.email,
          topic: this.topic,
          messageBody: this.messageBody,
        })
        .then(() => {
          this.$router.push({ name: 'overview' });
          this.showSuccess = true;
        })
        .catch(() => {
          this.showError = true;
        });
    },
  },
};
</script>

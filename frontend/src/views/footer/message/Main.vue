<template>
  <v-container fluid>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <v-card max-width="500" class="mx-auto pa-3 ma-5">
          <v-row align="center" class="fill-height" justify="center">
            <v-col class="py-0" cols="8" align="center" justify="center">
              <v-card-title align="center" justify="center" class="headline">
                {{ headerText }}</v-card-title
              >
            </v-col>
            <v-col align-self="end" class="pa-0" cols="2">
              <v-img
                :src="require('@/assets/inspi/inspi_front_kopfhoerer.png')"
                max-width="100"
                class="mt-4"
              />
            </v-col>
          </v-row>
          <message-form v-model="data" />
          <v-btn class="mr-4" color="primary" @click="submit"> Absenden </v-btn>
        </v-card>
      </v-flex>
    </v-row>

    <v-snackbar
      v-model="showError"
      color="error"
      y="top"
      multi-line
      :timeout="timeout"
    >
      Fehler beim Speichern der Nachricht <br />
      <br />
      {{ this.responseObj }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="showError = false">
          X
        </v-btn>
      </template>
    </v-snackbar>

    <v-snackbar v-model="showSuccess" y="top">
      {{ 'Die Nachricht wurde erfolgreich an uns gesendet' }}
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from 'axios';
// eslint-disable-next-line
import MessageForm from '@/components/form/MessageForm.vue';

export default {
  components: { MessageForm },

  data: () => ({
    showError: false,
    API_URL: process.env.VUE_APP_API,
    showSuccess: false,
    valid: false,
    checkbox: false,
    data: {
      createdBy: 'Robert',
      createdByEmail: 'test@test.de',
      messageType: 6,
      messageBody: 'dadasdsadsadasdasdasddas',
    },
    responseObj: '',
    timeout: -1,
    headerText: 'Nachricht an mich',
  }),
  computed: {
  },
  methods: {
    submit() {
      this.saveMessage();
    },
    saveMessage() {
      axios
        .post(`${this.API_URL}basic/message/`, {
          createdBy: this.data.createdBy,
          createdByEmail: this.data.createdByEmail,
          topic: this.data.topic,
          messageBody: this.data.messageBody,
        })
        .then(() => {
          this.showSuccess = true;
        })
        .catch((error) => {
          this.responseObj = JSON.stringify(error.response.data);
          this.showError = true;
        });
    },
  },
  created() {
    this.$store.commit('setHeaderString', 'Nachricht an Inspi');
  },
};
</script>

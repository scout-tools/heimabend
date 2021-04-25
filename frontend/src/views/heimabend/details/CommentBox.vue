<template>
  <v-expansion-panels style="maxwidth: 700px">
    <v-expansion-panel>
      <v-expansion-panel-header align="center" justify="center">
        Kommentar oder Vorschlag schreiben
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <message-form v-model="data" />
        <v-btn class="mr-4" color="primary" @click="submit"> Absenden </v-btn>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import axios from 'axios';
import MessageForm from '@/views/footer/message/components/MessageForm.vue';

export default {
  components: {
    MessageForm,
  },
  data: () => ({
    showError: false,
    API_URL: process.env.VUE_APP_API,
    showSuccess: false,
    valid: false,
    checkbox: false,
    data: {},
    responseObj: '',
    timeout: -1,
    headerText: 'Nachricht an mich',
  }),

  methods: {
    submit() {
      this.saveMessage();
    },
    saveMessage() {
      axios
        .post(`${this.API_URL}basic/message/`, {
          createdBy: this.data.createdBy,
          createdByEmail: this.data.createdByEmail,
          messageType: this.data.messageType,
          messageBody: this.data.messageBody,
          event: this.eventId,
        })
        .then(() => {
          this.$router.push({ name: 'overview' });
          this.showSuccess = true;
        })
        .catch((error) => {
          this.responseObj = JSON.stringify(error.response.data);
          this.showError = true;
        });
    },
  },
  computed: {
    eventId() {
      return this.$route.params.id;
    },
  },
};
</script>

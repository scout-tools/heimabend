<template>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header color="#F6F6F6" align="center" justify="center">
        Kommentar oder Vorschlag schreiben
      </v-expansion-panel-header>
      <v-expansion-panel-content color="#F6F6F6">
        <message-form v-model="data"  color="#F6F6F6"/>
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
    getMaxWidth() {
      return '900';
    },
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

<style scoped>
.v-expansion-panel {
    max-width: 900px;
}
</style>

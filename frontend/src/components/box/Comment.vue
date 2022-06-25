<template>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header color="#F6F6F6" class="pa-1" align="center" justify="center">
        <v-container fluid>
          <v-row align="center" justify="center">
            <v-col cols="1">
              <v-icon large color="blue">mdi-chat-plus</v-icon>
            </v-col>
            <v-col cols="10">
              <p class="text-left title ma-3">{{ headerText }}</p>
            </v-col>
          </v-row>
        </v-container>
      </v-expansion-panel-header>
      <v-expansion-panel-content v-if="!messageSent" color="#F6F6F6">
        <message-form
          v-model="data"
          :allowedMessageTypes="allowedMessageTypes"
          :showType="showType"
          :eventIdParam="eventIdParam"
          ref="messageForm"
        />
        <v-btn class="mr-4" color="primary" @click="submit"> Absenden </v-btn>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import axios from 'axios';
// eslint-disable-next-line
import MessageForm from '@/components/form/MessageForm.vue';

export default {
  props: {
    showEmail: {
      type: Boolean,
      default: true,
    },
    showName: {
      type: Boolean,
      default: true,
    },
    showType: {
      type: Boolean,
      default: true,
    },
    allowedMessageTypes: {
      type: String,
      default: 'all',
    },
    headerText: {
      type: String,
      default: 'Eigene Frage schreiben',
    },
    eventIdParam: {
      type: Number,
      default: 0,
    },
  },
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
    messageSent: false,
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
          this.onSucessSend();
        })
        .catch((error) => {
          this.responseObj = JSON.stringify(error.response.data);
          this.showError = true;
        });
    },
    onSucessSend() {
      this.showSuccess = true;
      this.$refs.messageForm.resetForm();
      this.$emit('messageSent');
    },
  },
  computed: {
    eventId() {
      if (this.eventIdParam) {
        return this.eventIdParam;
      }
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

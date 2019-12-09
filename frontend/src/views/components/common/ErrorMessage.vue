<template>
  <v-snackbar
    v-model="showError"
    color="error"
    y='top'
  >
    {{ details }}
    <v-btn
      dark
      text
      @click="showError = false"
    >
      Schließen
    </v-btn>
  </v-snackbar>
</template>

<script>
import router from '@/router'; // eslint-disable-line


export default {
  props: {
    showError: {
      type: Boolean,
      default: false,
    },
    responseObj: {
      type: Error,
      default: {},
    },
  },

  data: () => ({
  }),

  methods: {
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    statusText() {
      if (this.responseObj && this.responseObj.response) {
        return this.responseObj.response.statusText;
      }
      return 'Fehler';
    },
    details() {
      if (this.responseObj && this.responseObj.response) {
        return this.responseObj.response.data.detail;
      }
      return 'Fehler';
    },
  },
};
</script>

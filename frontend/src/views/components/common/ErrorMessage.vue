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
  props: [
    'showError',
    'responseObj',
  ],

  data: () => ({
    showError: false,
  }),

  methods: {
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    statusText() {
      if (this.responseObj.response) {
        return this.responseObj.response.statusText;
      }
      return ':-(';
    },
    details() {
      if (this.responseObj.response) {
        return this.responseObj.response.data.detail;
      }
      return ':-(';
    },
  },
};
</script>

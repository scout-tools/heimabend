<template>
  <v-snackbar
    v-model="showSuccess"
    color="success"
    y='top'
  >
    {{ 'Juhu, es hat geklappt' }}
  </v-snackbar>
</template>

<script>
// import axios from 'axios';
import router from '@/router'; // eslint-disable-line
// import store from '@/store';


export default {
  props: {
    showSuccess: {
      type: Boolean,
      default: false,
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
    isShowSuccess: {
      get() {
        return this.showSuccess;
      },
      set() {
        return false;
      },
    },
  },
};
</script>

<template>
<v-container>
  <v-row justify="center">
    <v-dialog v-model="dialog" transition="dialog-top-transition"
    persistent max-width="600px">
      <v-card>
      <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>
            {{ getHeader }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text class="mt-5">
          <v-container v-if="!isAuthenticated">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Benutzer"
                  autofocus
                  v-model="data.username"
                  required>
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Password"
                  type="password"
                  v-model="data.password"
                  v-on:keyup="onPasswortTypInPasswordField"
                  required>
                </v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <v-container v-if="isAuthenticated">
            <v-btn
            large
            @click="onLogoutClick">
              Ausloggen
            </v-btn>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">Schließen</v-btn>
          <v-btn
            v-if="!isAuthenticated"
            color="primary"
            text
            @click="login">
              Login
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
<ErrorMessage
  :showError="showError"
  :responseObj="responseObj"
/>
<SuccessMessage
  :showSuccess="showSuccess"/>
</v-container>
</template>

<script>
import axios from 'axios';
import store from '@/store';

import ErrorMessage from '@/views/components/common/ErrorMessage.vue';
import SuccessMessage from '@/views/components/common/SuccessMessage.vue';


export default {
  props: [],

  components: {
    ErrorMessage,
    SuccessMessage,
  },

  data: () => ({
    dialog: false,
    showError: false,
    showSuccess: false,
    responseObj: {},
    API_URL: process.env.VUE_APP_API,
    data: {
      username: '',
      password: '',
    },
  }),

  methods: {
    show() {
      this.dialog = true;
    },
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
    onPasswortTypInPasswordField(event) { // eslint-disable-line
      if (event.code === 'Enter') {
        this.login();
      }
    },
    login() {
      debugger;
      axios.post(`${this.API_URL}api/token/`, this.data)
        .then((response) => {
          store.commit('setTokens', response.access, response.refresh);
          this.dialog = false;
          this.showSuccess = true;
        })
        .catch((error) => {
          this.responseObj = error;
          this.showError = true;
          console.error(error);
        });
    },
    onLogoutClick() {
      // this.logout();
      store.commit('clearTokens');
    },
    // ...mapActions('logout'),
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getHeader() {
      return !this.isAuthenticated
        ? 'Du kannst dich einloggen'
        : 'Du bist bereits eingelogt';
    },
  },
};
</script>

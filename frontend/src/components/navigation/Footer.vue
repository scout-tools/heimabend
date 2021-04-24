<template>
  <div class="level">
    <login ref="login"/>
    <v-footer color="primary" padless>
      <v-row justify="center" no-gutters>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          @click="$router.push({ name: 'impressum' })"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-card-text-outline
          </v-icon>
          Impressum
        </v-btn>

        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          @click="$router.push({ name: 'datenschutz' })"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-fingerprint
          </v-icon>
          Datenschutz

        </v-btn>

        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          @click="$router.push({ name: 'aboutProject' })"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-lightbulb-on
          </v-icon>
          Idee

        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          @click="$router.push({ name: 'message' })"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-at
          </v-icon>
          Kontakt

        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          v-if="!isAuthenticated"
          @click="onClickLogin"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-chess-king
          </v-icon>
          Intern
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
          v-if="isAuthenticated"
          @click="onLogoutClicked"
        >
          <v-icon fab color="white" class="mr-1">
            mdi-logout-variant
          </v-icon>
          Logout
        </v-btn>
        <!-- <v-col class="primary lighten py-1 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} — <strong>Anmelde-Tool</strong>
        </v-col> -->
      </v-row>
    </v-footer>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Login from '@/views/components/dialogs/Login.vue'; //eslint-disable-line

export default {
  components: {
    Login,
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  data: () => ({
  }),
  methods: {
    onLogoutClicked() {
      this.$store.commit('clearTokens');
    },
    onClickLogin() {
      this.$refs.login.show();
    },
  },
};
</script>

<style scoped>
.level {
  z-index: 0 !important;
}
</style>

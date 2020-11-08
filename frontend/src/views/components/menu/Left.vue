<template>
    <v-navigation-drawer
      v-model="isDrawer"
      app
      clipped
      width="300"
    >
      <v-list>
          <v-row align="center">
             <v-card
              v-if="isAuthenticated"
              width="270"
              class="mx-auto"
              depressed
            >
              <v-list-item>
                <v-container>
                <v-row class="px-2 pb-2" v-if="isAuthenticated">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="isIsActive"
                    @change="onToggleIsActive"
                    label="Veröffentlicht"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col class="pa-0 ma-0"  align-self="center">
                    <v-icon class="pt-5" color="red">
                      mdi-eye-off-outline
                    </v-icon>
                  </v-col>
                </v-row>
                </v-container>
              </v-list-item>
            </v-card>
          </v-row>
    <v-subheader>Daten</v-subheader>
      <v-divider></v-divider>
          <v-list-item link bottom :to="{ name: 'ranking-overview' }">
            <v-list-item-icon>
              <v-icon color="orange">
                mdi-medal-outline
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Statistik</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider v-if="isAuthenticated"/>

          <v-list-item v-if="isAuthenticated" link bottom :to="{ name: 'tags' }">
            <v-list-item-icon>
              <v-icon color="green">
                mdi-tag-text-outline
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Tags</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider v-if="isAuthenticated"/>

          <v-list-item v-if="isAuthenticated"  link bottom :to="{ name: 'messageOverview' }">
            <v-list-item-icon>
              <v-icon color="black">
                mdi-message-text-outline
                </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Nachrichten</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        <v-divider/>
      <v-spacer dark class="my-6"/>
      </v-list>
      <template v-slot:append>
        <v-list bottom>
      <v-subheader>Über Uns</v-subheader>
      <v-divider/>
          <v-list-item link bottom v-if="!isAuthenticated">
            <v-list-item-icon>
              <v-icon >
                mdi-login
                </v-icon>
            </v-list-item-icon>
            <v-list-item-content
              @click="onClickLogin()"
            >
              <v-list-item-title>
                Einloggen
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link bottom v-if="isAuthenticated">
            <v-list-item-icon>
              <v-icon >
                mdi-logout
                </v-icon>
            </v-list-item-icon>
            <v-list-item-content
              @click="onClickLogout()"
            >
              <v-list-item-title>
                Ausloggen
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider/>
          <v-list-item link bottom :to="{ name: 'message' }">
            <v-list-item-icon>
              <v-icon color="blue">
                mdi-android-messages
                </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                Kontakt / Nachricht
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        <v-divider/>
          <v-list-item link bottom :to="{ name: 'faq' }">
            <v-list-item-icon>
              <v-icon color="green">
                mdi-frequently-asked-questions
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                Fragen / Antworten
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        <v-divider/>
          <v-list-item link bottom :to="{ name: 'aboutProject' }">
            <v-list-item-icon>
              <v-icon color="orange lighten-2">
                mdi-emoticon-happy-outline
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                Unsere Idee
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        <v-divider/>
          <v-list-item link bottom :to="{ name: 'impressum' }">
            <v-list-item-icon>
              <v-icon color="red">
                mdi-shield-sun-outline
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Impressum / Datenschutz</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
     </template>
      <login ref="login"/>
    </v-navigation-drawer>

</template>

<script>
import Login from '@/views/components/dialogs/Login.vue'; //eslint-disable-line

export default {
  components: {
    Login,
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    isDrawer: false,
  }),
  methods: {
    onClickLogin() {
      this.$refs.login.show();
    },
    onClickLogout() {
      this.$refs.login.onLogoutClick();
    },
    onToggleIsActive() {
      this.$store.commit('toggleIsActive');
    },
    toggleDrawer() {
      this.isDrawer = !this.isDrawer;
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isIsActive: {
      get() {
        return this.$store.getters.isActive;
      },
      set() {
        return false;
      },
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
  },
  created() {
    this.isDrawer = false;
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(40, 158, 40)
}
</style>

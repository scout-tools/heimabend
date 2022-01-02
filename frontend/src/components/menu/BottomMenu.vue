<template>
  <v-bottom-sheet v-model="sheet">
    <v-list>
      <v-subheader>Menu</v-subheader>
      <v-list-item
        v-show="!tile.auth || isAuthenticated"
        v-for="tile in tiles"
        :key="tile.title"
        @click="onClickItem(tile)"
      >
        <v-list-item-avatar>
          <v-icon>
            {{ tile.icon }}
          </v-icon>
        </v-list-item-avatar>
        <v-list-item-title>{{ tile.title }}</v-list-item-title>
      </v-list-item>
      <v-list-item
        v-if="isAuthenticated"
        @click="onLogoutClicked()"
      >
        <v-list-item-avatar>
          <v-icon>
            mdi-logout-variant
          </v-icon>
        </v-list-item-avatar>
        <v-list-item-title> Logout</v-list-item-title>
      </v-list-item>
      <v-list-item
        v-if="!isAuthenticated"
        @click="onClickLogin()"
      >
        <v-list-item-avatar>
          <v-icon>
            mdi-login-variant
          </v-icon>
        </v-list-item-avatar>
        <v-list-item-title> Login</v-list-item-title>
      </v-list-item>
    </v-list>
    <login ref="login"/>
  </v-bottom-sheet>
</template>

<script>
import { mapGetters } from 'vuex';
import Login from '@/views/components/dialogs/Login.vue'; //eslint-disable-line

export default {
  components: {
    Login,
  },
  data: () => ({
    sheet: false,
    tiles: [
      {
        icon: 'mdi-calculator-variant-outline',
        title: 'Statistik',
        link: 'ranking-overview',
      },
      {
        icon: 'mdi-frequently-asked-questions',
        title: 'Fragen & Antworten',
        link: 'faq',
      },
      {
        icon: 'mdi-tools',
        title: 'Sheldon Panel',
        link: 'admin-heimabend',
        auth: true,
      },
      {
        icon: 'mdi-lightbulb-on',
        title: 'Idee',
        link: 'aboutProject',
      },
      {
        icon: 'mdi-at',
        title: 'Kontakt',
        link: 'message',
      },
      {
        icon: 'mdi-card-text-outline',
        title: 'Impressum',
        link: 'impressum',
      },
      {
        icon: 'mdi-fingerprint',
        title: 'Datenschutz',
        link: 'datenschutz',
      },
    ],
  }),
  methods: {
    show() {
      this.sheet = true;
    },
    onClickItem(tile) {
      this.$router.push({
        name: tile.link,
      });
      this.sheet = false;
    },
    onLogoutClicked() {
      this.$store.commit('clearTokens');
    },
    onClickLogin() {
      this.$refs.login.show();
    },
  },
  computed: {
    ...mapGetters([
      'isAuthenticated',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
  },
};
</script>

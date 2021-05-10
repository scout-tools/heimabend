<template>
  <v-container fluid class="ma-5">
    <v-row align="center" justify="center">
      <router-link :to="{ name: 'inspi-easter-egg' }">
        <v-img
          :src="require('@/assets/inspi/inspi_danke.webp')"
          max-width="350"
        />
      </router-link>
    </v-row>
    <v-row align="center" justify="center">
      Die Nachricht wurde an mich gesendet.
    </v-row>
    <v-row align="center" justify="center">
      <router-link
        :to="{ name: 'overview' }">
      <v-btn class="ma-5" color="primary">
        Zurück zur Startseite
      </v-btn>
      </router-link>
    </v-row>
  </v-container>
</template>

<script>
// eslint-disable-next-line
import CommentBox from '@/components/box/Comment.vue';

export default {
  created() {
    this.$store.commit('setHeaderString', 'Nachricht gesendet');
  },
};
</script>

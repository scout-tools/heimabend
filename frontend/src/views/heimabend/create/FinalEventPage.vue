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
      Vielen Dank für deine Heimabend-Idee! <br />
      <br />
      Wir freuen uns über deinen Beitrag zum Inspirator. <br />
      Das Team wird sich deiner Idee zeitnah widmen und sie veröffentlichen.
      <br />
      Bei Rückfragen dazu melden wir uns über die von dir angegebene
      E-Mail-Adresse bei dir. <br />
      Wenn du Fragen an uns hast, nutze gerne das Kontaktformular. <br />
    </v-row>
    <v-row align="center" justify="center">
      <router-link
        :to="{ name: 'overview' }">
        <v-btn class="ma-5" color="primary">
          Zurück zur Startseite
        </v-btn>
      </router-link>
    </v-row>
    <v-row align="center" justify="center">
      <CommentBox
        headerText="Kommentar zum neuen Heimabend schreiben"
        color="#F6F6F6"
        :showType="false"
        allowedMessageTypes="question"
      />
    </v-row>
  </v-container>
</template>

<script>
// eslint-disable-next-line
import CommentBox from '@/components/box/Comment.vue';

export default {
  components: {
    CommentBox,
  },
  created() {
    this.$store.commit('setHeaderString', 'Erstellung beendet');
  },
};
</script>

<template>
    <v-container fluid class="maxWidth">
    <v-row align="center" justify="center">
      <v-col md="6">
        <h1 class="display-1 ma-3">
          Du bist super.
        </h1>
        <p class="body-1 block">
          Mit dem Ausfüllen dieser Umfrage hast du einen wichtigen
          Beitrag dazu geleistet die einzelnen Heimabend-Ideen
          zu bewerten und damit auch den Inspirator attraktiver zu machen.
          <br> <br>
          In Zukunft können wir dir damit die hoffentlich besten
          Ideen aus unserer großen Sammlung vorschlagen und dir
          für deine Gruppenstunden etwas Inspiration mitgeben.
        </p>
      </v-col>
      <v-col md="6">
        <v-img
          :src="require('@/assets/inspi/inspi_danke.webp')"
          class="commenBox"
          max-width="350"
        />
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col md="6">
        <h1 class="display-1 ma-3">
          Kommentar
        </h1>
        <p class="body-1 block">
          Wir würden uns sehr darüber freuen, wenn du uns über die
          Kommentarfunktion einen Kommentar mitgibst. Ist dir was aufgefallen?
          Kann ich was besser machen? Hast du noch eine Idee?
        </p>
      </v-col>
      <v-col md="6">
      <CommentBox
        headerText="Kommentar schreiben"
        color="#F6F6F6"
        :showType="false"
        allowedMessageTypes="question"
        class="commenBox"
      />
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <router-link :to="{ name: 'overview' }" class="no-underline">
        <v-btn class="ma-4" light outlined color="red">
          <v-icon left>mdi-flag-checkered</v-icon>
          Zurück zur Startseite
        </v-btn>
      </router-link>
      <router-link :to="{ name: 'scoring-test', params: { id: experimentId }}" class="no-underline">
        <v-btn class="ma-4" color="success">
          <v-icon left>mdi-food-apple</v-icon>
          Weiter füttern
        </v-btn>
      </router-link>
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
  computed: {
    experimentId() {
      return this.$route.params.id;
    },
  },
  created() {
    this.$store.commit('setHeaderString', 'Umfrage fertig');
  },
};
</script>

<style scoped>
.commenBox {
  width: 90vw !important;
}
.maxWidth {
  max-width: 800px !important;
}
.block {
  text-align: justify !important;
}
</style>

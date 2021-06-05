<template>
    <v-container fluid class="maxWidth">
    <v-row align="center" justify="center">
      <v-col md="6" align="center" justify="center">
        <h1 class="display-1 ma-3">
          Herzlich Willkommen!
        </h1>
        <p class="body-1 block">
          Darf ich mich vorstellen? Ich bin Inspi – der kreative Kopf
          hinter dem Heimabend-Inspirator. <br> <br>
          Damit diese Plattform mit verschiedenen Ideen noch weiter wachsen
          kann und dir dabei
          automatisch die für dich besten Ideen vorschlagen kann, brauche ich deine
          Unterstützung.
        </p>
      </v-col>
      <v-col md="6" align="center" justify="center">
      <router-link :to="{ name: 'inspi-easter-egg' }">
        <v-img
          :src="require('@/assets/inspi/inspi_hungry.png')"
          max-width="250"
        />
      </router-link>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" align="center" justify="center">
        <h1 class="display-1 ma-3">
          Ich habe Hunger!
        </h1>
        <p class="body-1 block">
          Ich ernähre mich von der Meinung der verschiedenen Personen, die diese
          Website nutzen und kann dir erst dann die besten Ideen vorschlagen,
          wenn ich wirklich satt bin. <br>
          Daher möchte ich dich bitten, an der kleinen
          Umfrage teilzunehmen und verschiedene ausgewählte Heimabend-Ideen für
          mich zu bewerten. <br> <br>
          Ich freue mich auf deine Meinungen.

        </p>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="12">
      <router-link
        :to="{ name: 'scoring-setup' }" class="no-underline">
        <v-btn class="ma-2" color="primary">
          Weiter
          <v-icon right>mdi-chevron-right</v-icon>
        </v-btn>
      </router-link>
      </v-col>
    </v-row>
    </v-container>
</template>

<script>
export default {
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: [],
    loading: true,
    show: true,
  }),

  created() {
    this.$store.commit('setHeaderString', 'Hilf Inspi');
    this.$store.commit('setIsScoringMode', true);
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
  },
};
</script>

<style scoped>
.maxWidth {
  max-width: 800px !important;
}

.block {
  text-align: justify !important;
}
</style>

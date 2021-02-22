<template>

  <v-form>
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <h1> Füttere Inspi mit Daten</h1>
          <p>
            Beantworte folgende Fragen und helfe Inspi klüger
            zu werden. inspi freut sich über deine Meinung.
          </p>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center">Wie alt bist du?</p>
        </v-col>
        <v-btn-toggle color="primary"  v-model="toggle_exclusive" mandatory>
          <v-btn> - </v-btn>
          <v-btn> 7-10 </v-btn>
          <v-btn> 10-13 </v-btn>
          <v-btn> 14-18 </v-btn>
          <v-btn> 19-30 </v-btn>
          <v-btn> 30-60 </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center">In einer Gruppe Aktiv?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="toggle_exclusive" mandatory>
          <v-btn> - </v-btn>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center">Bist du Gruppenführer_in?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="toggle_exclusive" mandatory>
          <v-btn> - </v-btn>
          <v-btn> Ja </v-btn>
          <v-btn> Nein </v-btn>
        </v-btn-toggle>
      </v-row>
      <v-divider class="my-5"></v-divider>
      <v-row align="center" justify="center">
        <v-col cols="12">
        <router-link
          :to="{ name: 'scoring-test'}"
          class="no-underline"
        >
          <v-btn
            color="primary"
          >
            <v-icon left>mdi-flash</v-icon>
            Loslegen!
          </v-btn>
        </router-link>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>

export default {
  props: [],

  components: {
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: [],
    loading: true,
    show: true,
    trans: 'slide-right',
  }),

  mounted() {
    this.getEvent();
    this.$store.commit('setIsScoringMode', true);
  },

  methods: {
  },
};
</script>

<style scoped>
</style>

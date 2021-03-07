<template>
  <v-form>
    <v-container fluid>
      <v-row align="center" justify="center">
        <h1>Ich bin Inspi</h1>
      </v-row>
      <v-row align="center" justify="center">
        <v-img :src="require('@/assets/inspi.png')" max-width="200" />
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p>
            <b>Deine Meinung</b> ist meine Leibspeise. <br />
            Helfe mir bitte statt zu werden.<br />
            <br />
            Damit ich dir passendsten Inspirationen bieten kann, brauche ich
            Futter. Füttere sie mit so vielen Ideen und Einschätzungen von dir
            wie möglich, damit ich allen Pfadfindern die besten Inspirationen
            bieten kann.<br />
          </p>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center"><b>Wie alt bist du?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.age_level" mandatory>
          <v-btn> - </v-btn>
          <v-btn> 6-13 </v-btn>
          <v-btn> 14-18 </v-btn>
          <v-btn> 19-30 </v-btn>
          <v-btn> 30-60 </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center"><b>Bist du Gruppenführer_in?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.group_leader" mandatory>
          <v-btn> Nein </v-btn>
          <v-btn> Ja </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider class="my-5"></v-divider>

      <v-row align="center" justify="center" v-if="data.group_leader === 0">
        <v-col cols="12">
          <p class="text-center">In welcher Gruppe Aktiv?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.group_type" mandatory>
          <v-btn> - </v-btn>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>
      <v-row align="center" justify="center" v-if="data.group_leader === 1">
        <v-col cols="12">
          <p class="text-center">Wo Gruppenführer?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.group_type" mandatory>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>
      <v-divider class="my-5"></v-divider>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <v-btn color="primary" @click="createExperiment">
            <v-icon left>mdi-flash</v-icon>
            Loslegen!
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import axios from 'axios';

export default {
  props: [],

  components: {},

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: [],
    loading: true,
    show: true,
    trans: 'slide-right',
    data: {
      age_level: 0,
      group_type: 0,
      group_leader: 0,
    },
  }),

  mounted() {
    this.$store.commit('setIsScoringMode', true);
  },

  methods: {
    createExperiment() {
      axios
        .post(`${this.API_URL}basic/experiment/`, {
          age_level: this.data.age_level,
          group_type: this.data.group_type,
          group_leader: this.data.group_leader,
        })
        .then((response) => {
          this.$router.push({
            name: 'scoring-test',
            params: {
              id: response.data.id,
            },
          });
        });
    },
  },
};
</script>

<style scoped>
</style>

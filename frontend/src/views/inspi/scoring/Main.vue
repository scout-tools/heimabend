<template>
  <v-form class="ma-4">
    <v-container fluid>
      <v-row align="center" justify="center">
        <h1>Hallo, ich bin Inspi.</h1>
      </v-row>
      <v-row align="center" justify="center">
      <router-link :to="{ name: 'inspi-easter-egg' }">
        <v-img :src="require('@/assets/inspi/inspi_hungry.png')" max-width="350" />
      </router-link>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p>
            <b>Deine Meinung</b> ist meine Leibspeise. <br />
            Hilf mir bitte satt zu werden.<br />
            <br />
            Damit ich dir und allen anderen Pfadfindern passende Inspiration
            bieten kann, brauche ich
            <b>gutes Futter</b>. <br />
            Füttere mich mit so vielen Ideen und Meinungen von dir wie möglich.
            <br />
            Ich danke dir.
          </p>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center"><b>Wie alt bist du?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.ageLevel" mandatory>
          <v-btn> - </v-btn>
          <v-btn> 6-13 </v-btn>
          <v-btn> 14-18 </v-btn>
          <v-btn> 19-30 </v-btn>
          <v-btn> 30-60 </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider inset class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-col cols="12">
          <p class="text-center"><b>Bist du aktuell Gruppenführer_in?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupLeader" mandatory>
          <v-btn> Nein </v-btn>
          <v-btn> Ja </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider inset class="my-5"></v-divider>

      <v-row align="center" justify="center" v-if="data.groupLeader === 0">
        <v-col cols="12">
          <p class="text-center"><b>In welcher Gruppe bist du derzeit aktiv?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupType" mandatory>
          <v-btn> - </v-btn>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>
      <v-row align="center" justify="center" v-if="data.groupLeader === 1">
        <v-col cols="12">
          <p class="text-center">Wo Gruppenführer?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupType" mandatory>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider inset class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-flex ma-3 xs10 sm7 md4>
          <v-expansion-panels flat>
            <v-expansion-panel>
              <v-expansion-panel-header color="#FBFBFB">
                <b>Wie genau kannst du mich füttern?</b>
              </v-expansion-panel-header>
              <v-expansion-panel-content color="#FBFBFB">
                <p>
                  Bitte gib zu jedem Heimabend, den ich dir zeige, deine Meinung
                  ab. Du hast folgene Auswahlmöglichkeiten
                </p>

                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-rating
                        color="warning"
                        background-color="warning"
                        empty-icon="mdi-star-outline"
                        full-icon="mdi-star"
                        half-icon="mdi-star-half-full"
                        length="5"
                        value=5>
                      </v-rating>
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      Der Heimabend ist
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      sehr gut beschrieben.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-rating
                        color="warning"
                        background-color="warning"
                        empty-icon="mdi-star-outline"
                        full-icon="mdi-star"
                        half-icon="mdi-star-half-full"
                        length="5"
                        value=3>
                      </v-rating>
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      Der Heimabend ist
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      mittelmäßig beschrieben.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-rating
                        color="warning"
                        background-color="warning"
                        empty-icon="mdi-star-outline"
                        full-icon="mdi-star"
                        half-icon="mdi-star-half-full"
                        length="5"
                        value=1>
                      </v-rating>
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      Der Heimabend
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      ist sehr schlecht beschrieben.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item three-line>
                  <v-list-item-icon>
                  <v-icon large color="red"> mdi-emoticon-confused </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title><b>Unklar</b></v-list-item-title>
                    <v-list-item-subtitle>
                      Der Heimabend
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      ist unverständlich.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-flex>
      </v-row>

      <v-divider inset class="my-5"></v-divider>

      <v-row align="center" justify="center">
        P.S. Deine Meinung und vor allen Dingen deine Daten
        bleiben natürlich vollkommen anonym.
      </v-row>
      <v-divider inset class="my-5"></v-divider>
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
      ageLevel: 0,
      groupType: 0,
      groupLeader: 0,
    },
  }),

  created() {
    this.$store.commit('setIsScoringMode', true);
    this.$store.commit('setHeaderString', 'Hilf Inspi');
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
  },

  methods: {
    createExperiment() {
      axios
        .post(`${this.API_URL}basic/experiment/`, {
          ageLevel: this.data.ageLevel,
          groupType: this.data.groupType,
          groupLeader: this.data.groupLeader,
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

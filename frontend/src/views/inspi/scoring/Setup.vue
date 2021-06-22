<template>
  <v-form class="ma-3">
    <v-container fluid class="maxWidth">
      <v-row align="center" justify="center">
        <v-col cols="12" class="mt-4 pa-2">
          <p class="text-center pa-0 ma-0"><b>Wie alt bist du?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.ageLevel" mandatory>
          <v-btn> - </v-btn>
          <v-btn> 6-13 </v-btn>
          <v-btn> 14-18 </v-btn>
          <v-btn> 19-30 </v-btn>
          <v-btn> 30-60 </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-row align="center" justify="center">
        <v-col cols="12" class="mt-4 pa-2">
          <p class="text-center pa-0 ma-0">
            <b>Bist du aktuell Gruppenführer_in?</b>
          </p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupLeader" mandatory>
          <v-btn> Nein </v-btn>
          <v-btn> Ja </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-row align="center" justify="center" v-if="data.groupLeader === 0">
        <v-col cols="12" class="mt-4 pa-2">
          <p class="text-center pa-0 ma-0">
            <b>In welcher Gruppe bist du derzeit aktiv?</b>
          </p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupType" mandatory>
          <v-btn> - </v-btn>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>
      <v-row align="center" justify="center" v-if="data.groupLeader === 1">
        <v-col cols="12" class="mt-4 pa-2">
          <p class="text-center pa-0 ma-0">Wo Gruppenführer?</p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.groupType" mandatory>
          <v-btn> Meute </v-btn>
          <v-btn> Sippe </v-btn>
          <v-btn> Roverrunde </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-row align="center" justify="center">
        <v-card class="my-3 maxWidth">
          <v-expansion-panels flat>
            <v-expansion-panel>
              <v-expansion-panel-header color="white">
                <b>Wie genau funktioniert diese Umfrage?</b>
              </v-expansion-panel-header>
              <v-expansion-panel-content color="white">
                <p class="body-1 block">
                  Bitte gib zu jeder dir vorgeschlagenen Heimabend-Idee deine
                  persönliche Meinung ab, bewerte dabei wie gut der Heimabend
                  beschrieben ist. Du folgende Auswahlmöglichkeiten:
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
                        value="5"
                      >
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
                        value="3"
                      >
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
                        value="1"
                      >
                      </v-rating>
                    </v-list-item-title>
                    <v-list-item-subtitle> Der Heimabend </v-list-item-subtitle>
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
                    <v-list-item-subtitle> Der Heimabend </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      ist unverständlich.
                    </v-list-item-subtitle>
                    <p>
                      Du hast während der gesamten Zeit neben der Bewertung auch die
                      Gelegenheit durch einen Kommentar die jeweilige Heimabend-Idee
                      genauer zu bewerten.
                    </p>
                  </v-list-item-content>
                </v-list-item>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-row>
      <v-row align="center" justify="center">
        <v-card class="my-3 maxWidth">
          <v-expansion-panels fluid flat>
            <v-expansion-panel fluid>
              <v-expansion-panel-header color="white">
                <b>Was passiert mit deinen Daten?</b>
              </v-expansion-panel-header>
              <v-expansion-panel-content color="white">
                <p class="body-1 block">
                  Deine Bewertung und die von dir angegeben Daten bleiben
                  vollkommen anonym und dienen dem Inspirator-Team zur
                  Auswertung der verschiedenen Heimabend-Ideen. Mithilfe deiner
                  Bewertung möchten wir verschiedenen Personen, die diese Seite
                  nutzen besten Heimabend-Ideen vorschlagen können und aktuelle
                  Ideen verbessern.
                </p>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-row>

      <v-row align="center" justify="center">
        <v-col cols="12">
          <v-btn color="primary" @click="createExperiment">
            Loslegen!
            <v-icon right>mdi-flash</v-icon>
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
    this.$store.commit('setHeaderString', 'Hilf Inspi');
    this.$store.commit('setIsScoringMode', true);
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
.maxWidth {
  width: 600px !important;
}

.block {
  text-align: justify !important;
}
</style>

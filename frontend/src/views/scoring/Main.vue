<template>
  <v-form>
    <v-container fluid>
      <v-row>
        <router-link :to="{ name: 'overview' }" class="no-underline mr-4">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                fab
                small
                outlined
                color="primary"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </template>
            <span>Zurück zum Inspirator</span>
          </v-tooltip>
        </router-link>
      </v-row>
      <v-row align="center" justify="center">
        <h1>Hallo, ich bin Inspi.</h1>
      </v-row>
      <v-row align="center" justify="center">
      <router-link :to="{ name: 'inspi-easter-egg' }">
        <v-img :src="require('@/assets/inspi.png')" max-width="200" />
      </router-link>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <p>
            <b>Dein Meinung</b> ist meine Leibspeise. <br />
            Hilf mir bitte satt zu werden.<br />
            <br />
            Damit ich dir und allen anderen Pfadfinder passende Inspirationen
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
        <v-btn-toggle color="primary" v-model="data.age_level" mandatory>
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
          <p class="text-center"><b>Bist du Gruppenführer_in?</b></p>
        </v-col>
        <v-btn-toggle color="primary" v-model="data.group_leader" mandatory>
          <v-btn> Nein </v-btn>
          <v-btn> Ja </v-btn>
        </v-btn-toggle>
      </v-row>

      <v-divider inset class="my-5"></v-divider>

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

      <v-divider inset class="my-5"></v-divider>

      <v-row align="center" justify="center">
        <v-flex ma-3 xs10 sm7 md4>
          <v-expansion-panels flat>
            <v-expansion-panel>
              <v-expansion-panel-header disable-icon-rotate>
                Wie genau kannst du mich füttern? (Klicke hier)
                <template v-slot:actions>
                  <v-icon color="success"> mdi-help-circle-outline </v-icon>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <p>
                  Bitte gib zu jedem Heimabend den ich dir zeige dein Meinung
                  ab. Du hast folgene Auswahlmöglichkeiten
                </p>

                <v-list-item three-line>
                  <v-list-item-icon>
                  <v-icon large color="orange"> mdi-medal </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title><b>MEGA</b></v-list-item-title>
                    <v-list-item-subtitle>
                      Ich finde diesen Heimabend mega gut und will
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      ihm am liebsten sofort machen.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-list-item three-line>
                  <v-list-item-icon>
                  <v-icon large color="green"> mdi-thumb-up </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title><b>Cool</b></v-list-item-title>
                    <v-list-item-subtitle>
                      Ich finde den Heimabend cool und würde ihn
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      so mit meiner Gruppe durchführen.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-list-item three-line>
                  <v-list-item-icon>
                  <v-icon large color="grey"> mdi-emoticon-confused </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title><b>Unklar</b></v-list-item-title>
                    <v-list-item-subtitle>
                      Ich verstehe den Heimabend nicht und
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      kann ihn so nicht durchführen.
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-list-item three-line>
                  <v-list-item-icon>
                  <v-icon large color="red"> mdi-thumb-down </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title><b>Doof</b></v-list-item-title>
                    <v-list-item-subtitle>
                      Ich mag den Heimabend nicht oder mag
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      die Idee nicht.
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
        Deine Daten behandele ich natürlich anonym.
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

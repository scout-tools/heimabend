<template>
  <v-container fluid>
    <v-row align="center" justify="center">
        <p>Inspi's Sättigungsgrad</p>
        <v-progress-linear v-model="getCount" height="25">
          <strong>{{ Math.ceil(getCount) }}%</strong>
        </v-progress-linear>
    </v-row>
    <v-row v-if="!isFinished">
      <transition :name="trans">
        <heimabend-card
          class="mb-10"
          :items="currenElement"
          :isDetailsView="true"
          v-show="show"
        />
      </transition>
    </v-row>

    <v-row v-else align="center" justify="center">
      <v-container>
        <v-row align="center" justify="center">
          <v-img :src="require('@/assets/inspi/inspi_happy.png')" max-width="350" />
        </v-row>
        <v-row align="center" justify="center">
          <p>Vielen Dank. Jetzt bin ich satt.</p>
        </v-row>

        <v-divider inset class="my-5"></v-divider>

        <v-row align="center" justify="center">
          <router-link :to="{ name: 'overview' }" class="no-underline mr-4">
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-btn v-bind="attrs" v-on="on">
                  <v-icon left>mdi-flag-checkered</v-icon>
                  Zurück zum Inspirator
                </v-btn>
              </template>
              <span>Zurück zum Inspirator</span>
            </v-tooltip>
          </router-link>
        </v-row>
        <v-divider inset class="my-5"></v-divider>
        <v-row align="center" justify="center">
          <v-btn @click="resetCount">
            <v-icon left>mdi-repeat</v-icon>
            Nochmal Füttern
          </v-btn>
        </v-row>
      </v-container>
    </v-row>
    <v-bottom-navigation grow fixed v-model="value">
      <v-tooltip top open-delay="1000">
        <template v-slot:activator="{ on, attrs }">
          <v-btn large @click="onClickComplain()" v-bind="attrs" v-on="on">
            <span>Unklar</span>
            <v-icon large color="red"> mdi-emoticon-confused </v-icon>
          </v-btn>
        </template>
        <span>Ich verstehe die Beschreibung nicht.</span>
      </v-tooltip>
      <v-rating
        :x-large="!$vuetify.breakpoint.smAndDown"
        color="warning"
        background-color="warning"
        empty-icon="mdi-star-outline"
        full-icon="mdi-star"
        half-icon="mdi-star-half-full"
        hover
        length="5"
        v-model="score"
      ></v-rating>

      <v-tooltip top open-delay="1000">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            large
            @click="onClickSendDecison()"
            v-bind="attrs"
            v-on="on"
            :disabled="score==0"
          >
            <span>{{ valueName }}</span>
            <v-icon large color="green"> mdi-send </v-icon>
          </v-btn>
        </template>
        <span>Bewertung absenden.</span>
      </v-tooltip>
    </v-bottom-navigation>
  </v-container>
</template>

<script>
import axios from 'axios';

import HeimabendCard from '@/views/heimabend/cards/Heimabend.vue';
import { serviceMixin } from '@/mixins/serviceMixin.js'; // eslint-disable-line

export default {
  mixins: [serviceMixin],
  props: [],

  components: {
    HeimabendCard,
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: [],
    loading: true,
    show: true,
    trans: 'slide-right',
    count: 0,
    value: 0,
    score: 0,
    decision: 1,
    isLoading: true,
  }),

  mounted() {
    this.getFirstEvent();
    this.$store.commit('setIsScoringMode', true);
  },
  computed: {
    getCount() {
      return Math.min(this.count * 10, 100);
    },
    isFinished() {
      return this.getCount >= 99;
    },
    experimentId() {
      return this.$route.params.id;
    },
    eventId() {
      return this.items[0].id;
    },
    currenElement() {
      return [this.items[0]];
    },
    valueName() {
      let scoreName = '-';
      switch (this.score) {
        case 1:
          scoreName = 'Sehr Doof';
          break;
        case 2:
          scoreName = 'Doof';
          break;
        case 3:
          scoreName = 'Neutral';
          break;
        case 4:
          scoreName = 'Cool';
          break;
        case 5:
          scoreName = 'Sehr Cool';
          break;
        default:
          scoreName = 'Auswählen';
          break;
      }
      return scoreName;
    },
  },
  methods: {
    resetCount() {
      this.getFirstEvent();
      this.count = 0;
    },
    async getRandomEvent() {
      const path = `${
        this.API_URL
      }basic/random-event/?&timestamp=${new Date().getTime()}`;
      const response = await axios.get(path);

      return response.data;
    },
    async postExperimentItem(decision) {
      const path = `${this.API_URL}basic/experiment-item/`;
      return axios.post(path, {
        event: this.eventId,
        experiment: this.experimentId,
        score: decision,
        jh
      });
    },
    getFirstEvent() {
      this.loading = true;
      Promise.all([this.getRandomEvent()])
        .then((values) => {
          [this.items] = values;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
    onClickSendDecison() {
      this.trans = 'slide-right';
      this.saveDecision(this.score);
    },
    onClickComplain() {
      this.trans = 'slide-down';
      this.saveDecision(0);
    },
    saveDecision(decision) {
      this.show = false;
      this.loading = true;
      Promise.all([
        this.postExperimentItem(decision),
        new Promise(resolve => setTimeout(resolve, 700)),
      ])
        .then(() => {
          this.items.shift();
          this.loading = false;
          this.show = true;
          this.count = this.count + 1;
          this.score = 0;
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped>
.slide-right-leave-active {
  transition: all 0.7s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-right-leave-to {
  transform: translateX(500px);
}
.slide-left-leave-active {
  transition: all 0.7s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-left-leave-to {
  transform: translateX(-500px);
}
.slide-up-leave-active {
  transition: all 0.7s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-up-leave-to {
  transform: translateY(-500px);
}
.slide-down-leave-active {
  transition: all 0.7s ease-in-out;
}
.slide-down-leave-to {
  transform: scale(0.3);
}
span {
  align-items: center;
}
.vertical-center {
  display: inline-flex;
  align-items: center;
}
</style>

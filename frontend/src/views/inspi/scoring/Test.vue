<template>
  <v-container fluid>
    <v-row align="center" justify="center">
        <v-progress-linear :value="getCount" height="25" readonly striped color="green">
          <strong>{{ `Zu ${Math.ceil(getCount)}% satt`}}</strong>
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
          <router-link :to="{ name: 'scoring-final' }" class="no-underline">
            <v-btn class="ma-2" color="primary">
              <v-icon left>mdi-fast-forward</v-icon>
                Weiter
              </v-btn>
          </router-link>
        </v-row>
      </v-container>
    </v-row>
    <v-row class="mb-10" v-if="showCommentBox && !isFinished">
      <CommentBox
        class="mb-10"
        headerText="Verbesserungsvorschlag"
        color="#F6F6F6"
        allowedMessageTypes="comment"
        :eventIdParam="eventId"
        @messageSent="onMessageSent"
      />
    </v-row>
    <v-row v-if="!showCommentBox && !isFinished" align="center" justify="center" class="mb-10">
      <p>Danke für den Vorschlag</p>
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

// eslint-disable-next-line
import CommentBox from '@/components/box/Comment.vue';

import HeimabendCard from '@/views/heimabend/cards/Heimabend.vue'; // eslint-disable-line
import { serviceMixin } from '@/mixins/serviceMixin.js'; // eslint-disable-line

export default {
  mixins: [serviceMixin],
  props: [],

  components: {
    CommentBox,
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
    showCommentBox: true,
  }),

  mounted() {
    this.getFirstEvent();
    this.$store.commit('setIsScoringMode', true);
  },
  computed: {
    getCount() {
      return Math.min(this.count * 25, 100);
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
    onMessageSent() {
      this.showCommentBox = false;
    },
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
      this.showCommentBox = true;
      window.scrollTo(0, 0);
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
          this.checkLast();
        })
        .catch(() => {
          this.loading = false;
        });
    },
    checkLast() {
      if (this.isFinished) {
        this.$router.push({
          name: 'scoring-final',
          params: {
            id: this.experimentId,
          },
        });
      }
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

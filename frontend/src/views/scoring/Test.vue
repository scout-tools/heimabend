<template>
  <v-container>
    <transition :name="trans">
      <heimabend-card
        v-touch="{
          left: () => trigger('slide-left'),
          right: () => trigger('slide-right'),
        }"
        class="card"
        :items="items"
        :isDetailsView="true"
        v-show="show"
      />
    </transition>
    <v-bottom-navigation grow fixed v-model="value">

    <v-tooltip top open-delay=1000>
      <template v-slot:activator="{ on, attrs }">
      <v-btn large :disabled="loading" @click="trigger('slide-left')"
          v-bind="attrs"
          v-on="on"
        >
        <span>doof</span>
        <v-icon large color="red">
          mdi-thumb-down
        </v-icon>
      </v-btn>
      </template>
      <span>Ich mag den Heimabend nicht.</span>
    </v-tooltip>

    <v-tooltip top open-delay=1000>
      <template v-slot:activator="{ on, attrs }">
      <v-btn large :disabled="loading" @click="trigger('slide-down')"
          v-bind="attrs"
          v-on="on"
        >
        <span>unklar</span>
        <v-icon large color="grey">
          mdi-emoticon-confused
        </v-icon>
      </v-btn>
      </template>
      <span>Ich verstehe den Heimabend nicht.</span>
    </v-tooltip>

    <v-tooltip top open-delay=1000>
      <template v-slot:activator="{ on, attrs }">
      <v-btn large :disabled="loading" @click="trigger('slide-up')"
          v-bind="attrs"
          v-on="on"
        >
        <span>MEGA</span>
        <v-icon large color="orange">
          mdi-medal
        </v-icon>
      </v-btn>
      </template>
      <span>Ich finde diesen Heimabend mega mega gut.</span>
    </v-tooltip>

    <v-tooltip top open-delay=1000>
      <template v-slot:activator="{ on, attrs }">
      <v-btn large :disabled="loading" @click="trigger('slide-right')"
          v-bind="attrs"
          v-on="on"
        >
        <span>cool</span>
        <v-icon large color="green">
          mdi-thumb-up
        </v-icon>
      </v-btn>
      </template>
      <span>Ich mag den Heimabend.</span>
    </v-tooltip>
    </v-bottom-navigation>
  </v-container>
</template>

<script>
import axios from 'axios';

import HeimabendCard from '@/views/heimabend/cards/Heimabend.vue';

export default {
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
    count: 1,
    value: 0,
    decision: 1,
    isLoading: true,
  }),

  mounted() {
    this.getFirstEvent();
    this.$store.commit('setIsScoringMode', true);
  },
  computed: {
    getCount() {
      return 5;
    },
    experimentId() {
      return this.$route.params.id;
    },
    eventId() {
      return this.items[0].id;
    },
  },
  methods: {
    async getRandomEvent() {
      const path = `${this.API_URL}basic/random-event/?&timestamp=${new Date().getTime()}`;
      const response = await axios.get(path);

      return response.data;
    },
    async postExperimentItem(decision) {
      const path = `${this.API_URL}basic/experiment-item/`;
      return axios.post(path, {
        event_id: this.eventId,
        experiment_id: this.experimentId,
        score: decision,
      });
    },
    getFirstEvent() {
      this.loading = true;
      Promise.all([this.getRandomEvent()]).then((values) => {
        [this.items] = values;
        this.loading = false;
      })
        .catch(() => {
          this.loading = false;
        });
    },
    saveDecision(decision) {
      this.loading = true;
      Promise.all([
        this.getRandomEvent(),
        this.postExperimentItem(decision),
        new Promise(resolve => setTimeout(resolve, 1000)),
      ]).then((values) => {
        [this.items] = values;
        this.loading = false;
        this.show = true;
      })
        .catch(() => {
          this.loading = false;
        });
    },
    trigger(name) {
      let decision = -1;
      this.trans = name;

      switch (name) {
        case 'slide-up':
          decision = 3;
          break;
        case 'slide-left':
          decision = 1;
          break;
        case 'slide-right':
          decision = 2;
          break;
        case 'slide-down':
          decision = 4;
          break;
        default:
          decision = 0;
          break;
      }
      this.show = false;
      this.count = this.count + 1;

      this.saveDecision(decision);
    },
  },
};
</script>

<style scoped>
.slide-right-leave-active {
  transition: all 1s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-right-leave-to {
  transform: translateX(500px);
}
.slide-left-leave-active {
  transition: all 1s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-left-leave-to {
  transform: translateX(-500px);
}
.slide-up-leave-active {
  transition: all 1s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-up-leave-to {
  transform: translateY(-500px);
}
.slide-down-leave-active {
  transition: all 1s ease-in-out;
}
.slide-down-leave-to {
  transform: scale(0.3)
}
span {
  align-items: center;
}
.vertical-center {
  display: inline-flex;
  align-items: center;
}
</style>

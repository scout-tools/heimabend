<template>
  <v-container>
    <transition :name="trans">
      <heimabend-card
        v-touch="{
          left: () => trigger('slide-left'),
          right: () => trigger('slide-right'),
        }"
        class="card"
        :items="item"
        :isDetailsView="true"
        v-show="show"
      />
    </transition>
    <v-bottom-navigation grow fixed v-model="value">
      <v-btn large value="recent" @click="trigger('slide-left')">
        <span>Öde</span>

        <v-icon large color="red">mdi-thumb-down</v-icon>
      </v-btn>

      <v-btn value="nearby" @click="trigger('slide-up')">
        <span>Mega</span>

        <v-icon large color="orange">mdi-star</v-icon>
      </v-btn>

      <v-btn value="favorites" @click="trigger('slide-right')">
        <span>Cool</span>

        <v-icon large color="green">mdi-thumb-up</v-icon>
      </v-btn>
      <span class="vertical-center">
        {{ 'Anzahl: ' + count }}
      </span>
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
    item: [],
    loading: true,
    show: true,
    trans: 'slide-right',
    count: 1,
  }),

  mounted() {
    this.getEvent();
    this.$store.commit('setIsScoringMode', true);
  },
  computed: {
    getCount() {
      return 5;
    },
  },
  methods: {
    getEvent() {
      const path = `${this.API_URL}basic/event/121/`;
      this.loading = true;
      axios
        .get(path)
        .then((res) => {
          this.item = [res.data];
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
    trigger(name) {
      this.trans = name;
      this.show = false;
      this.count = this.count + 1;
      setTimeout(() => {
        this.show = true;
      }, 800);
    },
  },
};
</script>

<style scoped>
.slide-right-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-right-leave-to {
  transform: translateX(500px);
}

.slide-left-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-left-leave-to {
  transform: translateX(-500px);
}
.slide-up-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-up-leave-to {
  transform: translateY(-500px);
}
span {
  align-items: center;
}
.vertical-center {
  display: inline-flex;
  align-items: center;
}
</style>

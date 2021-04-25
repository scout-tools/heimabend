<template>
<v-container>
  <v-card class="mx-auto" max-width="800" justify="center">
    <v-card-title justify="center"> Top 10 Aufrufe </v-card-title>
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="n in data" :key="n.id" v-slot="{ active, toggle }">
        <v-card class="ma-4" height="120" width="250" @click="onEventClicked(n.id)">
          <v-card-subtitle class="whiteText justify-center text-center primary">
            {{ n.title }}
          </v-card-subtitle>
          <v-img :src="n.imageLink" height="70px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-card>

  <v-spacer class="py-2"/>

  <v-card class="mx-auto" max-width="800" justify="center">
    <v-card-title justify="center"> 10 Neusten Heimabende </v-card-title>
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="n in data" :key="n.id" v-slot="{ active, toggle }">
        <v-card class="ma-4" height="120" width="250" @click="onEventClicked(n.id)">
          <v-card-subtitle class="whiteText justify-center text-center primary">
            {{ n.title }}
          </v-card-subtitle>
          <v-img :src="n.imageLink" height="70px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-card>

  <v-spacer class="py-2"/>

  <v-card class="mx-auto" max-width="800" justify="center">
    <v-card-title justify="center"> 10 Besten Bewertungen </v-card-title>
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="n in data" :key="n.id" v-slot="{ active, toggle }">
        <v-card class="ma-4" height="120" width="250" @click="onEventClicked(n.id)">
          <v-card-subtitle class="whiteText justify-center text-center primary">
            {{ n.title }}
          </v-card-subtitle>
          <v-img :src="n.imageLink" height="70px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-card>

    <v-spacer class="py-2"/>

  <v-card class="mx-auto" max-width="800" justify="center">
    <v-card-title justify="center"> 10 Nachhaltige Heimabende </v-card-title>
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="n in data" :key="n.id" v-slot="{ active, toggle }">
        <v-card class="ma-4" height="120" width="250" @click="onEventClicked(n.id)">
          <v-card-subtitle class="whiteText justify-center text-center primary">
            {{ n.title }}
          </v-card-subtitle>
          <v-img :src="n.imageLink" height="70px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-card>
</v-container>
</template>

<script>
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

export default {
  mixins: [serviceMixin],
  data: () => ({
    model: null,
    data: [],
  }),
  methods: {
    loadData() {
      this.getTopViews().then((response) => {
        this.data = response.data;
      });
    },
    onEventClicked(id) {
      this.$router.push({
        name: 'heimabendDetails',
        params: { id },
      });
    },
  },
  created() {
    this.loadData();
    this.$store.commit('setHeaderString', 'Inspirationen');
  },
};
</script>

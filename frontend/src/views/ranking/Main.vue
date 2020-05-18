/* eslint-disable no-unused-vars */
<template>
<div>
   <v-container>
    <v-tabs
     fixed-tabs
     centered>
      <v-tabs-slider/>
      <v-tab>Inspiratoren</v-tab>
      <v-tab>Heimabend</v-tab>
      <!-- <v-tab>Meist aufgerufen</v-tab> -->
      <!-- <v-tab disabled>Bescuher</v-tab> -->

      <v-tab-item>
        <author/>
      </v-tab-item>
      <v-tab-item>
        <new-events-per-week/>
      </v-tab-item>
    </v-tabs>
  </v-container>
</div>
</template>

<script>
import Author from './Author.vue';
import NewEventsPerWeek from './NewEventsPerWeek.vue';

export default {
  components: {
    Author,
    NewEventsPerWeek,
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
    };
  },
  methods: {
  },
};
</script>

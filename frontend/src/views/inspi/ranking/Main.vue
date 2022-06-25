/* eslint-disable no-unused-vars */
<template>
   <v-container fluid>
    <v-tabs
     fixed-tabs
     centered>
      <v-tabs-slider/>
      <v-tab>Autor_innen</v-tab>
      <v-tab>Neue Ideen</v-tab>
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
  created() {
    this.$store.commit('setHeaderString', 'Daten');
  },
};
</script>

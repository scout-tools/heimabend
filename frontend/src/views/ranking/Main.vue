/* eslint-disable no-unused-vars */
<template>
<div>
   <v-container>
    <v-tabs
     fixed-tabs
     centered>
      <v-tabs-slider/>
      <v-tab>Inspiratoren</v-tab>
      <v-tab>Heimabende</v-tab>
      <!-- <v-tab>Meist aufgerufen</v-tab> -->
      <!-- <v-tab disabled>Bescuher</v-tab> -->

      <v-tab-item>
        <author/>
      </v-tab-item>
      <v-tab-item>
        <events-per-time :items="dateCountArray"/>
      </v-tab-item>
    </v-tabs>
  </v-container>
</div>
</template>

<script>
import axios from 'axios';

import Author from './Author.vue';
import EventsPerTime from './EventsPerTime.vue';

export default {
  components: {
    Author,
    EventsPerTime,
  },
  data() {
    return {
      dateCountArray: [],
      API_URL: process.env.VUE_APP_API,
    };
  },
  methods: {
    getData() {
      const data = [['Monat', 'Heimabende']];
      const startDate = '2019-12-01';
      const endDate = new Date().toISOString();
      const dateArray = this.dateRange(startDate, endDate);
      dateArray.forEach((date) => {
        data.push([date, this.getCount(date, this.items)]);
      });
      this.dateCountArray = data;
    },
    calculateData() {
      this.getData();
    },
    // eslint-disable-next-line no-unused-vars
    getCount(dateString, events) {
      // eslint-disable-next-line no-unused-vars
      const dateTs = new Date(dateString).getTime();
      const filteredData = events.filter(d => new Date(d.createdAt).getTime() <= dateTs);
      console.log(filteredData);
      return filteredData.length;
    },
    dateRange(startDate, endDate) {
      const start = startDate.split('-');
      const end = endDate.split('-');
      const startYear = parseInt(start[0], 10);
      const endYear = parseInt(end[0], 10);
      const dates = [];

      for (let i = startYear; i <= endYear; i += 1) {
        const endMonth = i !== endYear ? 11 : parseInt(end[1], 10) - 1;
        const startMon = i === startYear ? parseInt(start[1], 10) - 1 : 0;
        for (let j = startMon; j <= endMonth; j = j > 12 ? j % 12 || 11 : j + 1) {
          const month = j + 1;
          const displayMonth = month < 10 ? `0${month}` : month;
          dates.push([i, displayMonth, '01'].join('-'));
        }
      }
      return dates;
    },
    getEvents() {
      const path = `${this.API_URL}basic/event/`;
      this.loading = true;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
          this.loading = false;
          this.calculateData();
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
  mounted() {
    this.getEvents();
  },
};
</script>

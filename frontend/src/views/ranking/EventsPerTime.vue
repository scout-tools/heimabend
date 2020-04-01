/* eslint-disable guard-for-in */
<template>
  <v-container>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <GChart type="LineChart" :data="items" :options="chartOptions" @ready="onChartReady"/>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>

export default {
  props: {
    items: Array,
  },
  data() {
    return {
      datacollection: null,
      API_URL: process.env.VUE_APP_API,
      chartOptions: {
        title: 'Anzahl der Heimabende nach Monaten',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        legend: { position: 'bottom' },
        curveType: 'function',
        height: 500,
      },
    };
  },
  methods: {
    onChartReady(chart) {
      chart.draw(this.items, this.chartOptions);
    },
  },
};
</script>

<style>
.small {
  max-width: 600px;
  margin: 150px auto;
}
</style>

/* eslint-disable guard-for-in */
<template>
  <v-container>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <GChart
          v-show="!loading1"
          type="LineChart"
          :data="items1"
          :options="chartOptions1"
          @ready="onChartReady1"
        />
        <v-progress-circular
          v-show="loading1"
          color="primary"
          indeterminate
        />
      </v-flex>
      <v-flex ma-3 lg7>
        <GChart
          v-show="!loading2"
          type="LineChart"
          :data="items2"
          :options="chartOptions2"
          @ready="onChartReady2"
        />
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading1: true,
      loading2: true,
      items0: [],
      items1: [],
      items2: [],
      datacollection: null,
      API_URL: process.env.VUE_APP_API,
      chartOptions1: {
        title: 'Anzahl der neuen Heimabend Ideen je Kalenderwochen',
        legend: { position: 'bottom' },
        hAxis: {
          slantedText: true,
          slantedTextAngle: 60, // here you can even use 180
        },
        curveType: 'function',
        height: 500,
      },
      chartOptions2: {
        title: 'Gesamte Anzahl der Heimabend Ideen je Kalenderwochen',
        legend: { position: 'bottom' },
        hAxis: {
          slantedText: true,
          slantedTextAngle: 60, // here you can even use 180
        },
        curveType: 'function',
        height: 500,
      },
    };
  },
  methods: {
    onChartReady1(chart1) {
      const me = this;
      this.prepairData();
      setTimeout(() => {
        me.prepairData();
        chart1.draw(me.items1, me.chartOptions1);
        this.loading1 = false;
      }, 1000);
    },
    onChartReady2(chart2) {
      const me = this;
      this.prepairData();
      setTimeout(() => {
        me.prepairData();
        chart2.draw(me.items2, me.chartOptions2);

        this.loading2 = false;
      }, 1000);
    },
    prepairData() {
      const array1 = [['Woche', 'Neue Heimabende']];
      const array2 = [['Woche', 'Gesamt Heimabende']];
      // eslint-disable-next-line arrow-parens
      this.items0.forEach((item) => {
        array1.push([`${item.year.toString()} - ${item.week.toString()}`, item.score]);
        if (item.year === 2020) {
          array2.push([`${item.year.toString()} - ${item.week.toString()}`, item.score_cumulative + 11]);
        }
      });
      this.items1 = array1;
      this.items2 = array2;
    },
    getData() {
      const path = `${this.API_URL}basic/statistic/`;
      this.loading = true;
      axios.get(path)
        .then((res) => {
          this.items0 = res.data;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
.small {
  max-width: 600px;
  margin: 150px auto;
}
</style>

/* eslint-disable guard-for-in */
<template>
  <v-container fluid>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <Plotly
          :data="chartData"
          :display-mode-bar="false"
          :layout="baseLayout"
        ></Plotly>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import moment from 'moment';
import axios from 'axios';
import { Plotly } from 'vue-plotly';

export default {
  components: {
    Plotly,
  },
  computed: {
    chartData() {
        let groupedResults = _.groupBy( // eslint-disable-line
          // eslint-disable-line
          this.response, // eslint-disable-line
          ( // eslint-disable-line
            // eslint-disable-line
            result // eslint-disable-line
          ) => moment(result['createdAt']).startOf('month') // eslint-disable-line
        ); // eslint-disable-line

      return [
        {
          x: this.response.map((a) => a.createdAt), // eslint-disable-line
          y: this.response.map((a, index) => index), // eslint-disable-line
          type: 'scatter',
          name: 'Gesamt',
          line: { color: 'red' },
          marker: {
            color: '#1B4B7E',
            line: {
              width: 2.5,
            },
          },
        },
        {
          x: Object.entries(groupedResults).map((a) => moment(a[0]).toDate()), // eslint-disable-line
          y: Object.entries(groupedResults).map((a) => a[1].length), // eslint-disable-line
          type: 'scatter',
          name: 'Neu',
          line: { color: 'blue' },
        },
      ];
    },
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      response: [],
      baseLayout: {
        title: 'Neue Heimabende',
        responsive: true,
        height: 700,
        // items with a `name` attribute in template.images will be added to any
        // plot using this template
        images: [
          {
            name: 'watermark_1',
            source: 'http://localhost:8080/img/inspi.8e55ecc8.png',
            xref: 'paper',
            yref: 'paper',
            x: 0.4,
            y: 0.9,
            sizex: 0.7,
            sizey: 0.7,
            opacity: 0.1,
            layer: 'below',
          },
        ],
        showlegend: true,
        plot_bgcolor: 'rgba(27, 75, 126, 0.1)',
        xaxis: {
          title: {
            text: 'Datum',
            font: {
              size: 18,
            },
          },
        },
        yaxis: {
          title: {
            text: 'Anzahl',
            font: {
              size: 18,
            },
          },
        },
      },
    };
  },
  methods: {
    getData() {
      const path = `${this.API_URL}basic/event-timestamp`;
      this.loading = true;
      axios
        .get(path)
        .then((res) => {
          this.response = res.data;
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

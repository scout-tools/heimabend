<template>
  <v-container fluid>
    <v-row justify="center">
      <v-flex ma-3 lg7>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th>Rang</th>
                <th>Name</th>
                <th>Anzahl Heimabende</th>
                <th>Medaille</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in gerOrdered" :key="item.createdBy">
                <td class="text-left">{{ index + 1 }}</td>
                <td class="text-left">{{ item.createdBy }}</td>
                <td class="text-left">{{ item.highscore }}</td>
                <td class="text-left">
                  <v-icon :color="getAwardColor(index + 1)">{{ getIcon(index + 1) }}</v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: true,
      items: [],
      API_URL: process.env.VUE_APP_API,
    };
  },
  methods: {
    getIcon(rank) {
      if (rank === 1 || rank === 2 || rank === 3) {
        return 'mdi-medal';
      }
      return '';
    },
    getAwardColor(rank) {
      if (rank === 1) {
        return '#d4af37';
      } if (rank === 2) {
        return '#8a9597';
      } if (rank === 3) {
        return '#cc8e34';
      }
      return '';
    },
    getCallHighscoreService() {
      this.loading = true;
      axios.get(`${this.API_URL}basic/highscore/`)
        .then((response) => {
          this.items = response.data;
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;
          this.responseObj = error;
          this.showError = true;
        });
    },
  },
  computed: {
    gerOrdered() {
      return this._.sortBy(this.items, ['highscore']).reverse();
    },
  },
  created() {
    this.getCallHighscoreService();
  },
};
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #f2f2f2;
}
th {
  font-size: 13px !important;
}
</style>

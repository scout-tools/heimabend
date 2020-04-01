<template>
  <v-container>
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
              <tr v-for="(item, index) in items" :key="item.name">
                <td class="text-left">{{ index + 1 }}</td>
                <td class="text-left">{{ item.name }}</td>
                <td class="text-left">{{ item.count }}</td>
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
export default {
  data() {
    return {
      items: [
        {
          name: 'Robert',
          count: 23,
        },
        {
          name: 'Dorothea',
          count: 10,
        },
        {
          name: 'Sheldon',
          count: 8,
        },
        {
          name: 'Jan',
          count: 6,
        },
      ],
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
  },
};
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #f2f2f2;
}
th {
  font-size: 16px !important;
}
</style>

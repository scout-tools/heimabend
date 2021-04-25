<template>
  <v-tabs vertical icons-and-text>
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      Experiment
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <experiment />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import Experiment from './experiment/Main.vue';

export default {
  components: {
    Experiment,
  },
};
</script>

<template>
  <v-tabs vertical icons-and-text>
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      KPI
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <kpi />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import Kpi from './kpi/Main.vue';

export default {
  components: {
    Kpi,
  },
};
</script>

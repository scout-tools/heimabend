<template>
  <v-tabs
    icons-and-text
    vertical
  >
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      Tabelle
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      Aufrufe
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <admin-event />
        </v-card-text>
      </v-card>
    </v-tab-item>

    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <most-views />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import AdminEvent from '@/views/admin/heimabend/editor/AdminEvent.vue';
import MostViews from '@/views/admin/heimabend/mostViews/MostViews.vue';

export default {
  components: {
    MostViews,
    AdminEvent,
  },
};
</script>

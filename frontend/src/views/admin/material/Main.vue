<template>
  <v-tabs vertical icons-and-text>
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      Gegenstand
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      Einheiten
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <NameMain />
        </v-card-text>
      </v-card>
    </v-tab-item>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <UnitMain />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import NameMain from './name/List.vue';
import UnitMain from './unit/List.vue';

export default {
  components: {
    NameMain,
    UnitMain,
  },
};
</script>

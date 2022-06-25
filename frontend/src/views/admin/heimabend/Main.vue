<template>
  <v-tabs
    :icons-and-text="!isMobil"
    vertical
  >
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      {{ isMobil ? '' : 'Tabelle' }}
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      {{ isMobil ? '' : 'Aufrufe' }}
    </v-tab>
    <v-tab>
      <v-icon left> mdi-party-popper </v-icon>
      {{ isMobil ? '' : 'Der Woche' }}
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

    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <event-of-the-week />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import AdminEvent from '@/views/admin/heimabend/editor/AdminEvent.vue';
import MostViews from '@/views/admin/heimabend/mostViews/MostViews.vue';
import EventOfTheWeek from '@/views/admin/heimabend/eventOfTheWeek/List.vue';

export default {
  components: {
    MostViews,
    AdminEvent,
    EventOfTheWeek,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
  },
};
</script>

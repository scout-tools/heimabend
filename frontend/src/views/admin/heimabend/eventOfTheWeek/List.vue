<template>
  <v-container fluid>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="filteredItems"
      show-select
      single-select
      hide-default-footer
      disable-pagination
      :loading="loading"
      loading-text="Wir suchen die Daten für dich raus."
      no-data-text="Es existiert noch kein Eintrag."
    >
      <template v-slot:item.releaseDate="{ item }">
        {{ moment(item.releaseDate).format('DD.MM.YYYY') }}
      </template>
      <template v-slot:item.history="{ item }">
        <v-simple-checkbox
          v-model="item.history"
          disabled
        ></v-simple-checkbox>
      </template>
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title> Heimabend der Woche</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-switch
            v-model="history"
            label="Vergangenheit"
          ></v-switch>
          <v-spacer />
          <v-btn tile class="ma-3" color="success" @click="onNewClicked">
            <v-icon left> mdi-plus </v-icon>
            Neu
          </v-btn>
          <!-- <v-btn
            tile
            :disabled="!selected.length"
            class="ma-3"
            color="lightblue"
            @click="openViewNewTab"
          >
            <v-icon left> mdi-eye </v-icon>
            Heima. anzeigen
          </v-btn>
          <v-btn
            tile
            :disabled="!selected.length"
            class="ma-3"
            color="warning"
            @click="openEditNewTab"
          >
            <v-icon left> mdi-pencil </v-icon>
            Heima bearb.
          </v-btn> -->
          <v-btn
            tile
            :disabled="!selected.length"
            class="ma-3"
            color="error"
            @click="onDeleteClick"
          >
            <v-icon left> mdi-delete </v-icon>
            Löschen
          </v-btn>
        </v-toolbar>
      </template>
    </v-data-table>
    <DeleteModual @refresh="refresh" ref="deleteAnfoModual" />
  </v-container>
</template>

<script>
import moment from 'moment'; // eslint-disable-line
import DeleteModual from '@/components/dialog/DeleteModal.vue'; // eslint-disable-line
import axios from 'axios'; // eslint-disable-line

export default {
  components: {
    DeleteModual,
  },
  data() {
    return {
      loading: true,
      items: [],
      API_URL: process.env.VUE_APP_API,
      selected: [],
      history: false,
      headers: [
        { text: 'Erscheinungsdatum', value: 'releaseDate' },
        { text: 'Titel', value: 'eventObj.title' },
        { text: 'Autor', value: 'eventObj.createdBy' },
        { text: 'Vergangenheit', value: 'history' },
        { text: 'Kommentar', value: 'comment' },
      ],
    };
  },
  computed: {
    filteredItems() {
      const items = this.items.filter(item => item.history === this.history || this.history);
      return items;
    },
  },
  methods: {
    refresh() {
      this.getEventOfTheWeek();
    },
    getEventOfTheWeek() {
      this.loading = true;
      axios
        .get(
          `${
            this.API_URL
          }basic/event-of-the-week/?&timestamp=${new Date().getTime()}`,
        )
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
    onNewClicked() {
      this.$router.push({ name: 'admin-heimabend-event-of-the-week-create' });
    },
    onOpenClick() {},
    onDeleteClick() {
      const { id } = this.selected[0];
      debugger;
      this.$refs.deleteAnfoModual.show(id);
    },
    openViewNewTab() {
      const { event } = this.selected[0];
      const routeData = this.$router.resolve({
        name: 'heimabendDetails',
        params: { event },
      });
      debugger;
      window.open(routeData.href, '_blank').focus();
    },
    openEditNewTab() {
      const { event } = this.selected[0];
      const routeData = this.$router.resolve({
        name: 'heimabendUpdate',
        params: { event },
      });
      debugger;
      window.open(routeData.href, '_blank').focus();
    },
  },
  created() {
    this.getEventOfTheWeek();
  },
};
</script>

<style scoped>
</style>

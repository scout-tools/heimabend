<template>
  <v-container>
    <v-row justify="center">
      <v-card class="py-5">
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-search"
            label="Suche"
            single-line
            hide-details
          />
          <v-spacer />
          <v-btn color="green" dark @click="onNewClicked()" class="mb-2">
            Neuer Tag
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="getItems"
            :search="search"
            :items-per-page="itemsPerPage"
            disable-pagination
            hide-default-footer
          >
            <template v-slot:item.isPublic="{ item }">
              <v-simple-checkbox
                v-model="item.isPublic"
                disabled
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.isHeader="{ item }">
              <v-simple-checkbox
                v-model="item.isHeader"
                disabled
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.isMandatory="{ item }">
              <v-simple-checkbox
                v-model="item.isMandatory"
                disabled
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.isEventOverview="{ item }">
              <v-simple-checkbox
                v-model="item.isEventOverview"
                disabled
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.action="{ item }">
              <v-icon class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
              <v-icon @click="deleteItem(item)"> mdi-delete </v-icon>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-row>
    <v-snackbar v-model="showError" color="error" y="top" :timeout="timeout">
      {{ 'Es ist ein Fehler adasdasufgetreten' }}
    </v-snackbar>
    <create-update ref="createUpdateModal" @dialogClose="onRefresh" />

    <delete-modal ref="deleteModal" @refresh="onRefresh" />
  </v-container>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

import CreateUpdate from './CreateUpdateModal.vue';
import DeleteModal from './DeleteModal.vue';

export default {
  components: {
    CreateUpdate,
    DeleteModal,
  },

  data: () => ({
    items: [],
    search: '',
    timeout: 3000,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Icon', value: 'icon' },
      { text: 'Reihenf.', value: 'sorting' },
      { text: 'Sichtbar', value: 'isPublic' },
      { text: 'Kopfzeile', value: 'isHeader' },
      { text: 'Pflicht', value: 'isMandatory' },
      { text: 'Übersicht', value: 'isEventOverview' },
      { text: 'Aktion', value: 'action', sortable: false },
    ],
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    itemsPerPage: 30,
    data: {},
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
    ...mapGetters(['tags', 'tagCategory', 'isAuthenticated']),
    getItems() {
      return this.items;
    },
  },

  methods: {
    getNewItems() {
      const path = `${
        this.API_URL
      }basic/tag-category?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {});
    },
    onNewClicked() {
      this.$refs.createUpdateModal.show();
    },
    onRefresh() {
      this.items = [];
      this.getNewItems();
    },
    editItem(item) {
      this.$refs.createUpdateModal.show(item);
    },
    deleteItem(item) {
      this.$refs.deleteModal.show(item);
    },
    show(item) {
      this.dialog = true;
      if (item) {
        this.isCreate = false;
        this.isUpdate = true;
        this.data = item;
      } else {
        this.isCreate = true;
        this.isUpdate = false;
      }
    },

    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },

    save() {
      this.formSubmit();
    },
  },
  created() {
    this.getNewItems();
  },
};
</script>

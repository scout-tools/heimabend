<template>
  <v-container>
    <v-row justify="center">
      <v-card>
        <v-card-title>
          <Searchfield
            :search="search"
            @onNewClicked="onNewClicked"
          />
        </v-card-title>
        <v-data-table
          class="test-1"
          :headers="headers"
          :items="getData"
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
          <template v-slot:item.isComment="{ item }">
            <v-simple-checkbox
              v-model="item.isComment"
              disabled
            ></v-simple-checkbox>
          </template>
          <template v-slot:item.action="{ item }">
            <v-icon @click="editItem(item)"> mdi-pencil </v-icon>
            <v-icon @click="deleteItem(item)"> mdi-delete </v-icon>
          </template>
        </v-data-table>
      </v-card>
    </v-row>
    <v-snackbar v-model="showError" color="error" y="top" :timeout="timeout">
      {{ 'Es ist ein Fehler adasdasufgetreten' }}
    </v-snackbar>
    <create-update-modal ref="createUpdateModal" @dialogClose="onRefresh" />
    <delete-modal ref="deleteModal" @refresh="onRefresh" />
  </v-container>
</template>

<script>
import axios from 'axios';

import Searchfield from '@/components/field/SearchField.vue';
import CreateUpdateModal from './CreateUpdateModal.vue';
import DeleteModal from './DeleteModal.vue';

import { serviceMixin } from '@/mixins/serviceMixin.js'; // eslint-disable-line

export default {
  mixins: [serviceMixin],
  components: {
    CreateUpdateModal,
    DeleteModal,
    Searchfield,
  },

  data: () => ({
    items: [],
    search: '',
    timeout: 3000,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Beschreibung', value: 'description' },
      { text: 'isPublic', value: 'isPublic' },
      { text: 'Aktion', value: 'action', sortable: false },
    ],
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    itemsPerPage: 1000,
    isCreate: true,
    isUpdate: false,
    serviceName: 'material-name',
  }),

  computed: {
    getData() {
      return this.items;
    },
  },
  methods: {
    onNewClicked() {
      this.$refs.createUpdateModal.show(null, this.serviceName);
    },
    onRefresh() {
      this.items = [];
      this.getItems(this.serviceName);
    },
    editItem(item) {
      this.$refs.createUpdateModal.show(item, this.serviceName);
    },
    deleteItem(item) {
      this.$refs.deleteModal.show(item, this.serviceName);
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
    submit() {
      this.saveMessage();
    },
    saveMessage() {
      axios
        .post(`${this.API_URL}basic/message/`, {
          createdBy: this.data.createdBy,
          createdByEmail: this.data.createdByEmail,
          messageType: this.data.messageType,
          messageBody: this.data.messageBody,
          eventId: this.eventId,
        })
        .then(() => {
          this.$router.push({ name: 'overview' });
          this.showSuccess = true;
        })
        .catch((error) => {
          this.responseObj = JSON.stringify(error.response.data);
          this.showError = true;
        });
    },
  },
  created() {
    this.getItems(this.serviceName);
  },
};
</script>

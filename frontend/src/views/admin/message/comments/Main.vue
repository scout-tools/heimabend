<template>
  <v-container fluid>
    <v-row justify="center">
      <v-data-table
        :headers="headers"
        :items="getItems"
        :items-per-page="itemsPerPage"
        :expanded.sync="expanded"
        hide-default-footer
        show-expand
      >
        <template v-slot:item.createdAt="{ item }">
          {{
            moment(item.createdAt).format('DD.MM.YYYY')
          }}
        </template>
        <template v-slot:item.isPublic="{ item }">
          <v-icon :color="item.isPublic ? 'green' : 'red'">
            {{
              item.isPublic ? 'mdi-check-circle' : 'mdi-close-circle'
            }}</v-icon
          >
        </template>
        <template v-slot:item.isProcessed="{ item }">
          <v-icon :color="item.isProcessed ? 'green' : 'red'">
            {{
              item.isProcessed ? 'mdi-check-circle' : 'mdi-close-circle'
            }}</v-icon
          >
        </template>
        <template v-slot:item.action="{ item }">
          <ActionButtonMenu
            :data="item"
          />
        </template>
        <template v-slot:expanded-item="{ item }">
          <td :colspan="headers.length">
            <v-card flat class="ma-2">
              <v-textarea
                class="ma-2"
                readonly
                label="Text"
                auto-grow
                v-model="item.messageBody"
              >
              </v-textarea>
            </v-card>
          </td>
        </template>
      </v-data-table>
    </v-row>
    <delete-modal ref="deleteMessageModal" />
  </v-container>
</template>
<script>
import axios from 'axios';
import moment from 'moment'; // eslint-disable-line

import DeleteModal from './components/DeleteModal.vue';
import ActionButtonMenu from './components/ActionButtonMenu.vue';

export default {
  components: {
    DeleteModal,
    ActionButtonMenu,
  },

  data: () => ({
    messages: [],
    search: '',
    timeout: 3000,
    expanded: [],
    headers: [
      { text: 'Datum', value: 'createdAt' },
      { text: 'Name', value: 'createdBy' },
      { text: 'isPublic', value: 'isPublic' },
      { text: 'isProcessed', value: 'isProcessed' },
      { text: 'Thema', value: 'messageType' },
      { text: 'Heimabend', value: 'event' },
      { text: 'Ansicht', value: 'action', sortable: false },
      { text: '', value: 'data-table-expand' },
    ],
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    responseObj: null,
    itemsPerPage: 30,
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getItems() {
      return this.messages.filter(item => item.event !== null);
    },
  },

  methods: {
    getMessages() {
      const path = `${
        this.API_URL
      }basic/message?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.showSuccess = true;
          this.messages = res.data;
        })
        .catch(() => {
          this.showError = true;
        });
    },
    onRefreshMessages() {
      this.messages = [];
      this.getMessages();
    },
    show(item) {
      this.$refs.messageModal.show(item);
    },
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
    deleteItem(item) {
      this.$refs.deleteMessageModal.show(item);
    },
  },
  created() {
    this.getMessages();
  },
};
</script>

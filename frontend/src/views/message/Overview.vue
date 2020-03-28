<template>
<v-container>
  <v-row justify="center">
    <v-flex ma-3 lg7>
        <v-data-table
          :headers="headers"
          :items="getItems"
          :items-per-page="itemsPerPage"
        >
        <template v-slot:item.action="{ item }">
          <v-icon
            class="mr-2"
            @click="show(item)"
          >
            mdi-eye
          </v-icon>
          <v-icon
            @click="deleteItem(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
      <ViewMessageDialog
        ref="messageModal"
      />
    </v-flex>
  </v-row>
  <DeleteModal
    ref="deleteMessageModal"
  />
</v-container>
</template>
<script>
import axios from 'axios';

import ViewMessageDialog from './ViewMessageDialog.vue'; // eslint-disable-line
import DeleteModal from './DeleteModal.vue';

export default {
  components: {
    ViewMessageDialog,
    DeleteModal,
  },

  data: () => ({
    messages: [],
    search: '',
    timeout: 3000,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'E-Mail', value: 'email' },
      { text: 'Thema', value: 'topic' },
      { text: 'Ansicht', value: 'action', sortable: false },
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
      return this.messages;
    },
  },

  methods: {
    getMessages() {
      const path = `${this.API_URL}basic/message/`;
      axios.get(path)
        .then((res) => {
          this.messages = res.data;
        })
        .catch(() => {
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

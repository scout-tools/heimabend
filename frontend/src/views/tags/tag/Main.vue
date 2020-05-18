<template>
<v-container>
  <v-row justify="center">
    <v-flex ma-3 lg7>
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-search"
          label="Suche"
          single-line
          hide-details
        />
        <v-spacer/>
        <v-btn
          color="green"
          dark
          @click="onNewClicked()"
          class="mb-2"
        >
          Neuer Tag
        </v-btn>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="getItems"
          :search="search"
          :items-per-page="itemsPerPage"
          disable-pagination
          hide-default-footer
        >
        <template v-slot:item.color="{ item }">
          <v-chip
            :color="item.color"
          >
            {{ item.color }}
          </v-chip>
        </template>

        <template v-slot:item.categoryId="{ item }">
          {{ getCategoryName(item.categoryId) }}
        </template>
        <template v-slot:item.action="{ item }">
          <v-icon
            small
            @click="editItem(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="deleteItem(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-card>
    </v-flex>
  </v-row>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
      :timeout="timeout"
    >
      {{ 'Es ist ein Fehler adasdasufgetreten' }}
    </v-snackbar>
  <CreateUpdateModal
    ref="createUpdateModal"
    @dialogClose="onRefresh"
  />
  <DeleteModal
    ref="deleteModal"
    @refresh="onRefresh"
  />
  </v-container>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

import CreateUpdateModal from './CreateUpdateModal.vue';
import DeleteModal from './DeleteModal.vue';


export default {
  components: {
    CreateUpdateModal,
    DeleteModal,
  },

  data: () => ({
    items: [],
    search: '',
    timeout: 3000,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Beschreibung', value: 'description' },
      { text: 'Farbe', value: 'color' },
      // { text: 'Wie oft verwendet?', value: 'tag_count' },
      { text: 'Kategorie', value: 'categoryId' },
      { text: 'Sichtbar?', value: 'is_visible' },
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
    ...mapGetters([
      'tags',
      'tagCategory',
      'isAuthenticated',
    ]),
    getItems() {
      // eslint-disable-next-line arrow-parens
      this.items.forEach(element => {
        // eslint-disable-next-line no-param-reassign
        element.categoryId = this.convertUrlToId(element.category);
      });
      return this.items;
    },
  },

  methods: {
    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    getNewItems() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {
        });
    },
    getCategoryName(categoryId) {
      if (categoryId) {
        return this.tagCategory.filter(item => item.id === categoryId)[0].name;
      }
      return '-';
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

<style scoped>
</style>

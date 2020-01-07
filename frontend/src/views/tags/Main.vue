<template>
<div>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      fullscreen
      hide-overlay
      transition="dialog-top-transition"
    >
      <v-card>
       <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Themen</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              dark
              text
              @click="cancel" >
                Fertig
              </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
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
                @click="onNewTag()"
                class="mb-2"
              >
                Neuer Tag
              </v-btn>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="getItems"
                :search="search"
              >
              <template v-slot:item.color="{ item }">
                <v-chip
                  :color="item.color"
                >
                  {{ item.color }}
                </v-chip>
              </template>
              <template v-slot:item.action="{ item }">
                <v-icon
                  class="mr-2"
                  @click="editItem(item)"
                >
                  mdi-pencil
                </v-icon>
                <v-icon
                  @click="deleteItem(item)"
                >
                  mdi-delete
                </v-icon>
              </template>
            </v-data-table>
          </v-card>
        </v-card-text>
      </v-card>
    </v-dialog>
    <ErrorMessage
      :showError="showError"
      :responseObj="responseObj"
    />
    <SuccessMessage
      :showSuccess="showSuccess"/>
  </v-row>
  <CreateUpdateTag
    ref="createTagModal"
    @dialogClose="onRefreshTags"
  />
  <DeleteModal
    ref="deleteTagModal"
    @refresh="onRefreshTags"
  />
  </div>
</template>

<script>
import axios from 'axios';

import ErrorMessage from '@/views/components/common/ErrorMessage.vue'; //eslint-disable-line
import SuccessMessage from '@/views/components/common/SuccessMessage.vue'; //eslint-disable-line
import CreateUpdateTag from './CreateUpdateTag.vue';
import DeleteModal from './DeleteModal.vue';


export default {
  components: {
    ErrorMessage,
    SuccessMessage,
    CreateUpdateTag,
    DeleteModal,
  },

  data: () => ({
    tags: [],
    search: '',
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Beschreibung', value: 'description' },
      { text: 'Farbe', value: 'color' },
      { text: 'Aktion', value: 'action', sortable: false },
    ],
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    responseObj: null,
    data: {
      title: 'Rucksack packen',
      description: '',
      isPossibleOutside: true,
      isPossibleInside: false,
      tags: [],
      material: '',
      costsRating: 1,
      executionTimeRating: 1,
      isPrepairationNeeded: true,
      isActive: false,
      createdBy: null,
      updatedBy: null,
      updatedAt: null,
      isLvlOne: true,
      isLvlTwo: true,
      isLvlThree: true,
    },
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getItems() {
      return this.tags;
    },
  },

  methods: {
    getTags() {
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          this.tags = res;
        })
        .catch(() => {
        });
    },
    onNewTag() {
      this.$refs.createTagModal.show();
    },
    onRefreshTags() {
      this.tags = [];
      this.getTags();
    },
    editItem(item) {
      this.$refs.createTagModal.show(item);
    },
    deleteItem(item) {
      this.$refs.deleteTagModal.show(item);
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
    this.getTags();
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
</style>

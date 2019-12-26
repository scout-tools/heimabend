<template>
<div>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Kategorie löschen</v-card-title>

        <v-card-text>
          Willst du echt diese Kategorie löschen?
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="grey darken-1"
            text
            @click="cancel()"
          >
            Abbrechen
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="onDeleteClick()"
          >
            Löschen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
      <ErrorMessage
      :showError="showError"
      :responseObj="responseObj"
    />
    <SuccessMessage
      :showSuccess="showSuccess"/>
</div>
</template>

<script>
import axios from 'axios';

import ErrorMessage from '@/views/components/common/ErrorMessage.vue'; // eslint-disable-line
import SuccessMessage from '@/views/components/common/SuccessMessage.vue'; // eslint-disable-line


export default {
  props: ['tags'],

  components: {
    ErrorMessage,
    SuccessMessage,
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    showError: false,
    showSuccess: false,
    responseObj: null,
    data: {
      id: null,
      name: null,
      description: null,
      color: null,
    },
    isCreate: true,
    isUpdate: false,
    levelFilter: [0, 1, 2],
  }),

  computed: {
  },

  methods: {
    onDeleteClick() {
      axios.delete(`${this.API_URL}basic/tag/${this.data.id}/`)
        .then(() => {
          this.dialog = false;
          this.$emit('dialogClose');
          this.$emit('refresh');
          this.showSuccess = true;
        })
        .catch(() => {
          this.showError = true;
        });
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
  },
};
</script>

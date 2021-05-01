<template>
<v-container fluid ma-3>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      hide-overlay
      max-width="50%">
      <v-card>
       <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title v-if="isCreate">Neu</v-toolbar-title>
          <v-toolbar-title v-if="isUpdate">Änderung</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              dark
              text
              @click="save()" >
                Speichern
              </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
          <v-form
              ref="form"
              v-model="valid"
            >
          <v-container class="pa-4">
            <v-row>
                <v-text-field
                  autofocus
                  :counter="40"
                  :rules="rules.name"
                  name="123"
                  label="Name"
                  v-model="data.name"
                  required>
                </v-text-field>
            </v-row>
            <v-row>
                <v-textarea
                  label="Beschreibung"
                  :counter="1000"
                  auto-grow
                  :rules="rules.description"
                  v-model="data.description"
                  required
                ></v-textarea>
            </v-row>
              <v-row>
                  <v-switch
                    label="Öffentlicht?"
                    color="secondary"
                    v-model="data.isPublic"
                    hide-details
                    indeterminate
                  />
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
      :timeout="timeout"
    >
      {{ 'Fehler' }}
    </v-snackbar>
    <v-snackbar
      v-model="showSuccess"
      color="success"
      y='top'
      :timeout="timeout"
    >
      {{ 'Erfolgreich gespeichert' }}
    </v-snackbar>
  </v-row>
</v-container>
</template>

<script>
import axios from 'axios';

export default {

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    valid: true,
    showError: false,
    showSuccess: false,
    timeout: 3000,
    responseObj: null,
    hideCanvas: false,
    hideInputs: true,
    hideModeSwitch: true,
    showSwatches: false,
    rules: {
      name: [
        v => !!v || 'Titel ist erforderlich',
      ],
      description: [
      ],
    },
    data: {
      name: 'hallo',
      description: '',
    },
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
  },

  methods: {
    formSubmit() {
      if (!this.$refs.form.validate()) {
        return;
      }
      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/${this.serviceName}/`, {
          name: this.data.name,
          icon: this.data.icon,
          description: this.data.description,
          sorting: this.data.sorting,
          isPublic: this.data.isPublic,
          isHeader: this.data.isHeader,
          isMandatory: this.data.isMandatory,
          isEventOverview: this.data.isEventOverview,
        })
          .then(() => {
            this.dialog = false;
            this.$emit('dialogClose');
            this.showSuccess = true;
          })
          .catch(() => {
            this.showError = true;
          });
      } else if (this.isUpdate) {
        axios.put(`${this.API_URL}basic/${this.serviceName}/${this.data.id}/`, {
          name: this.data.name,
          icon: this.data.icon,
          description: this.data.description,
          sorting: this.data.sorting,
          isPublic: this.data.isPublic,
          isHeader: this.data.isHeader,
          isMandatory: this.data.isMandatory,
          isEventOverview: this.data.isEventOverview,
        })
          .then(() => {
            this.dialog = false;
            this.$emit('dialogClose');
            this.showSuccess = true;
          })
          .catch(() => {
            this.showError = true;
          });
      }
    },
    show(item, serviceName) {
      this.serviceName = serviceName;
      this.dialog = true;
      if (item) {
        this.isCreate = false;
        this.isUpdate = true;
        this.data = item;
      } else {
        this.isCreate = true;
        this.isUpdate = false;
        this.data = {
          isPublic: false,
        };
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
};
</script>

<style scoped>
</style>

<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      hide-overlay
      max-width="70%">
      <v-card>
       <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title v-if="isCreate">Neue Kategorie</v-toolbar-title>
          <v-toolbar-title v-if="isUpdate">Kategorie ändern</v-toolbar-title>
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
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  outlined
                  autofocus
                  :counter="40"
                  :rules="rules.name"
                  name="123"
                  label="Name"
                  v-model="data.name"
                  required>
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-textarea
                  outlined
                  label="Beschreibung"
                  :counter="2500"
                  auto-grow
                  :rules="rules.description"
                  v-model="data.description"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                  <v-color-picker
                    label="Farbe"
                    :hide-canvas="hideCanvas"
                    :hide-inputs="hideInputs"
                    :hide-mode-switch="hideModeSwitch"
                    :show-swatches="showSwatches"
                    class="mx-auto"
                    :rules="rules.color"
                    v-model="data.color"
                  ></v-color-picker>
                </v-col>
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
      {{ 'Der Tag wurde erfolgreich gespeichert' }}
    </v-snackbar>
  </v-row>
</template>

<script>
import axios from 'axios';

export default {
  props: ['tags'],


  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    valid: true,
    showError: false,
    showSuccess: false,
    timeout: 3000,
    responseObj: null,
    color: '#8E00FF',
    hideCanvas: false,
    hideInputs: true,
    hideModeSwitch: true,
    mode: 'hex',
    modes: ['rgba', 'hsla', 'hexa'],
    showSwatches: false,
    rules: {
      name: [
        v => !!v || 'Titel ist erforderlich',
        v => (v && v.length >= 2) || 'Name must be more than 10 characters',
        v => (v && v.length <= 15) || 'Name must be less than 40 characters',
      ],
      description: [
      ],
      color: [
        v => (v.length <= 7) || 'Name must be less than 200 characters',
      ],
    },
    data: {
      name: 'Rucksack packen',
      description: '',
      color: '#ffffff',
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
        axios.post(`${this.API_URL}basic/tag/`, {
          name: this.data.name,
          description: this.data.description,
          color: this.data.color.hex,
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
        axios.put(`${this.API_URL}basic/tag/${this.data.id}/`, {
          name: this.data.name,
          description: this.data.description,
          color: this.data.color,
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
    onDeleteClick() {
      axios.delekte(`${this.API_URL}basic/tag/${this.data.id}/`)
        .then(() => {
          this.dialog = false;
          this.$emit('dialogClose');
          this.showSuccess = true;
        })
        .catch(() => {
          this.showError = true;
        });
    },
    getUrlTagList(tagList) {
      const ary = [];
      tagList.forEach((tag) => {
        ary.push(`${process.env.VUE_APP_API}basic/tag/${tag}/`);
      });
      return ary;
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
        this.data = [];
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
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(40, 158, 40)
}
</style>

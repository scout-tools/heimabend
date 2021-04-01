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
              <v-col cols="6">
                <v-textarea
                  outlined
                  label="Beschreibung"
                  :counter="1000"
                  auto-grow
                  :rules="rules.description"
                  v-model="data.description"
                  required
                ></v-textarea>
              </v-col>
              <v-col cols="6">
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
            <v-row>
              <v-col cols="6">
                <v-text-field
                  outlined
                  label="Reihenfolge"
                  :rules="rules.ordered_id"
                  v-model="data.ordered_id"
                  required
                  ></v-text-field>
                </v-col>
              </v-row>
            <v-row>
              <v-col cols="6">
                <v-select
                  :items="tagCategory"
                  return-object
                  hide-details
                  item-value="id"
                  item-text="name"
                  outlined
                  v-model="data.categoryId"
                  :rules="rules.categoryId"
                  label="Tag Kategory"
                  required
                />
              </v-col>
             <v-col cols="6">
                <v-switch
                  label="Sichtbar?"
                  color="secondary"
                  v-model="data.is_visible"
                  hide-details
                  dense
                  indeterminate
                >
                </v-switch>
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
  props: ['item'],


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
        v => (v && v.length >= 3) || 'Muss mehr als 3 Zeichen haben.',
        v => (v && v.length <= 20) || 'Muss weniger als 21 Zeichen haben',
      ],
      description: [
      ],
      color: [
        v => (v.length === 7) || 'Sieben Zeichen',
      ],
      categoryId: [
        v => !!v || 'Kategorie ist erforderlich',
      ],
    },
    data: {
      name: 'Rucksack packen',
      description: '',
      category: 3,
      ordered_id: null,
    },
    isCreate: true,
    isUpdate: false,
  }),

  computed: {
    tagCategory() {
      return this.$store.getters.tagCategory;
    },
    parsedCategory() {
      const link = this.data.category;
      return link;
    },
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
          category: this.data.categoryId.id,
          is_visible: this.data.is_visible,
          ordered_id: this.data.ordered_id,
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
          category: this.data.categoryId,
          is_visible: this.data.is_visible,
          ordered_id: this.data.ordered_id,
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

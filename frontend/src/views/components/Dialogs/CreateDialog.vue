<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-top-transition">
      <v-card >
      <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title v-if="isCreate">Neuer Heimabend</v-toolbar-title>
          <v-toolbar-title v-if="isUpdate">Heimabend ändern</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark text @click="save()" >Speichern</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="4">
                <v-text-field
                  outlined
                  label="Titel"
                  v-model="data.title"
                  required>
                </v-text-field>
              </v-col>
              <v-col cols="8">
                <v-textarea
                  outlined
                  label="Beschreibung"
                  v-model="data.beschreibung"
                ></v-textarea>
              </v-col>
              <v-col cols="4">
                <v-textarea
                  outlined
                  label="Material Liste"
                  required
                  v-model="data.material"
                ></v-textarea>
              </v-col>
              <v-col cols="3">
                <v-select
                    v-model="data.tags"
                    :items="tags"
                    item-value="id"
                    item-color="color"
                    item-text="name"
                    deletable-chips
                    chips
                    label="Themen"
                    multiple
                    outlined
                  ></v-select>
              </v-col>
              <v-col cols="2">
                <v-sheet class="pa-3">
                  <v-switch v-model="data.isPossibleInside" label="Drinnen möglich?"></v-switch>
                  <v-switch v-model="data.isPossibleOutside" label="Draußen möglich?"></v-switch>
                </v-sheet>
              </v-col>
              <v-col cols="2">
                <v-sheet class="pa-3">
                <v-text>
                  Wieviel Geld ist nötig?
                </v-text>
                <v-rating
                  v-model="data.costsRating"
                  emptyIcon="mdi-currency-eur"
                  fullIcon="mdi-currency-eur"
                  color="orange"
                  background-color="grey"
                  min="1"
                  length="3"
                ></v-rating>
                <v-text>
                  Wieviel Vorbereitungszeit ist nötig?
                </v-text>
                <v-rating
                  v-model="data.prepairationRating"
                  emptyIcon="mdi-clock"
                  fullIcon="mdi-clock"
                  color="red"
                  background-color="grey"
                  min="1"
                  length="3"
                ></v-rating>
                </v-sheet>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from 'axios';

export default {
  props: ['tags'],

  data: () => ({
    dialog: false,
    data: [],
    isCreate: true,
    isUpdate: false,
  }),

  methods: {
    formSubmit() {
      const currentObj = this;
      if (this.isCreate) {
        debugger;
        axios.post('http://localhost:8000/basic/event/', {
          title: this.data.title,
          beschreibung: this.data.beschreibung,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          prepairationRating: this.data.prepairationRating,
        })
          .then(() => {
            debugger;
            // console.log(response);
            this.$emit('dialogClose');
          })
          .catch((error) => {
            debugger;
            currentObj.output = error;
          });
      } else if (this.isUpdate) {
        axios.put('http://localhost:5000/ringMember', {
          id: this.data.id,
          title: this.data.title,
          beschreibung: this.data.beschreibung,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          prepairationRating: this.data.prepairationRating,
        })
          .then(() => {
            debugger;
            // console.log(response);
            this.$emit('dialogClose');
          })
          .catch((error) => {
            currentObj.output = error;
          });
      }
    },
    getUrlTagList(tagList) {
      const ary = [];
      tagList.forEach((tag) => {
        ary.push(`http://localhost:8000/basic/tag/${tag}/`);
      });
      debugger;
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
      this.dialog = false;
    },
  },
};
</script>

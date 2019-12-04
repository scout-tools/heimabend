<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-top-transition">
      <v-card >
      <v-toolbar dark color="primary">
          <v-btn icon dark @click="cancel()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title v-if="isCreate">Über das Projekt</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-container>
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

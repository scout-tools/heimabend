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
          <v-toolbar-title v-if="isCreate">Neuer Heimabend</v-toolbar-title>
          <v-toolbar-title v-if="isUpdate">Heimabend ändern</v-toolbar-title>
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
      <v-checkbox
        color="secondary"
        v-model="isAuthenticated"
        :rules="[v => !!v || 'Nur mit der Einverständniserklärung kannst du Ideen einreichen']"
        label="Ich möchte meine Heimabend veröffentlichen und es
          dürfen in Zukunft andere Änderungen an der Idee vornehmen?"
        required
      ></v-checkbox>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  outlined
                  autofocus
                  :counter="40"
                  :rules="rules.title"
                  name="123"
                  label="Titel"
                  v-model="data.title"
                  required>
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-textarea
                  outlined
                  label="Beschreibung"
                  :counter="2000"
                  auto-grow
                  :rules="rules.description"
                  v-model="data.description"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  outlined
                  label="Material Liste"
                  :counter="200"
                  required
                  :rules="rules.material"
                  v-model="data.material"
                ></v-text-field>
              </v-col>
           </v-row>
            <v-row>
              <v-col cols="3">
                <v-sheet class="pa-3">
                  <v-switch
                    v-model="data.isPossibleInside"
                    color="secondary"
                    label="Drinnen möglich?">
                  </v-switch>
                  <v-switch
                    v-model="data.isPossibleOutside"
                    color="secondary"
                    label="Draußen möglich?">
                  </v-switch>
                  <v-switch
                    v-model="data.isPrepairationNeeded"
                    color="secondary"
                    label="Vorbereitung nötig?">
                  </v-switch>
                </v-sheet>
              </v-col>
              <v-col cols="3" class="mt-5">
                <v-select
                    v-model="data.tags"
                    :items="tags"
                    item-value="id"
                    item-color="color"
                    :rules="rules.tags"
                    item-text="name"
                    deletable-chips
                    chips
                    label="Themen"
                    multiple
                    outlined
                  ></v-select>
              </v-col>
              <v-col cols="3">
                <v-sheet class="pa-3">
                <span class="subtitle-1">
                  Wieviel Geld ist nötig?
                </span>
                <v-rating
                  v-model="data.costsRating"
                  emptyIcon="mdi-currency-eur"
                  fullIcon="mdi-currency-eur"
                  color="orange"
                  background-color="grey"
                  min="1"
                  length="3"
                ></v-rating>
                <span class="subtitle-1">
                  Wieviel Durchführungszeit ist erforderlich?
                </span>
                <v-rating
                  v-model="data.executionTimeRating"
                  emptyIcon="mdi-clock"
                  fullIcon="mdi-clock"
                  color="black"
                  background-color="grey"
                  min="1"
                  length="3"
                ></v-rating>
                </v-sheet>
              </v-col>
              <v-col cols="3" class="mt-5">
                <v-text-field
                  v-if="!isAuthenticated || isUpdate"
                  outlined
                  label="Dein Name"
                  v-model="data.createdBy"
                  :disabled="isUpdate"
                  :rules="rules.createdBy"
                  required>
                </v-text-field>
                <v-text-field
                  v-if="!isAuthenticated || isUpdate"
                  outlined
                  label="Deine E-Mail Adresse"
                  :disabled="isAuthenticated"
                  v-model="data.createdByEmail"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
               <v-col cols="3">
                <v-sheet class="pa-3">
                <span class="subtitle-1">
                  Für welche Erfahrung ist der Heimabend geeignet?
                </span>
                <v-btn-toggle
                  v-model="levelFilter"
                  multiple
                  shaped
                  mandatory
                >
                  <v-btn>
                    <v-img
                      v-if="getOrange"
                      class="mx-1"
                      :src="require('../../../assets/knot_orange.png')"
                      max-width="40"
                    />
                    <v-img
                      v-if="!getOrange"
                      class="mx-1"
                      :src="require('../../../assets/knot_grey.png')"
                      max-width="40"
                    ></v-img>
                  </v-btn>
                  <v-btn>
                    <v-img
                      v-if="getBlue"
                      class="mx-1"
                      :src="require('../../../assets/knot_blue.png')"
                      max-width="40"
                    ></v-img>
                    <v-img
                      v-if="!getBlue"
                      class="mx-1"
                      :src="require('../../../assets/knot_grey.png')"
                      max-width="40"
                    ></v-img>
                  </v-btn>
                  <v-btn>
                    <v-img
                      v-if="getRed"
                      class="mx-1"
                      :src="require('../../../assets/knot_red.png')"
                      max-width="40"
                    ></v-img>
                    <v-img
                      v-if="!getRed"
                      class="mx-1"
                      :src="require('../../../assets/knot_grey.png')"
                      max-width="40"
                    ></v-img>
                  </v-btn>
                </v-btn-toggle>
                </v-sheet>
              </v-col>
              <v-col cols="3">
                <v-sheet class="pa-3">
                  <v-switch
                    v-model="data.isActive"
                    :disabled="!isAuthenticated"
                    color="secondary"
                    label="Veröffentlicht">
                  </v-switch>
                </v-sheet>
              </v-col>
            </v-row>
          </v-container>
   </v-form>
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
</template>

<script>
import axios from 'axios';

import ErrorMessage from '@/views/components/common/ErrorMessage.vue';
import SuccessMessage from '@/views/components/common/SuccessMessage.vue';


export default {
  props: ['tags'],

  components: {
    ErrorMessage,
    SuccessMessage,
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    dialog: false,
    valid: true,
    showError: false,
    showSuccess: false,
    responseObj: null,
    rules: {
      title: [
        v => !!v || 'Titel ist erforderlich',
        v => (v && v.length >= 10) || 'Name must be more than 10 characters',
        v => (v && v.length <= 40) || 'Name must be less than 40 characters',
      ],
      description: [
        v => !!v || 'Beschreibung ist erforderlich',
        v => (v && v.length >= 75) || 'Name must be more than 75 characters',
        v => (v && v.length <= 2000) || 'Name must be less than 1000 characters',
      ],
      material: [
        v => (v.length <= 200) || 'Name must be less than 200 characters',
      ],
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Tag ist erforderlich',
      ],
      createdBy: [
        v => (v && v.length > 3) || 'Mindestens drei Zeichen',
      ],
    },
    data: {
      title: '',
      description: '',
      isPossibleOutside: true,
      isPossibleInside: true,
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
    levelFilter: [0, 1, 2],
  }),

  computed: {
    getOrange() {
      if (this.levelFilter) {
        return this.levelFilter.includes(0);
      }
      return false;
    },
    getBlue() {
      if (this.levelFilter) {
        return this.levelFilter.includes(1);
      }
      return false;
    },
    getRed() {
      if (this.levelFilter) {
        return this.levelFilter.includes(2);
      }
      return false;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    currentUsername() {
      return this.$store.getters.getUsername;
    },
  },

  methods: {
    formSubmit() {
      if (!this.$refs.form.validate()) {
        return;
      }
      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/event/`, {
          title: this.data.title,
          description: this.data.description,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          costsRating: this.data.costsRating,
          executionTimeRating: this.data.executionTimeRating,
          isPrepairationNeeded: this.data.isPrepairationNeeded,
          isActive: this.data.isActive,
          isLvlOne: this.getLevel(0, this.data.material),
          isLvlTwo: this.getLevel(1, this.data.material),
          isLvlThree: this.getLevel(2, this.data.material),
          createdBy: !this.isAuthenticated
            ? this.data.createdBy : this._.startCase(this.currentUsername),
          createdByEmail: this.data.createdByEmail,
        })
          .then(() => {
            this.dialog = false;
            this.$emit('dialogClose');
            this.showSuccess = true;
          })
          .catch((error) => {
            this.showError = true;
            console.error(error);
          });
      } else if (this.isUpdate) {
        axios.put(`${this.API_URL}basic/event/${this.data.id}/`, {
          id: this.data.id,
          title: this.data.title,
          description: this.data.description,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          costsRating: this.data.costsRating,
          executionTimeRating: this.data.executionTimeRating,
          isPrepairationNeeded: this.data.isPrepairationNeeded,
          isActive: this.data.isActive,
          isLvlOne: this.getLevel(0, this.data.material),
          isLvlTwo: this.getLevel(1, this.data.material),
          isLvlThree: this.getLevel(2, this.data.material),
        })
          .then(() => {
            this.dialog = false;
            this.$emit('dialogClose');
            this.showSuccess = true;
          })
          .catch((error) => {
            this.showError = true;
            console.error(error);
          });
      }
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
      }
    },

    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },

    save() {
      this.formSubmit();
    },
    getLevel(value, array) {
      console.log(array);
      return true;
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
</style>

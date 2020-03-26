<template>
<div>
  <v-stepper
    v-model="e6"
    vertical
  >
    <v-stepper-step
      editable
      :complete="e6 > 1"
      step="1"
    >
      Text Informationen
      <small>Füge Texte zum Heimabend hinzu</small>
    </v-stepper-step>

    <v-stepper-content :class="getClassForTextContentSteps" step="1">
        <v-form
        ref="form1"
        v-model="valid"
      >
        <v-container >
          <v-row>
            <v-col cols="12">
              <v-text-field
                outlined
                autofocus
                :counter="40"
                :rules="rules.title"
                label="Titel"
                v-model="data.title"
                required>
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <editor
                  api-key="3syby8pyhylkqgpeyskfycuy0pc47gvppx1311cqijn05wxu"
                  initialValue="<p>Ihr könnt</p>"
                  v-model="data.description"
                  :rules="rules.description"
                  required
                  :init="{
                    height: 500,
                    menubar: false,
                    plugins: [
                      'advlist autolink lists link image charmap print preview anchor',
                      'searchreplace visualblocks code fullscreen',
                      'insertdatetime media table paste code help wordcount'
                    ],
                    toolbar:
                      'formatselect | bold italic underline | forecolor | \
                      bullist numlist | removeformat | undo redo'
                  }"
                  />
                  <div class="v-text-field__details" v-if="getCustomText !== 'Ok'">
                  <div class="v-messages theme--light error--text" role="alert">
                    <div class="v-messages__wrapper">
                      <div class="v-messages__message customerRequired pl-3 ma-1">
                        {{ getCustomText }}
                      </div>
                    </div>
                  </div>
                </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                outlined
                label="Materialliste"
                :counter="200"
                required
                :rules="rules.material"
                v-model="data.material"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
        <v-btn color="primary" @click="onNextClick()">Weiter</v-btn>

      </v-form>
    </v-stepper-content>

    <v-stepper-step
      :complete="e6 > 2"
      step="2"
    >
      Zusatz Informationen
      <small>
        Füge Zusatz Informationen zum Heimabend hinzu,
        damit der Heimabend besser gefunden werden kann.
      </small>
    </v-stepper-step>

    <v-stepper-content :class="getClassForTextContentSteps" step="2">
      <v-form
        ref="form2"
        v-model="valid"
      >
        <v-container>
          <v-row no-gutters>
            <v-col
              cols="12"
              sm="5"
              class="ma-3"
            >
              <v-sheet class="pa-2">
               <v-switch
                v-model="data.isPossibleInside"
                color="secondary"
                label="Ist Drinnen möglich?">
              </v-switch>
              <v-switch
                v-model="data.isPossibleOutside"
                color="secondary"
                label="Ist Draußen möglich?">
              </v-switch>
              <v-switch
                v-model="data.isPrepairationNeeded"
                color="secondary"
                label="Hat Vorbereitung nötig?">
              </v-switch>
              <v-switch
                v-model="data.isPossibleDigital"
                color="secondary"
                label="Ist Online mit der Sippe durchführbar?">
              </v-switch>
              <v-switch
                v-model="data.isPossibleAlone"
                color="secondary"
                label="Ist alleine durchführbar?">
              </v-switch>
            </v-sheet>
          </v-col>
          <v-col
            cols="12"
              sm="5"
              class="ma-3"
          >
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

          <v-col
            cols="12"
              sm="5"
              class="ma-3"
          >
            <v-sheet class="pa-3">
              <span class="subtitle-1">
                Wieviel Geld ist nötig?
              </span>  <!-- -->
              <v-row justify="center">
                <v-tooltip
                  nudge-left="80"
                  open-on-hover
                  bottom
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      v-on="on"
                      text
                    >
                        <v-rating
                          v-model="data.costsRating"
                          emptyIcon="mdi-currency-usd"
                          fullIcon="mdi-currency-usd"
                          color="orange"
                          background-color="grey"
                          min="0"
                          length="3"
                        ></v-rating>
                    </v-btn>
                  </template>
                  <span>
                    <p class="text-left">
                    Stufe 1: 0,00€ - 0,50€ pro Person <br>
                    Stufe 2: 1€ - 2€ pro Person <br>
                    Stufe 3: mehr als 2€ pro Person <br>
                    </p>
                  </span>
                </v-tooltip>
                <v-btn
                  :color="withoutCostsButtomColor"
                  small
                  class="ma-2"
                  @click="onResetPriceClick()"
                >
                <v-icon
                  :color="withoutCostsIconColor"
                >
                  mdi-currency-usd-off
                </v-icon>
                  Ohne Kosten
                </v-btn>
              </v-row>
            <span class="subtitle-1">
              Wieviel Durchführungszeit ist erforderlich?
            </span>
              <v-row justify="center">
               <v-tooltip
                  nudge-left="80"
                  open-on-hover
                  bottom
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      v-on="on"
                      text
                    >
                <v-rating
                  v-model="data.executionTimeRating"
                  emptyIcon="mdi-clock"
                  fullIcon="mdi-clock"
                  color="black"
                  background-color="grey"
                  min="0"
                  length="3"
                ></v-rating>
                    </v-btn>
                  </template>
                  <span>
                    <p class="text-left">
                    Stufe 1: bis 30 min <br>
                    Stufe 2: 30 min - 60 min<br>
                    Stufe 3: mehr als 60 min<br>
                    </p>
                  </span>
                </v-tooltip>
                  <v-btn
                  :color="largeProjectButtomColor"
                  small
                  class="ma-2"
                  @click="onLargeProjectClick()"
                >
                <v-icon
                  :color="largeProjectIconColor"
                >
                  mdi-table-large
                </v-icon>
                  Großprojekt
                </v-btn>
              </v-row>
            </v-sheet>
          </v-col>
          <v-col
            cols="12"
              sm="5"
              class="ma-3"
          >
            <v-sheet class="pa-3">
            <span class="subtitle-1">
              Für welche Stufe ist der Heimabend geeignet?
            </span>
            <v-btn-toggle
              v-model="levelFilter"
              multiple
              mandatory
            >
              <v-btn>
                <v-img
                  v-if="getOrange"
                  class="mx-1"
                  :src="require('@/assets/wolfskopf.png')"
                  max-width="40"
                />
                <v-img
                  v-if="!getOrange"
                  class="mx-1"
                  :src="require('@/assets/wolfskopf_grau.png')"
                  max-width="40"
                ></v-img>
              </v-btn>
              <v-btn>
                <v-img
                  v-if="getBlue"
                  class="mx-1"
                  :src="require('@/assets/knot_blue.png')"
                  max-width="40"
                ></v-img>
                <v-img
                  v-if="!getBlue"
                  class="mx-1"
                  :src="require('@/assets/knot_grey.png')"
                  max-width="40"
                ></v-img>
              </v-btn>
              <v-btn>
                <v-img
                  v-if="getRed"
                  class="mx-1"
                  :src="require('@/assets/knot_red.png')"
                  max-width="40"
                ></v-img>
                <v-img
                  v-if="!getRed"
                  class="mx-1"
                  :src="require('@/assets/knot_grey.png')"
                  max-width="40"
                ></v-img>
              </v-btn>
            </v-btn-toggle>
            </v-sheet>
          </v-col>

          <v-col
            cols="12"
              sm="5"
              class="ma-3"
          >
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

          <v-col
            cols="12"
              sm="5"
              class="ma-3"
          >
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
        <v-row>
            <v-checkbox
              color="green"
              v-model="agreeBox"
            :rules="[v => !!v || 'Nur mit der Einverständniserklärung kannst du Ideen einreichen']"
              label="Ich möchte meine Heimabendidee veröffentlichen und bin damit einverstanden,
                dass die Betreiber der Website ggf. Bearbeitungen an dem Beitrag vornehmen."
              required
            >
            </v-checkbox>
        </v-row>
      </v-container>

      <v-btn color="primary" @click="save()">Speichern</v-btn>

    </v-form>
    </v-stepper-content>
  </v-stepper>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
      :timeout="timeout"
    >
      {{ 'Fehler beim Speichern des Heimabends' }}
    </v-snackbar>
    <v-snackbar
      v-model="showSuccess"
      color="success"
      y='top'
      :timeout="timeout"
    >
      {{ 'Der Heimabend wurde erfolgreich gespeichert und warte auf die Freigabe' }}
    </v-snackbar>
    </div>
</template>

<script>
import axios from 'axios';
import Editor from '@tinymce/tinymce-vue';

export default {

  components: {
    editor: Editor,
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    e6: 1,
    dialog: false,
    valid: true,
    showError: false,
    showSuccess: false,
    timeout: 3000,
    responseObj: null,
    agreeBox: false,
    isEditorValid: true,
    rules: {
      title: [
        v => !!v || 'Titel ist erforderlich',
        v => (v && v.length >= 10) || 'Der Titel braucht mehr als 10 Zeichen',
        v => (v && v.length <= 40) || 'Der Titel darf nicht mehr als 40 Zeichen haben',
      ],
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Tag ist erforderlich',
      ],
      createdBy: [
        v => (v && v.length >= 3) || 'Der Name braucht mindestens drei Zeichen',
      ],
    },
    data: {
      title: '',
      description: '',
      isPossibleOutside: true,
      isPossibleInside: true,
      isPossibleAlone: false,
      isPossibleDigital: true,
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
    levelFilter: [0, 1, 2],
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
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
    tags() {
      return this.$store.getters.tags;
    },
    isCreate() {
      return !this.$attrs.id;
    },
    isUpdate() {
      return !!this.$attrs.id;
    },
    getCustomText() {
      const value = this.data.description;
      if (!value) {
        return 'Beschreibung ist erforderlich';
      }
      if (value && value.length <= 75) {
        return 'Name must be more than 75 characters';
      }
      if (value && value.length >= 2000) {
        return 'Name must be less than 1000 characters';
      }
      return 'Ok';
    },
    isLargeProject() {
      return this.data.executionTimeRating === 0;
    },
    largeProjectButtomColor() {
      return this.isLargeProject ? 'limegreen' : 'lightgrey';
    },
    largeProjectIconColor() {
      return this.isLargeProject ? 'black' : 'grey';
    },
    isWithoutCosts() {
      return this.data.costsRating === 0;
    },
    withoutCostsButtomColor() {
      return this.isWithoutCosts ? 'limegreen' : 'lightgrey';
    },
    withoutCostsIconColor() {
      return this.isWithoutCosts ? 'red darken-2' : 'grey';
    },
    getClassForTextContentSteps() {
      return this.isMobil ? 'mx-0 px-1' : '';
    },
  },

  mounted() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
      if (this.data.tags && this.data.tags.length) {
        this.data.tags = this.setIntTags(this.data.tags);
      }
    }
  },

  created() {
    this.agreeBox = !!this.$store.getters.isAuthenticated;
  },


  methods: {
    onResetPriceClick() {
      this.data.costsRating = 0;
    },
    onLargeProjectClick() {
      this.data.executionTimeRating = 0;
    },
    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    setIntTags(urlTags) {
      const tagList = [];
      urlTags.forEach((tag) => {
        tagList.push(this.convertUrlToId(tag));
      });
      return tagList;
    },
    onNextClick() {
      if (!this.$refs.form1.validate()
        || this.getCustomText !== 'Ok') {
        return false;
      }
      this.levelFilter = [];
      if (this.data.isLvlOne) {
        this.levelFilter.push(0);
      }
      if (this.data.isLvlTwo) {
        this.levelFilter.push(1);
      }
      if (this.data.isLvlThree) {
        this.levelFilter.push(2);
      }
      this.e6 = 2;
      return true;
    },
    formSubmit() {
      if (
        !this.$refs.form1.validate()
        || !this.$refs.form2.validate()
        || this.getCustomText !== 'Ok'
      ) {
        return;
      }
      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/event/`, {
          title: this.data.title,
          description: this.data.description,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          isPossibleDigital: this.data.isPossibleDigital,
          isPossibleAlone: this.data.isPossibleAlone,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          costsRating: this.data.costsRating,
          executionTimeRating: this.data.executionTimeRating,
          isPrepairationNeeded: this.data.isPrepairationNeeded,
          isActive: this.data.isActive,
          isLvlOne: this.getLevel(0, this.levelFilter),
          isLvlTwo: this.getLevel(1, this.levelFilter),
          isLvlThree: this.getLevel(2, this.levelFilter),
          createdBy: !this.isAuthenticated
            ? this.data.createdBy : this._.startCase(this.currentUsername),
          createdByEmail: this.data.createdByEmail,
        })
          .then(() => {
            this.$router.push({ name: 'overview' });
            this.showSuccess = true;
          })
          .catch(() => {
            this.showError = true;
          });
      } else if (this.isUpdate) {
        axios.put(`${this.API_URL}basic/event/${this.data.id}/`, {
          id: this.data.id,
          title: this.data.title,
          description: this.data.description,
          isPossibleOutside: this.data.isPossibleOutside,
          isPossibleInside: this.data.isPossibleInside,
          isPossibleDigital: this.data.isPossibleDigital,
          isPossibleAlone: this.data.isPossibleAlone,
          tags: this.getUrlTagList(this.data.tags),
          material: this.data.material,
          costsRating: this.data.costsRating,
          executionTimeRating: this.data.executionTimeRating,
          isPrepairationNeeded: this.data.isPrepairationNeeded,
          isActive: this.data.isActive,
          isLvlOne: this.getLevel(0, this.levelFilter),
          isLvlTwo: this.getLevel(1, this.levelFilter),
          isLvlThree: this.getLevel(2, this.levelFilter),
        })
          .then(() => {
            this.$router.push({ name: 'overview' });
            this.$emit('dialogClose');
            this.showSuccess = true;
          })
          .catch(() => {
            this.showError = true;
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
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },

    save() {
      this.formSubmit();
    },

    getLevel(searchParameter, filterArray) {
      if (filterArray && filterArray.length) {
        return filterArray.includes(searchParameter);
      }
      return false;
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
.customerRequired {
  text-align: left;
}

.limegreen {
    background-color: #32CD3266 !important;
}
</style>

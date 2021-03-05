<template>
        <v-form
        ref="form2"
        v-model="valid"
      >
  <v-container>
    <v-row  class="mt-6 ml-2 text-left">
      <span class="subtitle-1">
        Bitte fasse im ersten Absatz deine Idee zusammmen und beschreibe
        danach deine Idee ausführlicher. <br>
      </span>
    </v-row>
    <v-row>
      <v-col cols="12">
        <editor
            api-key="3syby8pyhylkqgpeyskfycuy0pc47gvppx1311cqijn05wxu"
            initialValue="<p>Ihr könnt</p>"
            v-model="data.description"
            :rules="rules.description"
            required
            @onInit="onInit()"
            :init="{
              height: 500,
              language: 'de',
              image_advtab: true,
              menubar: 'edit insert view format tools table',
              plugins: [
                'advlist autolink lists link image preview',
                'searchreplace visualblocks code',
                'table paste code wordcount image code',
              ],
              toolbar:
                'formatselect | bold italic underline | forecolor | \
                bullist numlist | removeformat | undo redo | image'
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
      <v-progress-circular
        v-show="loading"
        color="primary"
        indeterminate
      />
      </v-col>
    </v-row>
    <v-row  class="mt-6 ml-2 text-left">
      <span class="subtitle-2">
        Damit die Idee übersichtlicher dargestellt wird möchten wir
        dich bitten, deinen Beschreibungstext gedanklich in zwei
        Abschnitte zu gliedern: Im ersten Abschnitt fass bitte deine
        Heimabend-Idee kurz zusammen und im zweiten Abschnitt kannst
        du genauer beschreiben, worum es sich handelt. <br>
        <br>
          <i>Beachte: In dem nächsten Schritt hast du die Möglichkeit
          deine Materialliste zu erstellen, sodass du dein Material
          nicht im Beschreibungstext auflisten musst</i>
        <br>
        Viel Spaß dabei!
      </span>
    </v-row>
    <v-row class="ma-3" justify="center">
      <v-btn
        class="mr-5"
        @click="prevStep()"
      >
        Zurück
      </v-btn>

      <v-btn
        color="primary"
        @click="nextStep(n)"
      >
        Weiter
      </v-btn>
    </v-row>
  </v-container>
        </v-form>
</template>

<script>
import Editor from '@tinymce/tinymce-vue';

export default {

  components: {
    editor: Editor,
  },

  data: () => ({
    rules: {
    },
    data: {
      description: '',
    },
    loading: true,
    valid: true,
    n: 0,
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getCustomText() {
      const value = this.data.description;
      if (!value) {
        return 'Du musst eine Beschreibung hinzufügen.';
      }
      if (value && value.length <= 75) {
        return 'Die Beschreibung ist zu kurz.';
      }
      if (value && value.length >= 8000) {
        return 'Beschreibung ist zu lang. Sie darf maximal 3500 Zeichen besitzen.';
      }
      return 'Ok';
    },
  },

  created() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },

  methods: {
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form2.validate() || this.getCustomText !== 'Ok') {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        description: this.data.description,
      };
    },
    onInit() {
      this.loading = false;
    },
  },
};
</script>

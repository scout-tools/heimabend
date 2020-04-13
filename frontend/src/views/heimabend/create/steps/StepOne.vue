<template>
        <v-form
        ref="form1"
        v-model="valid"
      >
  <v-container>
    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Gebe eine Passende Überschrift für deinen Heimabend ein.
      </span>
    </v-row>
    <v-row class="ma-4">
      <v-text-field
        outlined
        autofocus
        :counter="40"
        :rules="rules.title"
        label="Titel"
        v-model="data.title"
        required>
      </v-text-field>
    </v-row>

    <v-divider class="my-2"/>

    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Gebe eine Passende Überschrift für deinen Heimabend ein.
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
    <v-row justify="center">
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
      title: [
        v => !!v || 'Titel ist erforderlich',
        v => (v && v.length >= 10) || 'Der Titel braucht mehr als 10 Zeichen',
        v => (v && v.length <= 40) || 'Der Titel darf nicht mehr als 40 Zeichen haben',
      ],
    },
    data: {
      title: '',
      description: '',
    },
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getCustomText() {
      const value = this.data.description;
      if (!value) {
        return 'Beschreibung ist erforderlich';
      }
      if (value && value.length <= 75) {
        return 'Die Beschreibung muss mindestens 75 Zeichen haben.';
      }
      if (value && value.length >= 1000) {
        return 'Beschreibung ist zu lang. Er darf maximal 1000 Zeichen besitzen.';
      }
      return 'Ok';
    },
  },

  methods: {
    nextStep() {
      if (!this.$refs.form1.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return this.data;
    },
  },
};
</script>

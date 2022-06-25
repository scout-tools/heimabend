<template>
  <v-form ref="form2" v-model="valid">
    <v-container>
      <v-row class="mt-6 ml-2 text-left">
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
              image_title: true,
              automatic_uploads: true,
              file_picker_types: 'image',
              image_dimensions: true,
              menubar: 'edit insert view format tools table',
              plugins: [
                'advlist autolink lists link image preview',
                'searchreplace visualblocks code',
                'table paste wordcount',
              ],
              toolbar:
                'formatselect | bold italic underline | forecolor | \
                bullist numlist | removeformat | undo redo | image',
              file_picker_callback: imageUploadhandler,
              relative_urls: false, // eslint-disable-line
              remove_script_host: false, // eslint-disable-line
              style_formats: [
                { title: 'Bilder' },
                {
                  title: 'Bild Links',
                  selector: 'img',
                  styles: {
                    float: 'left',
                    margin: '10px 10px 10px 10px',
                  },
                },
              ],
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
          <v-progress-circular v-show="loading" color="primary" indeterminate />
        </v-col>
      </v-row>
      <v-row class="mt-6 ml-2 text-left">
        <span class="subtitle-2">
          Damit die Idee übersichtlicher dargestellt wird möchten wir dich
          bitten, deinen Beschreibungstext gedanklich in zwei Abschnitte zu
          gliedern: Im ersten Abschnitt fass bitte deine Heimabend-Idee kurz
          zusammen und im zweiten Abschnitt kannst du genauer beschreiben, worum
          es sich handelt. <br />
          <br />
          <i
            >Beachte: In dem nächsten Schritt hast du die Möglichkeit deine
            Materialliste zu erstellen, sodass du dein Material nicht im
            Beschreibungstext auflisten musst.</i
          >
          <br />
          Viel Spaß dabei!
        </span>
      </v-row>
      <v-row class="ma-3" justify="center">
        <v-btn class="ma-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="ma-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right> mdi-chevron-right </v-icon>
        </v-btn>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                v-on="on"
                icon
                class="ma-1"
                color="secondary"
                @click="nextStep(true)"
              >
                <v-icon>
                  mdi-debug-step-over
                </v-icon>
              </v-btn>
            </template>
            <span>
              {{ 'Schritt überspringen' }}
            </span>
          </v-tooltip>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import Editor from '@tinymce/tinymce-vue';
import axios from 'axios';

export default {
  components: {
    editor: Editor,
  },

  data: () => ({
    rules: {},
    getImageUrl: process.env.VUE_APP_API + 'basic/imageupload/', // eslint-disable-line
    loading: true,
    valid: true,
    n: 0,
  }),
  props: {
    data: Object,
  },
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
        return 'Beschreibung ist zu lang. Sie darf maximal 8000 Zeichen besitzen.';
      }
      return 'Ok';
    },
  },

  methods: {
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep(skip = false) {
      if (
        (!this.$refs.form2.validate() || this.getCustomText !== 'Ok') && !skip
      ) {
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
    // imageUploadhandler(blobInfo, success, failure, progress) { // eslint-disable-line
    imageUploadhandler(cb, value, meta) { // eslint-disable-line
      const me = this;
      var input = document.createElement('input'); // eslint-disable-line
      input.setAttribute('type', 'file');
      input.setAttribute('accept', 'image/*');

      input.onchange = function () { // eslint-disable-line
        var file = this.files[0]; // eslint-disable-line

        var reader = new FileReader(); // eslint-disable-line
        reader.onload = function () { // eslint-disable-line
          var id = 'blobid' + new Date().getTime(); // eslint-disable-line
          var blobCache = tinymce.activeEditor.editorUpload.blobCache; // eslint-disable-line
          var base64 = reader.result.split(',')[1]; // eslint-disable-line
          var blobInfo = blobCache.create(id, file, base64); // eslint-disable-line
          blobCache.add(blobInfo);

          const formData = new FormData();

          formData.append('image', blobInfo.blob());
          formData.append('description', '123');

          me.postUpload(formData).then((response) => {
            cb(
              `${process.env.VUE_APP_API.slice(0, -1)}${response.data.image}`,
              { title: file.name },
            );
          });

          /* call the callback and populate the Title field with the file name */
        };
        reader.readAsDataURL(file);
      };
      input.click();
    },

    async postUpload(formData) {
      return axios.post(`${process.env.VUE_APP_API}upload/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
    },
  },
};
</script>

<style scoped>
img {
  max-width: 300px !important;
  margin: 10px !important;
}
</style>

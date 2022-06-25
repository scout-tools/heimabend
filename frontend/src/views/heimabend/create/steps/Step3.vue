<template>
  <v-form v-model="valid" ref="form3">
    <v-container fluid class="ma-3">
      <v-row class="mt-6 ml-4">
        <span class="subtitle-1">
          Hier kannst du ein Titelbild für deinen Heimabend einfügen.
        </span>
      </v-row>
      <v-row class="ma-4">
        <v-checkbox
          prepend-icon="mdi-image"
          v-model="addImage"
          label="Neues Titelbild einfügen"
          required
        >
          <template slot="append">
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon color="success" dark v-bind="attrs" v-on="on">
                  mdi-help-circle-outline
                </v-icon>
              </template>
              <span>
                {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
              </span>
            </v-tooltip>
          </template>
        </v-checkbox>
      </v-row>
      <v-row v-if="imageUuid">
        <v-img
          class="ma-5"
          max-height="300"
          aspect-ratio="2"
          :src="getImageLink"
        >
        </v-img>
      </v-row>
      <div v-if="addImage">
        <v-row class="ma-4">
          <v-file-input
            label="Datei"
            show-size
            prepend-icon="mdi-image"
            @change="uploadImage"
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
                </span>
              </v-tooltip>
            </template>
          </v-file-input>
        </v-row>
        <v-row v-if="showCropper">
          <cropper
            ref="cropper"
            class="example-cropper"
            :stencil-props="{
              aspectRatio: 2,
            }"
            :src="imageData"
          />
        </v-row>
        <v-row align="center" justify="center" v-if="isLoading">
          Uploading
          <v-progress-circular
            indeterminate
            size="100"
            color="primary"
          ></v-progress-circular>
        </v-row>
        <v-row v-if="showCropper">
          <v-btn class="ma-3" color="success" @click="onUploadImageClick">
            <v-icon>mdi-upload</v-icon>
            Diesen Ausschnitt Hochladen
          </v-btn>
        </v-row>
      </div>
      <div v-show="addImage">
        <v-row class="ma-4" v-if="false">
          <v-text-field
            v-model="tempData.imageId"
            prepend-icon="mdi-image"
            hint="This field uses counter prop"
            label="Foto-ID"
            disabled
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
                </span>
              </v-tooltip>
            </template>
          </v-text-field>
        </v-row>
        <v-row class="ma-4" v-if="false">
          <v-text-field
            v-model="imageUuid"
            prepend-icon="mdi-image"
            hint="This field uses counter prop"
            label="UUID"
            disabled
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
                </span>
              </v-tooltip>
            </template>
          </v-text-field>
        </v-row>
        <div v-if="imageUuid">
        <v-row class="ma-4">
          <v-text-field
            prepend-icon="mdi-image"
            v-model="tempData.description"
            :error-messages="descriptionErrors"
            label="Bild Beschreibung"
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
                </span>
              </v-tooltip>
            </template>
          </v-text-field>
        </v-row>
        <v-row class="ma-4">
          <v-text-field
            prepend-icon="mdi-image"
            v-model="tempData.photographerName"
            :error-messages="photographerNameErrors"
            label="Fotograf_in"
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
                </span>
              </v-tooltip>
            </template>
          </v-text-field>
        </v-row>
        <v-row class="ma-4">
          <v-checkbox
            prepend-icon="mdi-image"
            v-model="tempData.privacyConsent"
            :error-messages="privacyConsentErrors"
            label="Datenschutz"
            required
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{
                    'Entspricht das Bild den Datenschutzrichtlinien.' +
                    'Es darf keine Bilder enthaltenn.'
                  }}
                </span>
              </v-tooltip>
            </template>
          </v-checkbox>
        </v-row>
        <v-row class="ma-4">
          <v-checkbox
            prepend-icon="mdi-image"
            v-model="tempData.isOpenSource"
            :error-messages="isOpenSourceErrors"
            label="Bildrechte"
            required
          >
            <template slot="append">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" dark v-bind="attrs" v-on="on">
                    mdi-help-circle-outline
                  </v-icon>
                </template>
                <span>
                  {{ 'Sind die Bildrechte Open Source?' }}
                </span>
              </v-tooltip>
            </template>
          </v-checkbox>
        </v-row>
        </div>
      </div>
      <v-row class="ma-3" justify="center">
        <v-btn class="ma-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="ma-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right> mdi-chevron-right </v-icon>
        </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import axios from 'axios';
import { Cropper } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';
// eslint-disable-next-line
import { validationMixin } from 'vuelidate';
import {
  requiredIf,
} from 'vuelidate/lib/validators';

export default {
  mixins: [validationMixin],
  components: {
    Cropper,
  },
  validations: {
    tempData: {
      description: {
        required: requiredIf(item => !!item.id && !!item.description),
      },
      photographerName: {
        required: requiredIf(item => !!item.id && !!item.photographerName),
      },
      privacyConsent: {
        required: requiredIf(item => !!item.id && !!item.privacyConsent),
      },
      isOpenSource: {
        required: requiredIf(item => !!item.id && !!item.isOpenSource),
      },
    },
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    n: 0,
    dialog: false,
    cropImg: '',
    valid: true,
    visibleComponent: 'cropperjs',
    isLoading: false,
    showCropper: false,
    imageData: null,
    addImage: false,
    imageUuid: null,
    tempData: {
      id: null,
      eventId: null,
      imageUuid: {
        imageUuid: null,
      },
      description: null,
      photographerName: null,
      privacyConsent: null,
      isOpenSource: null,
    },
  }),
  props: {
    data: Object,
  },
  watch: {
    data(value) {
      if (value.headerImage) {
        this.tempData = value.headerImage;
      }
      this.imageUuid = this.getUuid(value);
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getImageLink() {
      if (this.imageUuid) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${this.imageUuid}.default.jpeg`;
      }
      return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/inspi_v2.png`;
    },
    descriptionErrors() {
      const errors = [];
      if (!this.$v.tempData.description.$dirty) return errors;
      !this.$v.tempData.description.required && errors.push('Beschreibung einfügen'); // eslint-disable-line
      return errors;
    },
    photographerNameErrors() {
      const errors = [];
      if (!this.$v.tempData.photographerName.$dirty) return errors;
      !this.$v.tempData.photographerName.required && errors.push('Name des Fotofrafen einfügen'); // eslint-disable-line
      return errors;
    },
    privacyConsentErrors() {
      const errors = [];
      if (!this.$v.tempData.privacyConsent.$dirty) return errors;
      !this.$v.tempData.privacyConsent.required && errors.push('Bitte einwilligen'); // eslint-disable-line
      return errors;
    },
    isOpenSourceErrors() {
      const errors = [];
      if (!this.$v.tempData.isOpenSource.$dirty) return errors;
      !this.$v.tempData.isOpenSource.required && errors.push('Bitte einwilligen'); // eslint-disable-line
      return errors;
    },
  },
  methods: {
    getUuid(value) {
      if (
        value
        && value.headerImage
        && value.headerImage.imageUuid
        && value.headerImage.imageUuid.imageUuid
      ) {
        return value.headerImage.imageUuid.imageUuid;
      }
      return null;
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      this.validate();
      if (this.valid) {
        this.$emit('nextStep');
      }
    },
    onUploadImageClick() {
      const me = this;
      this.isLoading = true;
      const { canvas } = this.$refs.cropper.getResult();
      this.showCropper = false;
      if (canvas) {
        const formData = new FormData();
        canvas.toBlob((blob) => {
          formData.append('image', blob, 'header.jpeg');

          me.postUpload(formData).then((response) => {
            me.callback(response);
          });
        }, 'image/jpeg');
      }
    },
    callback(response) {
      this.tempData.imageId = response.data.id; // image-id
      this.imageUuid = response.data.imageUuid; // just for display stuff
      this.isLoading = false;
    },
    async postUpload(formData) {
      return axios.post(`${process.env.VUE_APP_API}upload/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
    },
    getData() {
      return {
        id: this.tempData.id, // image-meta-id
        imageId: this.tempData.imageId, // image-id
        description: this.tempData.description,
        photographerName: this.tempData.photographerName,
        privacyConsent: this.tempData.privacyConsent,
        isOpenSource: this.tempData.isOpenSource,
      };
    },
    flipX() {
      const dom = this.$refs.flipX;
      let scale = dom.getAttribute('data-scale');
      scale = scale ? -scale : -1;
      this.$refs.cropper.scaleX(scale);
      dom.setAttribute('data-scale', scale);
    },
    flipY() {
      const dom = this.$refs.flipY;
      let scale = dom.getAttribute('data-scale');
      scale = scale ? -scale : -1;
      this.$refs.cropper.scaleY(scale);
      dom.setAttribute('data-scale', scale);
    },
    getCropBoxData() {
      this.data = JSON.stringify(this.$refs.cropper.getCropBoxData(), null, 4);
    },
    move(offsetX, offsetY) {
      this.$refs.cropper.move(offsetX, offsetY);
    },
    reset() {
      this.$refs.cropper.reset();
    },
    rotate(deg) {
      this.$refs.cropper.rotate(deg);
    },
    setCropBoxData() {
      if (!this.data) return;
      this.$refs.cropper.setCropBoxData(JSON.parse(this.data));
    },
    setData() {
      if (!this.data) return;
      this.$refs.cropper.setData(JSON.parse(this.data));
    },
    uploadImage(file) {
      const me = this;
      me.imageData = null;

      if (file && file.type.indexOf('image/') === -1) {
        return;
      }
      if (typeof FileReader === 'function') {
        const reader = new FileReader();
        reader.onload = (event) => {
          me.imageData = event.target.result;
          // rebuild cropperjs with the updated source
          // me.$refs.cropper.src = event.target.result;
          me.showCropper = true;
        };
        reader.readAsDataURL(file);
      }
    },
    showFileChooser() {
      this.$refs.input.click();
    },
    zoom(percent) {
      this.$refs.cropper.relativeZoom(percent);
    },
    validate() {
      this.$v.$touch();
      this.valid = !this.$v.$anyError;
    },
  },
};
</script>

<style>
.example-cropper {
  border: solid 1px #eee;
  min-height: 300px;
  width: 100%;
}

.cropper {
  height: 600px;
  background: #ddd;
}
</style>

<template>
  <v-form ref="form3">
    <v-container fluid class="ma-3">
      <v-row class="mt-6 ml-4">
        <span class="subtitle-1">
          Hier kannst du ein Titelbild für deinen Heimabend einfügen.
        </span>
      </v-row>
      <v-row>
        <v-file-input
          class="ma-4"
          label="Titelbild"
          show-size
          prepend-icon="mdi-image"
          @change="uploadImage"
        >
        </v-file-input>
      </v-row>
      <v-row v-if="showCropper">
        <cropper
          ref="cropper"
          class="example-cropper"
          :stencil-props="{
            aspectRatio: 2,
          }"
          :src="data.imageData"
        />
      </v-row>
      <v-row v-else>
          <v-img
            class="ma-5"
            max-height="300"
            aspect-ratio="2"
            :src="data.imageLink"
          >
          </v-img>
      </v-row>
      <v-row>
        <v-text-field
          v-model="data.id"
          hint="This field uses counter prop"
          label="Foto-ID"
          disabled
        ></v-text-field>
      </v-row>
      <v-row>
        <v-text-field
          v-model="data.imageDescription"
          label="Bild Beschreibung"
        ></v-text-field>
      </v-row>
      <v-row>
        <v-text-field
          v-model="data.photographerName"
          label="Fotograf_in"
        ></v-text-field>
      </v-row>
      <v-row>
        <v-checkbox
          v-model="data.privacyConsent"
          color="red"
          label="Datenschutz"
          required
        ></v-checkbox>
      </v-row>
      <v-row>
        <v-checkbox
          v-model="data.isOpenSource"
          color="red"
          label="Bildrechte"
          required
        ></v-checkbox>
      </v-row>
      <v-row class="ma-3" justify="center">
        <v-btn class="mr-5" @click="prevStep()"> Zurück </v-btn>

        <v-btn color="primary" @click="nextStep(n)"> Weiter </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import axios from 'axios';
import { Cropper } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

export default {
  components: {
    Cropper,
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    n: 0,
    dialog: false,
    cropImg: '',
    visibleComponent: 'cropperjs',
    showCropper: false,
  }),
  props: {
    data: Object,
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
  },

  methods: {
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (this.showCropper) {
        this.saveImage();
      }

      this.$emit('nextStep');
    },

    saveImage() {
      const me = this;
      const { canvas } = this.$refs.cropper.getResult();
      if (canvas) {
        const formData = new FormData();
        canvas.toBlob((blob) => {
          formData.append('image', blob, 'userpic.jpeg');
          formData.append('is_open_source', me.data.isOpenSource);
          formData.append('privacy_consent', me.data.privacyConsent);
          formData.append('photographer_name', me.data.photographerName);
          formData.append('description', me.data.imageDescription);

          this.postUpload(formData).then((response) => {
            me.data.id = response.data.id;
            debugger;
          });
        }, 'image/jpeg');
      }
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
        imageId: this.data.id,
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
      me.data.imageData = null;
      me.showCropper = false;

      if (file && file.type.indexOf('image/') === -1) {
        return;
      }
      if (typeof FileReader === 'function') {
        const reader = new FileReader();
        reader.onload = (event) => {
          me.data.imageData = event.target.result;
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

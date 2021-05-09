<template>
  <v-container fluid>
    <v-row justify="center">
      <v-card class="mx-auto top-margin" max-width="800px">
        <v-stepper vertical v-model="currentStep">
          <v-stepper-step :complete="currentStep > 1" :step="1">
            {{ headerStep[0] }}
          </v-stepper-step>

          <v-stepper-content step="1">
            <step-one ref="step1" :data="data" @cancel="cancel()" @nextStep="nextStep()" />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 2" :step="2">
            {{ headerStep[1] }}
          </v-stepper-step>

          <v-stepper-content step="2">
            <step-two
              ref="step2"
              :data="data"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 3" :step="3">
            {{ headerStep[2] }}
          </v-stepper-step>

          <v-stepper-content step="3">
            <step-three
              ref="step3"
              :data="data"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 4" :step="4">
            {{ headerStep[3] }}
          </v-stepper-step>

          <v-stepper-content step="4">
            <step-four
              ref="step4"
              :data="data"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 5" :step="5">
            {{ headerStep[4] }}
          </v-stepper-step>

          <v-stepper-content step="5">
            <step-five
              ref="step5"
              :data="data"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 6" :step="6">
            {{ headerStep[5] }}
          </v-stepper-step>

          <v-stepper-content step="6">
            <step-six
              :data="data"
              ref="step6"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 7" :step="7">
            {{ headerStep[6] }}
          </v-stepper-step>

          <v-stepper-content step="7">
            <step-seven
              :data="data"
              ref="step7"
              @prevStep="prevStep()"
              @nextStep="nextStep()"
            />
          </v-stepper-content>

          <v-stepper-step :complete="currentStep > 8" :step="8">
            {{ headerStep[7] }}
          </v-stepper-step>

          <v-stepper-content step="8">
            <step-eight
              :data="data"
              ref="step8"
              @prevStep="prevStep()"
              @finish="finish()"
            />
          </v-stepper-content>
        </v-stepper>
      </v-card>
    </v-row>
    <v-snackbar v-model="showError" color="error" y="top" :timeout="timeout">
      {{ 'Fehler beim Speichern des Heimabends' }}
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from 'axios';

import StepOne from './steps/Step1.vue';
import StepTwo from './steps/Step2.vue';
import StepThree from './steps/Step3.vue';
import StepFour from './steps/Step4.vue';
import StepFive from './steps/Step5.vue';
import StepSix from './steps/Step6.vue';
import StepSeven from './steps/Step7.vue';
import StepEight from './steps/Step8.vue';

export default {
  components: {
    StepOne,
    StepTwo,
    StepThree,
    StepFour,
    StepFive,
    StepSix,
    StepSeven,
    StepEight,
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      currentStep: 1,
      steps: 7,
      showError: false,
      showSuccess: false,
      timeout: 7000,
      headerStep: [
        'Überschrift',
        'Beschreibungstext',
        'Titelbild',
        'Materialien',
        'Eigenschaften',
        'Themen',
        'Kategorien',
        'Abschließen',
      ],
      data: [],
    };
  },

  computed: {
    isLastStep() {
      return this.currentStep === this.steps;
    },
    isFirstStep() {
      return this.currentStep === 1;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getId() {
      return this.$route.params.id;
    },
  },

  watch: {
    steps(val) {
      if (this.currentStep > val) {
        this.currentStep = val;
      }
    },
  },
  created() {
    this.$store.commit('setHeaderString', 'Neuer Heimabend');
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
    if (this.getId) {
      axios
        .get(`${this.API_URL}basic/event/${this.getId}/?&timestamp=${new Date().getTime()}`)
        .then((response) => {
          this.data = response.data;
        });
    } else {
      this.data = {
        title: '',
        description: '',
        imageData: null,
        imageLink: null,
        materialItems: [],
        executionTime: 1,
        difficulty: 1,
        costsRating: 1,
        prepairationTime: 1,
        tags: [47, 46, 44, 43, 42, 45, 51, 50],
        createdBy: null,
        createdByEmail: '',
        isOpenSource: false,
        privacyConsent: false,
        photographerName: '',
        imageDescription: '',
      };
    }
  },
  methods: {
    nextStep() {
      this.currentStep += 1;
    },
    prevStep() {
      this.currentStep -= 1;
    },
    finish() {
      this.postData();
    },
    postData() {
      const dataStep1 = this.$refs.step1.getData();
      const dataStep2 = this.$refs.step2.getData();
      const dataStep5 = this.$refs.step5.getData();
      const dataStep6 = this.$refs.step6.getData();
      const dataStep7 = this.$refs.step7.getData();
      const dataStep8 = this.$refs.step8.getData();
      if (this.isCreate) {
        axios
          .post(`${this.API_URL}basic/event/`, {
            title: dataStep1.title,
            description: dataStep2.description,
            tags: dataStep6.tags.concat(dataStep7.selectedMandatoryFilter),
            costsRating: dataStep5.costsRating,
            executionTime: dataStep5.executionTime,
            prepairationTime: dataStep5.prepairationTime,
            difficulty: dataStep5.difficulty,
            isPublic: false,
            createdBy: dataStep8.createdBy,
            createdByEmail: dataStep8.createdByEmail,
          })
          .then((response) => {
            this.saveMaterial(response.data.id);
          })
          .catch(() => {
            this.showError = true;
          });
      } else if (this.isUpdate) {
        axios
          .put(`${this.API_URL}basic/event/${this.getId}/`, {
            id: this.data.id,
            title: dataStep1.title,
            description: dataStep2.description,
            tags: dataStep6.tags.concat(dataStep7.selectedMandatoryFilter),
            costsRating: dataStep5.costsRating,
            executionTime: dataStep5.executionTime,
            prepairationTime: dataStep5.prepairationTime,
            difficulty: dataStep5.difficulty,
            isPublic: false,
            createdBy: dataStep8.createdBy,
            createdByEmail: dataStep8.createdByEmail,
          })
          .then((response) => {
            this.saveMaterial(response.data.id);
          })
          .catch(() => {
            this.showError = true;
          });
      }
    },
    saveMaterial(eventId) {
      const materialList = this.$refs.step4.getData();
      if (materialList && materialList.length) {
        this.postMaterialItems(materialList, eventId).then(() => {
          this.saveImageMeta(eventId);
        });
      } else {
        this.saveImageMeta(eventId);
      }
    },
    saveImageMeta(eventId) {
      const imageMetaData = this.$refs.step3.getData();
      if (imageMetaData && imageMetaData.id) {
        this.putImageMeta(imageMetaData, eventId).then(() => {
          this.$router.push({
            name: 'heimabendCreateFinale',
          });
        });
      } else if (imageMetaData) {
        this.postImageMeta(imageMetaData, eventId).then(() => {
          this.$router.push({
            name: 'heimabendCreateFinale',
          });
        });
      }
    },
    async postMaterialItems(materialList, eventId) {
      const path = `${process.env.VUE_APP_API}material-items/`;
      const material = materialList.map(item => ({ ...item, eventId }));
      return axios.post(path, material);
    },
    async postImageMeta(imageMetaData, eventId) {
      const path = `${process.env.VUE_APP_API}basic/image-meta/`;
      return axios.post(path, {
        image: imageMetaData.imageId,
        description: imageMetaData.description,
        photographerName: imageMetaData.photographerName,
        privacyConsent: imageMetaData.privacyConsent,
        isOpenSource: imageMetaData.isOpenSource,
        event: eventId,
      });
    },
    async putImageMeta(imageMetaData, eventId) {
      const path = `${process.env.VUE_APP_API}basic/image-meta/${imageMetaData.id}/`;
      return axios.put(path, {
        image: imageMetaData.imageId,
        description: imageMetaData.description,
        photographerName: imageMetaData.photographerName,
        privacyConsent: imageMetaData.privacyConsent,
        isOpenSource: imageMetaData.isOpenSource,
        event: eventId,
      });
    },
    cancel() {
      this.$router.push({ name: 'overview' });
      this.$emit('dialogClose');
    },
  },
};
</script>

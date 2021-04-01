<template>
  <v-container>
    <v-row justify="center">
      <v-card class="mx-auto top-margin" max-width="800px">
        <v-stepper vertical v-model="currentStep">
          <v-stepper-step :complete="currentStep > 1" :step="1">
            {{ headerStep[0] }}
          </v-stepper-step>

          <v-stepper-content step="1">
            <step-one ref="step1" :data="data" @nextStep="nextStep()" />
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
        'Titel',
        'Beschreibung',
        'Bild',
        'Materialien',
        'Fakten',
        'Themen',
        'Kategorien',
        'Abschluss',
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

  methods: {
    nextStep() {
      this.currentStep += 1;
    },
    prevStep() {
      this.currentStep -= 1;
    },

    finish() {
      const dataStep1 = this.$refs.step1.getData();
      const dataStep2 = this.$refs.step2.getData();
      const dataStep3 = this.$refs.step3.getData();
      const dataStep4 = this.$refs.step4.getData();
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
            material: this.convertMaterialArrayString(dataStep4.material_list),
            material_list: dataStep4.material_list,
            costsRating: dataStep5.costsRating,
            executionTimeRating: dataStep5.executionTimeRating,
            isPrepairationNeeded: dataStep5.isPrepairationNeeded,
            isActive: dataStep8.isActive,
            imageLink: dataStep3.imageLink,
            createdBy: dataStep8.createdBy,
            createdByEmail: dataStep8.createdByEmail,
          })
          .then(() => {
            this.$router.push({
              name: 'overview',
              params: { showSuccess: true },
            });
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
            material: this.convertMaterialArrayString(dataStep4.material_list),
            material_list: dataStep4.material_list,
            costsRating: dataStep5.costsRating,
            executionTimeRating: dataStep5.executionTimeRating,
            isPrepairationNeeded: dataStep5.isPrepairationNeeded,
            isActive: dataStep8.isActive,
            imageLink: dataStep3.imageLink,
            createdBy: dataStep8.createdBy,
            createdByEmail: dataStep8.createdByEmail,
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
    convertMaterialArrayString(material) {
      if (material && material.length) {
        return material.join(',');
      }
      return '';
    },
  },
};
</script>

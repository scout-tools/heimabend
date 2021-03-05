<template>
<v-container>
  <v-row justify="center">
    <v-stepper
      vertical
      v-model="currentStep"
    >
      <v-stepper-header>
        <template v-for="n in steps">
          <v-stepper-step
            :key="`${n}-step`"
            :complete="currentStep > n"
            :step="n"
          >
            {{ headerStep[n-1] }}
          </v-stepper-step>

          <v-divider
            v-if="n !== steps"
            :key="n"
          ></v-divider>
        </template>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content
          step="1"
        >
          <step-one
            ref="step1"
            :data="data"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="2"
        >
          <step-two
            ref="step2"
            :data="data"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="3"
        >
          <step-three
            ref="step3"
            :data="data"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="4"
        >
          <step-four
            ref="step4"
            :data="data"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="5"
        >
          <step-five
            ref="step5"
            :data="data"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="6"
        >
          <step-six
            :data="data"
            ref="step6"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="7"
        >
          <step-seven
            :data="data"
            ref="step7"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="8"
        >
          <step-eight
            :data="data"
            ref="step8"
            @prevStep="prevStep()"
            @finish="finish()"
          />
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-row>
    <v-snackbar
      v-model="showError"
      color="error"
      y='top'
      :timeout="timeout"
    >
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

      // const dataStep8 = this.$refs.step8.getData();
      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/event/`, {
          title: dataStep1.title,
          description: dataStep2.description,
          tags: this.getUrlTagList(dataStep6.tags.concat(dataStep7.selectedMandatoryFilter)),
          material: this.convertMaterialArray(dataStep4.material),
          costsRating: dataStep5.costsRating,
          executionTimeRating: dataStep5.executionTimeRating,
          isPrepairationNeeded: dataStep5.isPrepairationNeeded,
          isActive: dataStep8.isActive,
          imageLink: dataStep3.imageLink,
          createdBy: dataStep8.createdBy,
          createdByEmail: dataStep8.createdByEmail,
        })
          .then(() => {
            this.$router.push({ name: 'overview', params: { showSuccess: true } });
          })
          .catch(() => {
            this.showError = true;
          });
      } else if (this.isUpdate) {
        axios.put(`${this.API_URL}basic/event/${this.getId}/`, {
          id: this.data.id,
          title: dataStep1.title,
          description: dataStep2.description,
          tags: this.getUrlTagList(dataStep6.tags.concat(dataStep7.selectedMandatoryFilter)),
          material: this.convertMaterialArray(dataStep4.material),
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
    getUrlTagList(tagList) {
      if (tagList) {
        const ary = [];
        tagList.forEach((tag) => {
          ary.push(`${process.env.VUE_APP_API}basic/tag/${tag}/`);
        });
        return ary;
      }
      return [];
    },
    convertMaterialArray(material) {
      return material.join(',');
    },
  },
};
</script>

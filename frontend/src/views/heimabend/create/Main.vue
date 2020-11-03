<template>
<v-container>
  <v-row justify="center">
    <v-flex
      ma-3
      lg7
    >
    <v-stepper
      alt-labels
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
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="3"
        >
          <step-three
            ref="step3"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="4"
        >
          <step-four
            ref="step4"
            @prevStep="prevStep()"
            @nextStep="nextStep()"
          />
        </v-stepper-content>

        <v-stepper-content
          step="5"
        >
          <step-five
            ref="step5"
            @prevStep="prevStep()"
            @finish="finish()"
          />
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
    </v-flex>
  </v-row>
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
      {{
        'Vielen Dank für deinen Beitrag zum Heimabend Inspirator! ' +
        'Deine Heimabenidee wurde erfolgreich gespeichert und wartet ' +
        'darauf, von uns freigeschaltet zu werden.' }}
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


export default {
  components: {
    StepOne,
    StepTwo,
    StepThree,
    StepFour,
    StepFive,
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      currentStep: 1,
      steps: 5,
      showError: false,
      showSuccess: false,
      timeout: 7000,
      headerStep: [
        'Beschreibung',
        'Eigenschaften',
        'Themenauswahl',
        'Pflichtthemen',
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
      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/event/`, {
          title: dataStep2.title,
          description: dataStep1.description,
          tags: this.getUrlTagList(dataStep3.tags.concat(dataStep4.selectedMandatoryFilter)),
          material: this.convertMaterialArray(dataStep2.material),
          costsRating: dataStep3.costsRating,
          executionTimeRating: dataStep3.executionTimeRating,
          isPrepairationNeeded: dataStep2.isPrepairationNeeded,
          isActive: dataStep5.isActive,
          createdBy: dataStep5.createdBy,
          createdByEmail: dataStep5.createdByEmail,
        })
          .then(() => {
            this.$router.replace({ name: 'overview' });
            this.showSuccess = true;
          })
          .catch(() => {
            this.showError = true;
          });
      } else if (this.isUpdate) {
        axios.put(`${this.API_URL}basic/event/${this.getId}/`, {
          id: this.data.id,
          title: dataStep2.title,
          description: dataStep1.description,
          tags: this.getUrlTagList(dataStep3.tags.concat(dataStep4.selectedMandatoryFilter)),
          material: this.convertMaterialArray(dataStep2.material),
          costsRating: dataStep3.costsRating,
          executionTimeRating: dataStep3.executionTimeRating,
          isPrepairationNeeded: dataStep2.isPrepairationNeeded,
          isActive: dataStep4.isActive,
          createdBy: dataStep4.createdBy,
          createdByEmail: dataStep4.createdByEmail,
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

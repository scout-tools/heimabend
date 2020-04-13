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
            Schritt {{ n }}
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
      {{ 'Der Heimabend wurde erfolgreich gespeichert und warte auf die Freigabe' }}
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from 'axios';

import StepFour from './steps/StepFour.vue';
import StepOne from './steps/StepOne.vue';
import StepTwo from './steps/StepTwo.vue';
import StepThree from './steps/StepThree.vue';


export default {
  components: {
    StepOne,
    StepTwo,
    StepThree,
    StepFour,
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      currentStep: 1,
      steps: 4,
      showError: false,
      showSuccess: false,
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

      if (this.isCreate) {
        axios.post(`${this.API_URL}basic/event/`, {
          title: dataStep1.title,
          description: dataStep1.description,
          isPossibleOutside: dataStep2.isPossibleOutside,
          isPossibleInside: dataStep2.isPossibleInside,
          isPossibleDigital: dataStep2.isPossibleDigital,
          isPossibleAlone: dataStep2.isPossibleAlone,
          tags: this.getUrlTagList(dataStep3.tags),
          material: dataStep2.material,
          costsRating: dataStep3.costsRating,
          executionTimeRating: dataStep3.executionTimeRating,
          isPrepairationNeeded: dataStep2.isPrepairationNeeded,
          isActive: dataStep4.isActive,
          isLvlOne: dataStep3.isLvlOne,
          isLvlTwo: dataStep3.isLvlTwo,
          isLvlThree: dataStep3.isLvlThree,
          createdBy: dataStep4.createdBy,
          createdByEmail: dataStep4.createdByEmail,
        })
          .then(() => {
            this.$router.replace({ name: 'overview' });
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
          createdBy: this.data.createdBy,
          createdByEmail: this.data.createdByEmail,
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
  },
};
</script>

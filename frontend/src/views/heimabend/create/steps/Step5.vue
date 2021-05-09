<template>
  <v-form ref="form5" v-model="valid">
    <v-container>
      <v-row class="ma-5">
        <creating-slider
          v-bind:value="data.difficulty"
          v-on:input="updateDifficulty"
          :headerText="'Schwierigkeitsgrad?'"
          :labels="['Einfach', 'Mittel', 'Schwer']"
          :icon="'mdi-head-snowflake-outline'"
          :color="'green'"

        />
      </v-row>

      <v-divider class="py-2"/>

      <v-row class="ma-5">
        <creating-slider
          :headerText="'Dauer?'"
          v-bind:value="data.executionTime"
          v-on:input="updateExecutionTime"
          :labels="['30 min', '60 min', '120 min', 'mehr']"
          :icon="'mdi-timer'"
          :color="'blue'"
        />
      </v-row>
      <v-divider class="py-2"/>

      <v-row class="ma-5">
        <creating-slider
          :headerText="'Kosten pro Person?'"
          v-bind:value="data.costsRating"
          v-on:input="updateCostsRating"
          :labels="['0,00 €' , '0,50 €', '1,00 €', 'mehr']"
          :icon="'mdi-currency-usd'"
          :color="'orange'"
        />
      </v-row>

      <v-divider class="py-2"/>

      <v-row class="ma-5">
        <creating-slider
          :headerText="'Vorbereitungszeit?'"
          v-bind:value="data.prepairationTime"
          v-on:input="updatePrepairationTime"
          :labels="['wenig', '30 min', '60 min', 'mehr']"
          :icon="'mdi-clock'"
          :color="'red ligthen-1'"
        />
      </v-row>

      <v-divider class="my-2" />
      <v-row class="ma-3" justify="center">
        <v-btn class="mx-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="mx-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right> mdi-chevron-right </v-icon>
        </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import CreatingSlider from '@/components/slider/CreatingSlider.vue';

export default {
  data: () => ({
    rules: {
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Thema ist erforderlich',
      ],
    },
    valid: true,
    n: 0,
    difficultlevel: 0,
  }),
  components: {
    CreatingSlider,
  },
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
    updateCostsRating(costsRating) {
      this.data.costsRating = costsRating;
    },
    updatePrepairationTime(prepairationTime) {
      this.data.prepairationTime = prepairationTime;
    },
    updateExecutionTime(executionTime) {
      this.data.executionTime = executionTime;
    },
    updateDifficulty(difficulty) {
      this.data.difficulty = difficulty;
    },
    difficult(val) {
      return this.icons[val];
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form5.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        costsRating: this.data.costsRating,
        executionTime: this.data.executionTime,
        prepairationTime: this.data.prepairationTime,
        difficulty: this.data.difficulty,
      };
    },
  },
};
</script>

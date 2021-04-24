<template>
  <v-form ref="form4" v-model="valid">
    <v-container>

      <v-row class="ma-5">
        <creating-slider
          v-model="data.difficultlevel"
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
          v-model="data.costsRating"
          :labels="['30 min', '60 min', '120 min', 'mehr']"
          :icon="'mdi-timer'"
          :color="'blue'"
        />
      </v-row>
      <v-divider class="py-2"/>

      <v-row class="ma-5">
        <creating-slider
          :headerText="'Kosten pro Person?'"
          v-model="data.costsRating"
          :labels="['0,00 €' , '0,50 €', '1,00 €', 'mehr']"
          :icon="'mdi-currency-usd'"
          :color="'orange'"
        />
      </v-row>

      <v-divider class="py-2"/>

      <v-row class="ma-5">
        <creating-slider
          :headerText="'Vorbereitungszeit?'"
          v-model="data.executionTimeRating"
          :labels="['wenig', '30 min', '60 min', 'mehr']"
          :icon="'mdi-clock'"
          :color="'red ligthen-1'"
        />
      </v-row>

      <v-divider class="my-2" />
      <v-row class="ma-3" justify="center">
        <v-btn class="mr-5" @click="prevStep()"> Zurück </v-btn>

        <v-btn color="primary" @click="nextStep()"> Weiter </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import { mapGetters } from 'vuex';
import CreatingSlider from '@/components/slider/CreatingSlider.vue';

export default {
  data: () => ({
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
    ...mapGetters(['tags', 'tagCategory']),
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
    difficult(val) {
      return this.icons[val];
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form4.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        tags: this.data.tags,
        costsRating: this.data.costsRating,
        executionTimeRating: this.data.executionTimeRating,
      };
    },
  },
};
</script>

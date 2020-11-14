<template>
  <v-form
    ref="form0"
    v-model="valid"
  >
  <v-container>
    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Gib eine passende Überschrift für deine Heimabend-Idee ein.
      </span>
    </v-row>
    <v-row class="ma-4">
      <v-text-field
        outlined
        autofocus
        :counter="40"
        :rules="rules.title"
        label="Überschrift"
        v-model="data.title"
        required>
      </v-text-field>
    </v-row>

    <v-divider class="my-2"/>
    

    <v-row class="ma-3" justify="center">
      <v-btn
        color="primary"
        @click="nextStep(n)"
      >
        Weiter
      </v-btn>
    </v-row>
  </v-container>
        </v-form>
</template>

<script>

export default {

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    n: 0,
    dialog: false,
    valid: true,
    data: {
      title: '',
      materialArray: [],
      isPrepairationNeeded: false,
    },
    rules: {
      title: [
        v => !!v || 'Überschrift ist erforderlich.',
        v => (v && v.length >= 10) || 'Die Überschrift ist zu kurz.',
        v => (v && v.length <= 40) || 'Die Überschtift ist zu lang.',
      ],
    },
  }),

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

  created() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
      this.convertMaterialString(this.data.material);
    }
  },


  methods: {
    convertMaterialString(array) {
      this.data.materialArray = array.split(',');
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form0.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        title: this.data.title,
        material: this.data.materialArray,
        isPrepairationNeeded: this.data.isPrepairationNeeded,
      };
    },
  },
};
</script>

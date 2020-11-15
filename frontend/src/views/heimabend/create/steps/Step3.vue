<template>
  <v-form
    ref="form3"
    v-model="valid"
  >
  <v-container>
    <v-row class="mt-6 ml-4">
      <span class="subtitle-1">
        Füge hier alle Materialien hinzu. Bestätige jedes einzelne Objekt mit "Enter".
      </span>
    </v-row>
    <v-row class="ma-4">
        <v-combobox
          outlined
          autofocus
          v-model="data.materialArray"
          label="Material Liste"
          multiple
          required
          chips
        ></v-combobox>
    </v-row>

    <v-row class="ma-3" justify="center">
      <v-btn
        class="mr-5"
        @click="prevStep()"
      >
        Zurück
      </v-btn>

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
      if (!this.$refs.form3.validate()) {
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

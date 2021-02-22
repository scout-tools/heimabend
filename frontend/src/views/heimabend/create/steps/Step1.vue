<template>
  <v-form
    ref="form1"
    v-model="valid"
  >
  <v-container>
    <v-row class="mt-6 ml-2">
      <span class="text-left subtitle-1">
        Willkommen bei der <b> Heimabenderstellung </b>. <br>
        <br>
        Viele Pfadfinder freuen sich
        schon auf deine Inspiration. Im folgenden führen wir dich durch 7 kleine
        Schritte. Viel Spaß!
      </span>
    </v-row>
    <v-divider class="text-left ma-5"/>
    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Gib deiner Heimabend-Idee eine passende Überschrift.
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
    }
  },


  methods: {
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form1.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        title: this.data.title,
      };
    },
  },
};
</script>

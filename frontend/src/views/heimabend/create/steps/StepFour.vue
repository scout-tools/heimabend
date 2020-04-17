<template>
        <v-form
        ref="form4"
        v-model="valid"
      >
  <v-container>
    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Die Heimabend-Idee wird unter deinem Namen veröffentlicht.
        Nutze dafür gerne deinen Fahrtennamen.
      </span>
    </v-row>
    <v-row class="ma-3">
      <v-text-field
        outlined
        label="Dein Pfadfindername"
        v-model="data.createdBy"
        :rules="rules.createdBy"
        required>
      </v-text-field>
    </v-row>
    <v-row class="mt-6 ml-2">
      <span class="subtitle-1">
        Diese E-Mail Adresse ist nur für das Redaktions-Team bei evtuellen Rückfragen sichtbar.
      </span>
    </v-row>
    <v-row class="ma-3">
      <v-text-field
        outlined
        label="Deine E-Mail Adresse"
        v-model="data.createdByEmail"
      >
      </v-text-field>
    </v-row>
    <v-row v-if="isAuthenticated" class="ma-3">
      <v-switch
        v-model="data.isActive"
        color="secondary"
        label="Dieser Heimabend ist öffentlich sichtbar.">
      </v-switch>
    </v-row>
    <v-row class="ma-3">
      <v-checkbox
        color="green"
        v-model="agreeBox"
        :rules="[v => !!v || 'Nur mit der Einverständniserklärung kannst du Ideen einreichen']"
        label="Ich möchte, dass diese Heimabend-Idee, nach einer inhaltlichen Prüfung,
          veröffentlicht
          wird und ich bin damit einverstanden, dass diese Heimabend-Idee später verändert,
          gekürzt oder ergänzt werden könnte. Dabei habe ich weder Textbausteine noch Bilder
          unrechtmäßigmäßig verwendet oder kopiert."
        required
      >
      </v-checkbox>
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
        @click="finish()"
      >
        Absenden
      </v-btn>
    </v-row>
  </v-container>
  </v-form>
</template>

<script>

export default {

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    e6: 1,
    dialog: false,
    valid: true,
    showError: false,
    showSuccess: false,
    timeout: 3000,
    responseObj: null,
    agreeBox: false,
    isEditorValid: true,
    rules: {
      title: [
        v => !!v || 'Titel ist erforderlich',
        v => (v && v.length >= 10) || 'Der Titel braucht mehr als 10 Zeichen',
        v => (v && v.length <= 40) || 'Der Titel darf nicht mehr als 40 Zeichen haben',
      ],
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Thema ist erforderlich',
      ],
      createdBy: [
        v => (v && v.length >= 3) || 'Der Name braucht mindestens drei Zeichen',
      ],
    },
    data: {
      createdBy: null,
      createdByEmail: '',
      isActive: false,
    },
    levelFilter: [0, 1, 2],
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    getOrange() {
      if (this.levelFilter) {
        return this.levelFilter.includes(0);
      }
      return false;
    },
    getBlue() {
      if (this.levelFilter) {
        return this.levelFilter.includes(1);
      }
      return false;
    },
    getRed() {
      if (this.levelFilter) {
        return this.levelFilter.includes(2);
      }
      return false;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    currentUsername() {
      return this.$store.getters.getUsername;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    isLargeProject() {
      return this.data.executionTimeRating === 0;
    },
    largeProjectButtomColor() {
      return this.isLargeProject ? 'limegreen' : 'lightgrey';
    },
    largeProjectIconColor() {
      return this.isLargeProject ? 'black' : 'grey';
    },
    isWithoutCosts() {
      return this.data.costsRating === 0;
    },
    withoutCostsButtomColor() {
      return this.isWithoutCosts ? 'limegreen' : 'lightgrey';
    },
    withoutCostsIconColor() {
      return this.isWithoutCosts ? 'red darken-2' : 'grey';
    },
    getClassForTextContentSteps() {
      return this.isMobil ? 'mx-0 px-1' : '';
    },
  },
  created() {
    this.agreeBox = !!this.$store.getters.isAuthenticated;
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },


  methods: {
    prevStep() {
      this.$emit('prevStep');
    },

    finish() {
      if (!this.$refs.form4.validate()) {
        return;
      }
      this.$emit('finish');
    },
    getData() {
      return {
        createdBy: this.data.createdBy,
        createdByEmail: this.data.createdByEmail,
        isActive: this.data.isActive,
      };
    },
  },
};
</script>

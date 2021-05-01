<template>
        <v-form
        ref="form8"
        v-model="valid"
      >
  <v-container>
    <v-row class="ma-3">
      <v-text-field
        v-model="data.createdBy"
        autofocus
        :rules="rules.createdBy"
        label="Dein Pfadfindername"
        prepend-icon="mdi-card-text"
        required
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{
                'Die Heimabend-Idee wird unter deinem Namen veröffentlicht.' +
                'Nutze dafür gerne deinen Fahrtennamen.'
              }}
            </span>
          </v-tooltip>
        </template>
      </v-text-field>
    </v-row>
    <v-row class="ma-3">
      <v-text-field
        v-model="data.createdByEmail"
        autofocus
        label="Deine E-Mail Adresse"
        prepend-icon="mdi-card-text"
        required
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{
                'Diese E-Mail Adresse ist nur für das Redaktions-Team bei' +
                'evtuellen Rückfragen zu deiner Heimabend-Idee sichtbar.'
              }}
            </span>
          </v-tooltip>
        </template>
      </v-text-field>
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
        <v-btn class="mx-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
      <v-btn
        color="success"
        @click="finish()"
      >
        Absenden
        <v-icon right>
          mdi-content-save-all
        </v-icon>
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
  }),
  props: {
    data: Object,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
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
      if (!this.$refs.form8.validate()) {
        return;
      }
      this.$emit('finish');
    },
    getData() {
      return {
        createdBy: this.data.createdBy,
        createdByEmail: this.data.createdByEmail,
      };
    },
  },
};
</script>

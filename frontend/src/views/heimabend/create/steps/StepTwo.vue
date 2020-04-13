<template>
        <v-form
        ref="form2"
        v-model="valid"
      >
  <v-container>
    <v-row class="mt-6 ml-4">
      <span class="subtitle-1">
        Füge hier alle Materialien hinzu. Bestätige jede Objekt mit "Enter".
      </span>
    </v-row>
    <v-row>
      <v-col class="pa-10" cols="12">
        <v-combobox
          outlined
          autofocus
          v-model="data.material"
          label="Material Liste"
          multiple
          required
          chips
        ></v-combobox>
      </v-col>
    </v-row>

    <v-divider class="my-2"/>

    <v-row no-gutters>

    <v-row class="mt-6 ml-4">
      <span class="subtitle-1">
        Wähle so viele passende Themen zu deinen Heimabend aus wie möglich?
      </span>
    </v-row>
        <v-sheet class="pa-8">
          <v-switch
          v-model="data.isPossibleInside"
          color="secondary"
          label="Dieser Heimabend ist Drinnen in einem Haus durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleOutside"
          color="secondary"
          label="Dieser Heimabend ist Draußen im z.B. Garten oder Wald durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPrepairationNeeded"
          color="secondary"
          label="Dieser Heimabend benötigt Zeit in der Vorbereitung?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleDigital"
          color="secondary"
          label="Ist Online mit deiner Sippe durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleAlone"
          color="secondary"
          label="Ist alleine durchführbar?">
        </v-switch>
        </v-sheet>
    </v-row>

    <v-row justify="center">
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
    e6: 1,
    dialog: false,
    valid: true,
    data: {
      material: '',
      isPossibleInside: false,
      isPossibleOutside: false,
      isPrepairationNeeded: false,
      isPossibleDigital: false,
      isPossibleAlone: false,
    },
    levelFilter: [0, 1, 2],
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getCustomText() {
      const value = this.data.description;
      if (!value) {
        return 'Beschreibung ist erforderlich';
      }
      if (value && value.length <= 75) {
        return 'Name must be more than 75 characters';
      }
      if (value && value.length >= 2500) {
        return 'Beschreibung ist zu lang';
      }
      return 'Ok';
    },
  },

  mounted() {
  },

  created() {
  },


  methods: {
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form2.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return this.data;
    },
  },
};
</script>

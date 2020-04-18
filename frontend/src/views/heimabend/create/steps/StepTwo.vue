<template>
  <v-form
    ref="form2"
    v-model="valid"
  >
  <v-container>
    <v-row class="mt-6 ml-4">
      <span class="subtitle-1">
        Füge hier alle Materialien hinzu. Bestätige jedes Objekt mit "Enter".
      </span>
    </v-row>
    <v-row>
      <v-col class="pa-10" cols="12">
        <v-combobox
          outlined
          autofocus
          v-model="data.materialArray"
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
        Beantworte jede Frage für deinen Heimabend.
      </span>
    </v-row>
        <v-sheet class="pa-8">
          <v-switch
          v-model="data.isPossibleInside"
          color="secondary"
          label="Ist diese Heimabend-Idee drinnen (in einem Haus) durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleOutside"
          color="secondary"
          label="Ist diese Heimabend-Idee draußen (im z.B. Garten oder Wald) durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPrepairationNeeded"
          color="secondary"
          label="Benötigt diese Heimabend-Idee benötigt Zeit zur Vorbereitung?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleDigital"
          color="secondary"
          label="Ist diese Heimabend-Idee online mit deiner Gruppe durchführbar?">
        </v-switch>
        <v-switch
          v-model="data.isPossibleAlone"
          color="secondary"
          label="Ist diese Heimabend-Idee alleine durchführbar?">
        </v-switch>
        </v-sheet>
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
    e6: 1,
    dialog: false,
    valid: true,
    data: {
      materialArray: [],
      isPossibleInside: true,
      isPossibleOutside: true,
      isPrepairationNeeded: false,
      isPossibleDigital: false,
      isPossibleAlone: false,
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
      if (!this.$refs.form2.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        material: this.data.materialArray,
        isPossibleInside: this.data.isPossibleInside,
        isPossibleOutside: this.data.isPossibleOutside,
        isPrepairationNeeded: this.data.isPrepairationNeeded,
        isPossibleDigital: this.data.isPossibleDigital,
        isPossibleAlone: this.data.isPossibleAlone,
      };
    },
  },
};
</script>

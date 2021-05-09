<template>
  <v-form
    ref="form1"
    v-model="valid"
  >
  <v-container fluid>
    <v-row class="mt-6 ml-2">
      <v-col cols="8">
      <span class="text-left subtitle-1">
        Willkommen bei der <b> Heimabenderstellung </b>. <br>
        <br>
        Viele Pfadfinder freuen sich
        schon auf deine Inspiration. Im folgenden führen wir dich durch 7 kleine
        Schritte. Viel Spaß!
      </span>
      </v-col>
      <v-col cols="4" align="center" justify="center">
        <v-img :src="require('@/assets/inspi/inspi_happy.webp')" max-width="80" />
      </v-col>
    </v-row>
    <v-divider class="text-left ma-5"/>
    <v-row class="ma-4">
      <v-text-field
        v-model="data.title"
        autofocus
        :counter="40"
        :rules="rules.title"
        label="Überschrift"
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
              {{ 'Gib deiner Heimabend-Idee eine passende Überschrift.' }}
            </span>
          </v-tooltip>
        </template>
      </v-text-field>
    </v-row>

    <v-divider class="my-2"/>

      <v-row class="ma-3" justify="center">
        <v-btn color="error" class="mx-1" @click="cancel()">
      <v-icon left>
        mdi-close
      </v-icon>
          Abbrechen
        </v-btn>
        <v-btn class="mx-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right>
            mdi-chevron-right
          </v-icon>
        </v-btn>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                v-on="on"
                icon
                class="mx-1"
                color="secondary"
                @click="nextStep(true)"
              >
                <v-icon>
                  mdi-debug-step-over
                </v-icon>
              </v-btn>
            </template>
            <span>
              {{ 'Schritt überspringen' }}
            </span>
          </v-tooltip>
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
    rules: {
      title: [
        v => !!v || 'Überschrift ist erforderlich.',
        v => (v && v.length >= 10) || 'Die Überschrift ist zu kurz.',
        v => (v && v.length <= 40) || 'Die Überschtift ist zu lang.',
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
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
  },


  methods: {
    cancel() {
      this.$emit('cancel');
    },
    nextStep(skip = false) {
      if (!this.$refs.form1.validate() && !skip) {
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

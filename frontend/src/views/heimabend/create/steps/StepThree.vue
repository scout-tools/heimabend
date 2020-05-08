<template>
  <v-form
    ref="form3"
    v-model="valid"
  >
<v-container>
  <v-row class="mt-6 ml-4">
    <span class="subtitle-1">
      Wähle so viele Themen aus, wie zu deiner Heimabend-Idee passen.
    </span>
  </v-row>
  <v-row class="ma-6">
    <v-select
      v-model="data.tags"
      :items="tags"
      item-value="id"
      item-color="color"
      :rules="rules.tags"
      item-text="name"
      deletable-chips
      chips
      label="Wähle aus der Liste bis zu 5 Themen aus."
      no-data-text="Wähle aus der Liste Themen aus."
      multiple
      outlined
    ></v-select>
  </v-row>
  <v-divider class="my-2"/>
  <v-row class="mt-6 ml-4">
    <span class="subtitle-1">
      Welche Kosten entstehen bei der Durchführung dieser Heimabend-Idee?
    </span>
  </v-row>

  <v-row>
    <v-tooltip
      nudge-left="80"
      open-on-hover
      bottom
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
          text
        >
          <v-rating
            v-model="data.costsRating"
            emptyIcon="mdi-currency-usd"
            fullIcon="mdi-currency-usd"
            color="orange"
            background-color="grey"
            min="0"
            length="3"
          ></v-rating>
        </v-btn>
      </template>
      <span>
        <p class="text-left">
        Stufe 1: 0,00€ - 0,50€ pro Person <br>
        Stufe 2: 1€ - 2€ pro Person <br>
        Stufe 3: mehr als 2€ pro Person <br>
        </p>
      </span>
    </v-tooltip>
    <v-switch
      color="secondary"
      v-model="isWithoutCosts"
      small
      label="Keine Kosten"
      class="ma-2"
      @click="onResetPriceClick()"
    >
      Ohne Kosten
    </v-switch>
  </v-row>

  <v-row class="mt-6 ml-4">
    <span class="subtitle-1">
      Wieviel Durchführungszeit ist erforderlich?
    </span>
  </v-row>
  <v-row>
    <v-tooltip
      nudge-left="80"
      open-on-hover
      bottom
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
          text
        >
        <v-rating
          v-model="data.executionTimeRating"
          emptyIcon="mdi-clock"
          fullIcon="mdi-clock"
          color="black"
          background-color="grey"
          min="0"
          length="3"
        ></v-rating>
          </v-btn>
        </template>
        <span>
          <p class="text-left">
          Stufe 1: bis 30 min <br>
          Stufe 2: 30 min - 60 min<br>
          Stufe 3: mehr als 60 min<br>
          </p>
        </span>
      </v-tooltip>
    <v-switch
      color="secondary"
      v-model="isLargeProject"
      small
      label="Handelt es sich um ein Großprojekt?"
      class="ma-2"
      @click="onLargeProjectClick()"
    >
      Ohne Kosten
    </v-switch>
    </v-row>
    <v-divider class="my-2"/>
    <v-row class="mt-6 ml-4">
      <span class="subtitle-1">
        Für welche Stufe ist die Heimabend-Idee geeignet?
      </span>
    </v-row>
    <v-row class="mx-6">
      <v-switch
      color="secondary"
      v-model="data.isLvlOne"
      label="Geeignet für die Wölflingsstufe (7 bis 10 Jahren).">
      </v-switch>
        <v-img
          v-if="!isMobil"
          class="ma-4"
          :src="require('@/assets/wolfskopf.png')"
          max-width="40"
        />
    </v-row>
    <v-row class="mx-6">
      <v-switch
      color="secondary"
      v-model="data.isLvlTwo"
      label="Geeignet für die Pfadfinderstufe (11 bis 14 Jahren).">
      </v-switch>
        <v-img
          v-if="!isMobil"
          class="ma-4"
          :src="require('@/assets/knot_blue.png')"
          max-width="40"
        ></v-img>
    </v-row>
    <v-row class="mx-6">
      <v-switch
      color="secondary"
      v-model="data.isLvlThree"
      label="Geeignet für die Roverstufe (ab 15 Jahren).">
      </v-switch>
        <v-img
          v-if="!isMobil"
          class="ma-4"
          :src="require('@/assets/knot_red.png')"
          max-width="40"
        ></v-img>
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
        @click="nextStep()"
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
    rules: {
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Thema ist erforderlich',
      ],
    },
    data: {
      executionTimeRating: 1,
      costsRating: 1,
      isLvlOne: true,
      isLvlTwo: true,
      isLvlThree: true,
    },
    valid: true,
  }),

  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    currentUsername() {
      return this.$store.getters.getUsername;
    },
    tags() {
      return this.$store.getters.tags;
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

  mounted() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
      if (this.data.tags && this.data.tags.length) {
        this.data.tags = this.setIntTags(this.data.tags);
      }
    }
  },

  created() {
    this.agreeBox = !!this.$store.getters.isAuthenticated;
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },


  methods: {
    onResetPriceClick() {
      this.data.costsRating = 0;
    },
    onLargeProjectClick() {
      this.data.executionTimeRating = 0;
    },
    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    setIntTags(urlTags) {
      const tagList = [];
      urlTags.forEach((tag) => {
        tagList.push(this.convertUrlToId(tag));
      });
      return tagList;
    },
    onNextClick() {
      if (!this.$refs.form1.validate()
        || this.getCustomText !== 'Ok') {
        return false;
      }
      this.e6 = 2;
      return true;
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
        isLvlOne: this.data.isLvlOne,
        isLvlTwo: this.data.isLvlTwo,
        isLvlThree: this.data.isLvlThree,
        tags: this.data.tags,
        costsRating: this.data.costsRating,
        executionTimeRating: this.data.executionTimeRating,
      };
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(40, 158, 40)
}
.customerRequired {
  text-align: left;
}

.limegreen {
    background-color: rgb(40, 158, 40) !important;
}

.v-btn:before {
    background-color: transparent !important;
}
</style>

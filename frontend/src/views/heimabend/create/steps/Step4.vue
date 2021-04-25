<template>
  <v-form ref="form4" v-model="valid">
    <v-container>
      <v-row class="mt-6 ml-4">
        <span class="subtitle-1">
          Sammle hier bitte alles an Material, was für die Vorbereitung und
          Durchführung deiner Idee benötigt wird. Die einzelnen Objekte kannst
          du jeweils mit „Enter“ bestätigen.“
        </span>
      </v-row>
      <v-row class="ma-4">
        <v-combobox
          outlined
          autofocus
          v-model="data.materialList"
          label="Material Liste"
          multiple
          chips
          prepend-icon="mdi-archive"
        >
          <template v-slot:selection="{ attrs, item, select, selected }">
            <v-chip
              v-bind="attrs"
              :input-value="selected"
              close
              @click="select"
              @click:close="remove(item)"
            >
              <strong>{{ item }}</strong
              >&nbsp;
            </v-chip>
          </template>
        </v-combobox>
      </v-row>

      <v-row class="ma-3" justify="center">
        <v-btn class="mr-5" @click="prevStep()"> Zurück </v-btn>

        <v-btn color="primary" @click="nextStep(n)"> Weiter </v-btn>
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
    getSideBarTags() {
      if (this.tags && this.tagCategory) {
        const sideBarTagCategories = this.tagCategory.filter(item => item.item === 9);
        const sideBarTags = this.filterTagByCategory(sideBarTagCategories[0].id);
        return sideBarTags;
      }
      return [];
    },
  },

  watch: {
    data() {
      if (this.data.materialList && this.data.materialList.length === 0) {
        this.convertMaterialString(this.data.material);
      }
    },
  },

  methods: {
    convertMaterialString(array) {
      if (array && array.length) {
        this.data.materialList = array.split(',');
      }
    },
    remove(item) {
      this.data.materialList.splice(this.data.materialList.indexOf(item), 1);
      this.data.materialList = [...this.data.materialList];
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
        materialList: this.data.materialList,
      };
    },
  },
};
</script>

<template>
  <v-form ref="form4" v-model="valid">
    <v-container fluid class="ma-4">
      <v-row class="mt-6 ml-4">
        <span class="subtitle-1">
          Sammle hier bitte alles an Material, was für die Vorbereitung und
          Durchführung deiner Idee benötigt wird. Bitte gib die Stückzahl für 6
          Personen an.
        </span>
      </v-row>
      <v-row justify="center">
        <div v-for="(item, index) in items" :key="index">
          <MaterialItem
            :item="item"
            :units="units"
            :names="names"
            @deleteItem="deleteItem"
          />
        </div>
      </v-row>
      <v-row justify="start">
        <v-btn color="success" @click="addItem">
          <v-icon left> mdi-plus </v-icon>
          Neuer Gegenstand
        </v-btn>
      </v-row>
      <v-row justify="center">
        <v-btn class="mx-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="mx-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon> mdi-chevron-right </v-icon>
        </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
// eslint-disable-next-line
import axios from 'axios';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';
// eslint-disable-next-line
import MaterialItem from '@/components/form/MaterialItem.vue';

export default {
  mixins: [serviceMixin],
  components: {
    MaterialItem,
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    n: 0,
    dialog: false,
    valid: true,
    units: [],
    names: [],
    count: -1,
    forXPersons: 6,
    items: [],
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
  created() {
    this.getMaterialUnits();
    this.getMaterialName();
    this.refreshStoreItems('message-type', 'setMessageType');
    this.loadMaterialData();
  },
  methods: {
    loadMaterialData() {
      if (this.isUpdate) {
        this.getService2(
          'material-item',
          new URLSearchParams({ event: this.$route.params.id }),
        ).then((response) => {
          this.items = response.data;
        });
      }
    },
    deleteItem(item) {
      const arrayNo = this.items.indexOf(item);
      this.items.splice(arrayNo, 1);
    },
    addItem() {
      this.items.push({
        id: this.count,
        unitId: 1,
        quantity: 1,
        name: '',
      });
      this.count = this.count - 1;
    },
    getMaterialUnits() {
      this.getService('material-unit').then((res) => {
        this.units = res.data;
      });
    },
    getMaterialName() {
      this.getService('material-name').then((res) => {
        this.names = res.data;
      });
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
      return this.items;
    },
  },
};
</script>

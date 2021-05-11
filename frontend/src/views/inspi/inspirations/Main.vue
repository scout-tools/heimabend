<template>
  <v-container fluid>
    <v-spacer class="py-3" />
    <EventSlider :data="data1" titel="Top Aufrufe"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data2" titel="Neusten Heimabende"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data3" titel="Mit Abstand Heimabende"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data4" titel="Nachhaltige Heimabende"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data5" titel="Meuten Heimabende"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data6" titel="Sippen Heimabende"/>
    <v-spacer class="py-3" />
    <EventSlider :data="data7" titel="Roverrunden Heimabende"/>

  </v-container>
</template>

<script>
// eslint-disable-next-line
import EventSlider from '@/components/slider/Events.vue';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';


export default {
  mixins: [serviceMixin],
  components: {
    EventSlider,
  },
  data: () => ({
    model: null,
    data1: [],
    data2: [],
    data3: [],
    data4: [],
    data5: [],
    data6: [],
    data7: [],
  }),
  methods: {
    loadData() {
      this.getTopViews().then((response) => {
        this.data1 = response.data;
      });
      this.getService2(
        'event',
        new URLSearchParams({ limit: '15', ordering: '-created_at' }),
      ).then((response) => {
        this.data2 = response.data.results;
      });
      this.getService2(
        'event',
        new URLSearchParams({ filterTags: '54', limit: '15', ordering: '?' }),
      ).then((response) => {
        this.data3 = response.data.results;
      });
      this.getService2(
        'event',
        new URLSearchParams({ filterTags: '32', limit: '15', ordering: '?' }),
      ).then((response) => {
        this.data4 = response.data.results;
      });
      this.getService2(
        'event',
        new URLSearchParams({ filterTags: '50', limit: '15', ordering: '?' }),
      ).then((response) => {
        this.data5 = response.data.results;
      });
      this.getService2(
        'event',
        new URLSearchParams({ filterTags: '51', limit: '15', ordering: '?' }),
      ).then((response) => {
        this.data6 = response.data.results;
      });
      this.getService2(
        'event',
        new URLSearchParams({ filterTags: '52', limit: '15', ordering: '?' }),
      ).then((response) => {
        this.data7 = response.data.results;
      });
    },
  },
  created() {
    this.loadData();
    this.$store.commit('setHeaderString', 'Inspiration');
  },
};
</script>

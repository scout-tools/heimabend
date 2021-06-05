<template>
  <v-container fluid>
    <v-spacer class="py-3" />
    <EventSlider :data="data1" titel="Top Aufrufe" />
    <v-spacer class="py-3" />
    <EventSlider :data="data2" titel="Neusten Heimabende" />
    <v-spacer class="py-3" />
    <EventSlider :data="data3" titel="Mit-Abstand-Heimabende" />
    <v-spacer class="py-3" />
    <EventSlider :data="data4" titel="Nachhaltige Heimabende" />
    <v-spacer class="py-3" />
    <EventSlider :data="data5" titel="Meuten-Heimabende" />
    <v-spacer class="py-3" />
    <EventSlider :data="data6" titel="Sippen-Heimabende" />
    <v-spacer class="py-3" />
    <EventSlider :data="data7" titel="Roverrunden-Heimabende" />
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
    data1: [{}, {}, {}, {}, {}, {}, {}],
    data2: [{}, {}, {}, {}, {}, {}, {}],
    data3: [{}, {}, {}, {}, {}, {}, {}],
    data4: [{}, {}, {}, {}, {}, {}, {}],
    data5: [{}, {}, {}, {}, {}, {}, {}],
    data6: [{}, {}, {}, {}, {}, {}, {}],
    data7: [{}, {}, {}, {}, {}, {}, {}],
  }),
  methods: {
    loadData() {
      this.getTopViews().then((response1) => {
        this.data1 = response1.data;
      });
      this.getService2(
        'event',
        new URLSearchParams({ limit: '15', ordering: '-created_at' }),
      ).then((response2) => {
        this.data2 = response2.data.results;
        this.getService2(
          'event',
          new URLSearchParams({ filterTags: '54', limit: '15', ordering: '?' }),
        ).then((response3) => {
          this.data3 = response3.data.results;
          this.getService2(
            'event',
            new URLSearchParams({ filterTags: '32', limit: '15', ordering: '?' }),
          ).then((response4) => {
            this.data4 = response4.data.results;
            this.getService2(
              'event',
              new URLSearchParams({ filterTags: '50', limit: '15', ordering: '?' }),
            ).then((response5) => {
              this.data5 = response5.data.results;
              this.getService2(
                'event',
                new URLSearchParams({ filterTags: '51', limit: '15', ordering: '?' }),
              ).then((response6) => {
                this.data6 = response6.data.results;
                this.getService2(
                  'event',
                  new URLSearchParams({ filterTags: '52', limit: '15', ordering: '?' }),
                ).then((response7) => {
                  this.data7 = response7.data.results;
                });
              });
            });
          });
        });
      });
    },
  },
  created() {
    this.loadData();
    this.$store.commit('setHeaderString', 'Inspiration');
  },
};
</script>

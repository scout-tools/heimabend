<template>
  <v-card flat v-if="data.length" class="mx-auto" justify="center">
    <v-card-title class="pa-0" justify="center"> {{ titel }} </v-card-title>
    <v-slide-group
      v-if="data.length"
      class="pa-0"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="item in data" :key="item.id" v-slot="{ active, toggle }">
        <v-card
          class="ma-2"
          height="180"
          width="320"
          @click="onEventClicked(item.id)"
        >
          <HeimabendCardHeader :item="item"/>
          <v-img :src="getImageLink(item)" height="115px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
    <v-progress-circular
      v-else
      indeterminate
      size="100"
      color="white"
    ></v-progress-circular>
  </v-card>
</template>

<script>
// eslint-disable-next-line import/no-unresolved
import HeimabendCardHeader from '@/components/heimabend/CardHeader.vue';

export default {
  props: {
    data: Array,
    titel: String,
  },
  components: {
    HeimabendCardHeader,
  },
  methods: {
    getImageLink(item) {
      if (item.headerImage) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${item.headerImage}.default.jpeg`;
      }
      return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/inspi_v2.png`;
    },
    onEventClicked(id) {
      this.$router.push({
        name: 'heimabendDetails',
        params: { id },
      });
    },
  },
};
</script>

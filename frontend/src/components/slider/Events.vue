<template>
  <v-card flat class="mx-auto" justify="center">
    <v-card-title class="pa-0" justify="center"> {{ titel }} </v-card-title>
    <v-slide-group
      class="pa-0"
      active-class="success"
      show-arrows
    >
      <v-slide-item v-for="n in data" :key="n.id" v-slot="{ active, toggle }">
        <v-card
          class="ma-2"
          height="170"
          width="290"
          @click="onEventClicked(n.id)"
        >
          <v-card-subtitle class="whiteText justify-center text-center primary">
            {{ n.title }}
          </v-card-subtitle>
          <v-img :src="getImageLink(n)" height="115px"></v-img>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-card>
</template>

<script>
export default {
  props: {
    data: Array,
    titel: String,
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

<template>
  <v-card flat class="mx-auto" justify="center">
    <v-card-title class="pa-0 ml-5" justify="center"> {{ titel }} </v-card-title>
    <v-slide-group
      v-if="data.length"
      class="pl-0"
      active-class="success"
      show-arrows
    >
      <v-slide-item
        v-for="item in data"
        :key="item.id"
        v-slot="{ active, toggle }"
      >
        <v-card
          class="ma-2"
          height="200"
          width="280"
          @click="onEventClicked(item.id)"
        >
          <HeimabendCardHeader :item="item" :preview="true" />
          <v-img
            class="pa-5 background-sky"
            :src="getImageLink(item)"
            :lazy-src="getTempImage()"
            height="140"
            contain
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
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
      if (item.headerImage && item.headerImage.imageUuid) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${item.headerImage.imageUuid.imageUuid}.default.jpeg`;
      }
      return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/inspi_v2.png`;
    },
    getTempImage() {
      return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/inspi_v2.png`;
    },
    onEventClicked(id) {
      this.$router.push({
        name: 'heimabendDetails',
        params: { id },
      });
      this.$router.go();
    },
  },
};
</script>

<style scoped>
.background-sky {
  background: rgb(199,216,252);
  background: linear-gradient(41deg,
  rgba(199,216,252,1) 0%,
  rgba(255,255,255,1) 100%);
}
</style>

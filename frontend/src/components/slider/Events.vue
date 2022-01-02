<template>
  <v-card flat v-if="data.length" class="mx-auto" justify="center">
    <v-card-title class="pa-0 ml-5" justify="center"> {{ titel }} </v-card-title>
    <v-slide-group
      v-if="data.length"
      class="pa-0"
      active-class="success"
    >
      <v-hover v-slot="{ hover }" v-for="(item, index) in data"
        :key="`${titel}-${item.id}-${index}`">
        <v-slide-item v-slot="{ active, toggle }">
          <template>
            <div>
<!--          height: 64px (header) + 140px (img) -->
              <v-card
                class="ma-2"
                height="204"
                width="280"
                @click="onEventClicked(item.id)"
              >
                <v-expand-transition>
                  <v-card
                    max-height="100%"
                    v-if="hover"
                    class="v-card--reveal d-flex transition-fast-in-fast-out
                         blue-grey darken-2 display-3 white--text"
                  >
                    <v-card-text class="white--text">
                      <p v-html="item.description"/>
                    </v-card-text>
                  </v-card>
                </v-expand-transition>
                <HeimabendCardHeader :item="item" :preview="true"/>
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
            </div>
          </template>
        </v-slide-item>
      </v-hover>
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

<style lang="scss" scoped>
.v-card--reveal {
  bottom: 0;
  opacity: 0.9;
  position: absolute;
  z-index: 100;
}

.background-sky {
  background: rgb(199,216,252);
  background: linear-gradient(41deg,
    rgba(199,216,252,1) 0%,
    rgba(255,255,255,1) 100%);
}
</style>

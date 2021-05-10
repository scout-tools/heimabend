<template>
  <v-card flat v-if="data.length" class="mx-auto" justify="center">
    <v-card-title class="pa-0" justify="center"> {{ titel }} </v-card-title>
    <v-slide-group
      v-if="data.length"
      class="pa-0"
      active-class="success"
    >
      <v-hover v-slot="{ hover }" v-for="item in data" :key="item.id">
        <v-slide-item v-slot="{ active, toggle }">
          <template>
            <div>
              <v-card
                class="ma-2"
                height="180"
                width="320"
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
                <HeimabendCardHeader :item="item" disable-tooltip/>
                <v-img :src="getImageLink(item)" height="115px"/>
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
    onEventClicked(id) {
      this.$router.push({
        name: 'heimabendDetails',
        params: { id },
      });
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
</style>

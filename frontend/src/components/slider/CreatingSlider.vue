<template>
  <v-container>
    <v-row align="center" justify="center">
      <span class="subtitle-1 font-weight-black">
        {{ headerText }}
      </span>
    </v-row>
    <v-row align="center" justify="center">
        <v-slider
          class="ma-2"
          v-model="data"
          :tick-labels="labels"
          min="0"
          :max="labels.length-1"
          ticks="always"
          thumb-label="always"
          tick-size="4"
          :color="color"
        >
          <template v-slot:thumb-label="{ value }">
            <v-icon color="white">
              {{ icon }}
            </v-icon>
          </template>
        </v-slider>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    data: Object,
    labels: Array,
    icon: String,
    color: String,
    headerText: String,
  },
  data: () => ({
    valid: true,
    n: 0,
    difficultlevel: 0,
  }),
  computed: {
  },

  methods: {
  },
};
</script>

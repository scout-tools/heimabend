<template>
    <v-tooltip
      nudge-left="80"
      bottom
    >
      <template
        v-slot:activator="{ on }"
      >
        <div
          class="d-flex flex-column"
          :class="getDivClass()"
          >
          <v-btn
            v-on="on"
            dense
            text
            depressed
            class="mx-0 px-0"
          >
            <v-icon
              v-if="customIcon !== 'wolf' && customIcon !== 'scout' && customIcon !== 'rover'"
              dense
              :color="isActiveState ?
                customColor + ' darken-2' : 'grey'"
            >
              {{ customIcon }}
            </v-icon>

            <v-img
              v-if="customIcon == 'wolf'"
              class="ma-0 pa-0"
              :src="require('@/assets/wolfskopf.png')"
              max-width="28"
            />

            <v-img
              v-if="customIcon == 'scout'"
              class="ma-0 pa-0"
              :src="require('@/assets/knot_blue.png')"
              max-width="28"
            />

            <v-img
              v-if="customIcon == 'rover'"
              class="ma-0 pa-0"
              :src="require('@/assets/knot_red.png')"
              max-width="28"
            />

            <span
              class="subtitle-2 mx-1"
              :class="getColotClass"
              v-if="!isMobil"
            >
              {{ customText }}
            </span>
          </v-btn>
          <v-row justify="center">
            <v-switch
              color="secondary"
              v-model="isActiveState"
              class="ma-0 pa-0"
              hide-details
              dense
              indeterminate
            >
            </v-switch>
          </v-row>
        </div>
      </template>
      <span>
        {{ customTooltip }}
      </span>
    </v-tooltip>
</template>
<script>
export default {
  props: {
    customIcon: {
      type: String,
    },
    customColor: {
      type: String,
    },
    customText: {
      type: String,
    },
    customTooltip: {
      type: String,
    },
    customTrigger: {
      type: Boolean,
    },
    customVariable: {
      type: String,
    },
    customMutation: {
      type: String,
    },
  },
  data() {
    return {
      isActiveState: false,
    };
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getColotClass() {
      return this.isActiveState ? 'customer-color-activ' : 'customer-color-inactive';
    },
  },
  watch: {
    isActiveState(value) {
      this.$store.commit(this.customMutation, value);
      if (value) {
        // eslint-disable-next-line no-undef
        _paq.push(['trackEvent', 'ActivateFilter', this.customVariable]);
      }
    },
    customTrigger() {
      this.updateState();
    },
  },
  methods: {
    getDivClass() {
      return !this.isMobil ? 'mx-2' : 'mx-0';
    },
    updateState() {
      this.isActiveState = this.$store.getters[this.customVariable];
    },
  },
  mounted() {
    this.updateState();
  },
};
</script>

<style scoped>
.customer-color-activ {
  color: black !important;
}
.customer-color-inactive {
  color: gray !important;
}
</style>

<template>
  <div class="text-center">
    <v-bottom-sheet
      v-model="sheet"
      :hide-overlay="isHideOverlay"
      :persistent="isPersistent"
    >
      <v-sheet
        color="lightPrimary"
        class="text-center pa-3"
        height="160px"
      >
        <v-btn
          class="mt-3"
          color="error"
          @click="onButtonClick()"
        >Zustimmen</v-btn>
        <div class="py-3">Wir nutzen Cookies um
          um dein Nutzerverhalten besser zu verstehen und die Seite zu verbessern.
        </div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  data: () => ({
    sheet: true,
    isHideOverlay: true,
    isPersistent: true,
  }),
  methods: {
    onButtonClick() {
      this.$store.commit('acceptedPrivacy', true);
    },
  },
};
</script>

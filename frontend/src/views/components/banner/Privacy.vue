<template>
  <div class="text-center">
    <v-bottom-sheet
      v-model="sheet"
      :hide-overlay="isHideOverlay"
      :persistent="isPersistent"
    >
      <v-sheet class="text-center" height="200px">
        <v-btn
          class="mt-6"
          color="error"
          @click="onButtonClick()"
        >Zustimmen</v-btn>
        <div class="py-3">Diese Seite verwendet Cookies und nutzt sie
          um das Nutzerverhalten besser zu verstehen und die Seite zu verbessern.</div>
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

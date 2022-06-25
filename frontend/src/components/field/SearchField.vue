<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field
          v-model="search"
          append-icon="mdi-search"
          label="Suche"
          single-line
          hide-details
        />
        <v-spacer />
      </v-col>
      <v-col>
        <v-btn color="green" dark @click="$emit('onNewClicked')" class="mb-2">
          Neu
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    search: String,
  },
};
</script>

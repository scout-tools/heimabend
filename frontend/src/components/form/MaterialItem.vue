<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="1" align="center" justify="center">
        <v-text-field
          disabled
          v-model="item.id"
          label="id">
        </v-text-field>
      </v-col>
      <v-col cols="2" align="center" justify="center">
        <v-text-field
          label="Stückzahl"
          v-model="item.quantity"
        >
        </v-text-field>
      </v-col>
      <v-col cols="2" align="center" justify="center">
        <v-autocomplete
          label="Einheit"
          v-model="item.unitId"
          :items="units"
          auto-select-first
          item-text="name"
          item-value="id"
        />
      </v-col>
      <v-col cols="5" align="center" justify="center">
        <v-combobox
          label="Gegenstand"
          v-model="item.name"
          :items="names"
          item-text="name"
          item-value="name"
        />
      </v-col>
      <v-col cols="1" align="center" justify="center">
        <v-btn dark icon small color="red" @click="$emit('deleteItem', item)">
          <v-icon dark> mdi-close </v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    item: Object,
    units: Array,
    names: Array,
  },
};
</script>

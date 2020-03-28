<template>
  <v-select
    :items="items"
    v-model="selectedFilter"
    label="Filter"
    return-object
    hide-details
    item-value="id"
    single-line
    @change="onFilterChanged"
  >
    <template slot="selection" slot-scope="data">
      <v-icon>
        {{ data.item.icon }}
      </v-icon>
      <div>
        {{ data.item.text }}
      </div>
    </template>
    <template slot="item" slot-scope="data">
      <v-icon>
        {{ data.item.icon }}
      </v-icon>
      <v-list-item-content>
        <v-list-item-title>
          {{ data.item.text }}
        </v-list-item-title>
      </v-list-item-content>
    </template>
  </v-select>
</template>

<script>
export default {
  methods: {
    onFilterChanged(obj) {
      this.$store.commit('changeSorter', obj.id);
    },
  },
  computed: {
    selectedFilter: {
      get() {
        return this.$store.getters.getSorter;
      },
      set() {
        return false;
      },
    },
  },
  data() {
    return {
      items: [
        {
          id: 'random',
          text: 'Zufällige Sortierung',
          icon: 'mdi-dice-multiple-outline',
        },
        {
          id: 'newest',
          text: 'Neuste Zuerst',
          icon: 'mdi-timer',
        },
        {
          id: 'alpha',
          text: 'Titel A-Z',
          icon: 'mdi-sort-descending',
        },
      ],
      toggle_multiple: [1, 2, 3],
    };
  },
};
</script>

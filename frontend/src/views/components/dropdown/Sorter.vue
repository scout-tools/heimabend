<template>
  <v-select
    :items="items"
    v-model="selectedFilter"
    label="Filter"
    return-object
    hide-details
    outlined
    dense
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
        return this.$store.getters.sorter;
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
          id: '-createdAt',
          text: 'Neuste Zuerst',
          icon: 'mdi-timer',
        },
        {
          id: '-like_score',
          text: 'Beste Bewertung',
          icon: 'mdi-star-face',
        },
        // {
        //   id: 'random',
        //   text: 'Zufällige Sortierung',
        //   icon: 'mdi-dice-multiple-outline',
        // },
        {
          id: 'title',
          text: 'Titel A-Z',
          icon: 'mdi-sort-descending',
        },
      ],
    };
  },
};
</script>

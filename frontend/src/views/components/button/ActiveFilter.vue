<template>
  <v-chip-group column>
    <v-chip label close :small="isMobil"
      v-for="(tag, index) in getActiveTags"
      :color="tag.color"
      :key="index"  @click:close="onCloseChip(tag)">
      {{ tag.name }}
    </v-chip>
  </v-chip-group>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  methods: {
    onCloseChip(value) {
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);

      if (value && value.id) {
        this.$store.commit('removeOneFilter', value.id);
      } else if (value.type && value.type === 'search') {
        this.$store.commit('setSearchInput', '');
      } else {
        this.$store.commit('removeNumberFilter', value);
      }
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
      'filterTags',
      'numberFilter',
      'searchInput',
    ]),
    getActiveTags() {
      let tags = [];
      // eslint-disable-next-line
      if ((this.mandatoryFilter || this.filterTags) && (this.mandatoryFilter.length || this.filterTags.length)) {
        tags = this.tags.filter(
          item => this.mandatoryFilter.includes(item.id) || this.filterTags.includes(item.id),
        );
      }
      tags = tags.concat(this.numberFilter);
      if (this.searchInput) {
        tags.push({
          name: `Suche: ${this.searchInput}`,
          value: this.searchInput,
          type: 'search',
        });
      }

      return tags;
    },
  },
};
</script>

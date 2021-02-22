<template>
    <v-tooltip
      slot="append"
      bottom
      nudge-left="80"
    >
      <template v-slot:activator="{ on }">
        <v-chip
          :filter="filter"
          light
          :small="small"
          :close="close"
          v-on="on"
          v-bind:class="[cursor, margin]"
          :color="tag.color"
          :value="tag.id"
          @click:close="$emit('click:close', tag.id)"
        >
          {{ getTagNameById(tag.id) }}
        </v-chip>
      </template>
      <span>
          {{  getDescriptionNameById(tag.id) }}
        </span>
    </v-tooltip>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'ChipTooltip',
  props: ['tag', 'margin', 'small', 'cursor', 'close', 'filter'],
  computed: {
    ...mapGetters([
      'tags',
    ]),
  },
  methods: {
    getTagNameById(idString) {
      let id;
      if (idString && typeof idString === 'string') {
        const idStringArray = idString.split('/');
        id = idStringArray[idStringArray.length - 2];
      } else {
        id = idString;
      }
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      return '';
    },
    getDescriptionNameById(idString) {
      let id;
      if (idString && typeof idString === 'string') {
        const idStringArray = idString.split('/');
        id = idStringArray[idStringArray.length - 2];
      } else {
        id = idString;
      }
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.description) {
        return returnTag.description;
      }
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      return 'Keine Beschreibung vorhanden';
    },
  },
};
</script>

<style scoped>

</style>

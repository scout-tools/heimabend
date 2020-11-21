<template>
<div>
    <v-chip
      class="mr-1"
      light
      small
      close
      v-for="(tag, index) in getActiveTags"
      :key="index"
      :color="tag.color"
      @click:close="onCloseChip(tag.id)"
    >
      {{ tag.name }}
    </v-chip>
</div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  methods: {
    onCloseChip(value) {
      this.$store.commit('removeOneFilter', value);
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
    ]),
    getActiveTags() {
      if (this.mandatoryFilter && this.mandatoryFilter.length) {
        return this.tags.filter(item => this.mandatoryFilter.includes(item.id)
          || this.filterTags.includes(item.id));
      }
      return [];
    },
  },
};
</script>

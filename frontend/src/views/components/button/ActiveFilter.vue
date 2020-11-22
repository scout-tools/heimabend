<template>
<div>
  <v-chip-group >
    <v-chip-tooltip v-for="(tag, index) in getActiveTags" :key="index"
      :tag="tag" margin="mr-1" small cursor="info-cursor" close @click:close="onCloseChip"/>
  </v-chip-group>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import VChipTooltip from '@/views/components/chip/ChipTooltip.vue';

export default {
  components: {
    VChipTooltip,
  },
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
      // eslint-disable-next-line
      if ((this.mandatoryFilter || this.filterTags) && (this.mandatoryFilter.length || this.filterTags.length)) {
        return this.tags.filter(
          item => this.mandatoryFilter.includes(item.id) || this.filterTags.includes(item.id),
        );
      }
      return [];
    },
  },
};
</script>

<template>
<div>
  <v-toolbar
    flat
    dense
    fixed>
    <v-container fluid>
      <v-row>
        <v-col cols="7" class="py-4 text-left">
          <active-filter/>
        </v-col>

        <v-col cols="1" class="pt-2">
          <v-btn
            icon
            ma-1
            @click="onClickRestore"
            color="black"
            :disabled="isFilterDefault">
            <v-icon>
              mdi-filter-remove
            </v-icon>
          </v-btn>
        </v-col>
        <v-col cols="2" class="pr-5 pl-2">
          <sorter/>
        </v-col>
        <v-col cols="2" v-if="!isMobil"></v-col>
      </v-row>
    </v-container>
  </v-toolbar>
    <v-divider/>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import ActiveFilter from '@/views/components/button/ActiveFilter.vue'; //eslint-disable-line
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    ActiveFilter,
    Sorter,
  },

  methods: {
    onCloseChip(value) {
      this.$store.commit('removeOneFilter', value);
    },
    onClickRestore() {
      this.$store.commit('clearFilters');
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isFilterDefault() {
      return !((this.mandatoryFilter && this.mandatoryFilter.length) || this.getFilterTags.length);
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
    ]),
  },
};
</script>

<template>
<div>
  <v-toolbar
    flat
    dense
    fixed
    color="#F6F6F6">
    <v-container fluid>
      <v-row>
        <v-col cols="9" class="text-left">
          <active-filter/>
        </v-col>

        <v-col cols="1" class="pt-2">
          <v-btn
            icon
            ma-1
            @click="onClickRestore"
            color="green"
            :disabled="isFilterDefault">
            <v-icon>
              mdi-filter-remove
            </v-icon>
          </v-btn>
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

export default {
  components: {
    ActiveFilter,
  },

  methods: {
    onCloseChip(value) {
      this.$store.commit('removeOneFilter', value);
    },
    onClickRestore() {
      this.$store.commit('clearFilters');
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    isFilterDefault() {
      return !(
        (this.mandatoryFilter && this.mandatoryFilter.length) || // eslint-disable-line
        this.getFilterTags.length || // eslint-disable-line
        (this.numberFilter && this.numberFilter.length)
      );
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
      'numberFilter',
    ]),
  },
};
</script>

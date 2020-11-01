<template>
<div>
  <v-toolbar
    flat
    dense
    fixed>
    <active-filter/>
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
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getColorClass() {
      return this.isActiveState ? 'customer-color-activ' : 'customer-color-inactive';
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
    ]),
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(192, 214, 192)
}
.v-btn--active:before {
    opacity: 0.4;
    color: rgb(149, 201, 240)
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
  opacity: 0.3;
}
</style>

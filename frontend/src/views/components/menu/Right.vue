   <template>
    <v-sheet
      tile
      color="primary"
    >
      <v-chip-group
        multiple
        column
        light
        v-model="filterTags"
        @change="onChange()"
        @click="onClick()"
      >
        <v-chip
          filter
          light
          small
          v-for="(tag, index) in tags"
          :value="tag.id"
          :key="index"
          :color="tag.color">
          {{ tag.name }}
        </v-chip>
      </v-chip-group>
  </v-sheet>
</template>

<script>
// eslint-disable-next-line import/no-unresolved

export default {
  data: () => ({
    items: [],
    filterTags: [],
    oldFilterLength: 0,
  }),
  computed: {
    tags() {
      return this.$store.getters.tags;
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    isOverviewRoute() {
      return this.$route.name === 'overview';
    },
  },
  methods: {
    onClick() {
      this.oldFilterLength = this.filterTags.length;
    },
    onLoginClick() {
      this.$refs.login.show();
    },
    // eslint-disable-next-line no-unused-vars
    onChange() {
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', this.filterTags);

      if (this.oldFilterLength < this.filterTags.length) {
        const id = this.filterTags[this.filterTags.length - 1];
        // eslint-disable-next-line no-undef
        _paq.push(['trackEvent', 'tagChanged', id]);
      }
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', []);
    },
  },
  watch: {
    getFilterTags() {
    },
  },
};
</script>

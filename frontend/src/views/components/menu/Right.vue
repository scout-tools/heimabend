   <template>
    <v-sheet
      tile
      color="primary"
    >
      <span class="subtitle-1 whiteText">
          {{ 'Themenauswahl' }}
      </span>
      <v-chip-group
        multiple
        column
        light
        v-model="filterTags"
        @change="onChange()"
        @click="onClick()"
      >
        <v-chip-tooltip v-for="(tag, index) in getSideBarTags()" :key="index"
                        :tag="tag" small filter/>
      </v-chip-group>
  </v-sheet>
</template>

<script>
import { mapGetters } from 'vuex';
import VChipTooltip from '@/views/components/chip/ChipTooltip.vue';

export default {
  components: {
    VChipTooltip,
  },
  data: () => ({
    items: [],
    filterTags: [],
    oldFilterLength: 0,
  }),
  computed: {
    ...mapGetters([
      'tags',
      'tagCategory',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
  },
  methods: {
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category === categoryId);
    },
    getSideBarTags() {
      if (this.tags && this.tagCategory) {
        const sideBarTagCategories = this.tagCategory.filter(item => item.is_header === false);
        const sideBarTags = this.filterTagByCategory(sideBarTagCategories[0].id);
        return sideBarTags;
      }
      return [];
    },
    onClick() {
      this.oldFilterLength = this.filterTags.length;
    },
    onLoginClick() {
      this.$refs.login.show();
    },
    // eslint-disable-next-line no-unused-vars
    onChange() {
      this.$store.commit('changeFilterTags', this.filterTags);

      if (this.oldFilterLength < this.filterTags.length) {
        const id = this.filterTags[this.filterTags.length - 1];
        // eslint-disable-next-line no-undef
        _paq.push(['trackEvent', 'tagChanged', id]);
      }
    },
    resetTags() {
      this.filterTags = [];
      this.$store.commit('changeFilterTags', []);
    },
  },
  watch: {
    getFilterTags() {
    },
  },
};
</script>

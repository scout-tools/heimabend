   <template>
    <v-sheet
      tile
      color="primary"
    >
    <!-- <div
      v-for="category in getSideBarTagCategories"
      :key="category.id"
    >
        <div dark class="mt-7">
        <span  dark class="subtitle-1 whiteText">
          {{ category.name }}
        </span>
        <v-icon small class="whiteText">
          {{ getIcon(category.name) }}
        </v-icon>
      <v-divider class="my-1" dark/>
        </div> -->
      <span dark class="subtitle-1 whiteText">
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
        <v-chip
          filter
          light
          small
          v-for="(tag, index) in getSideBarTags"
          :value="tag.id"
          :key="index"
          :color="tag.color">
          {{ tag.name }}
        </v-chip>
      </v-chip-group>
    <!-- </div>  filterTagByCategory(category.id) -->
  </v-sheet>
</template>

<script>
import { mapGetters } from 'vuex';
// eslint-disable-next-line import/no-unresolved

export default {
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
    getSideBarTags() {
      if (this.tags && this.tagCategory) {
        const sideBarTagCategories = this.tagCategory.filter(item => item.is_header === false);
        const sideBarTags = this.filterTagByCategory(sideBarTagCategories[0].id);
        return sideBarTags;
      }
      return [];
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
  },
  methods: {
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category === `${process.env.VUE_APP_API}basic/tag-category/${categoryId}/`);
    },
    getIcon(name) {
      switch (name) {
        case 'Herz (Gemüt)':
          return 'mdi-heart';
        case 'Hand (Körper)':
          return 'mdi-hand';
        case 'Kopf (Verstand)':
          return 'mdi-head';
        default:
          break;
      }
      return '';
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

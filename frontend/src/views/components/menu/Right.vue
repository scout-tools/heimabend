   <template>
  <v-sheet tile color="primary" class="allow-scroll fixed">
    <v-container fluid class="pa-3">
      <v-row align="center" justify="center">
        <span class="subtitle-1 whiteText">
          {{ 'Themenauswahl' }}
        </span>
      </v-row>
      <v-row align="center" justify="center" v-if="getSideBarTags.length">
        <v-chip-group
          multiple
          column
          light
          v-model="filterTags"
          @change="onChange()"
          @click="onClick()"
        >
          <v-chip-tooltip
            v-for="(tag, index) in getSideBarTags"
            :key="index"
            :tag="tag"
            small
            filter
          />
        </v-chip-group>
      </v-row>
      <v-row class="mt-10" align="center" justify="center" v-else>
        <v-progress-circular
          dark
          :size="80"
          :width="10"
          class="ma-5"
          color="white"
          indeterminate
        ></v-progress-circular>
    <span class="subtitle-1 whiteText">
      Bitte hab etwas Geduld.
    </span>
      </v-row>
    </v-container>
  </v-sheet>
</template>

<script>
import { mapGetters } from 'vuex';
// eslint-disable-next-line
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
    ...mapGetters(['tags', 'tagCategory']),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    getSideBarTags() {
      if (this.tags && this.tagCategory) {
        const sideBarTagCategories = this.tagCategory.filter(item => item.id === 9);
        const sideBarTags = this.filterTagByCategory(sideBarTagCategories[0].id);
        return sideBarTags;
      }
      return [];
    },
  },
  methods: {
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category === categoryId);
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
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);

      if (this.oldFilterLength < this.filterTags.length) {
        const id = this.filterTags[this.filterTags.length - 1];
        // eslint-disable-next-line no-undef
        _paq.push(['trackEvent', 'tagChanged', id]);
      }
    },
    resetTags() {
      this.filterTags = [];
      this.$store.commit('changeFilterTags', []);
      this.$store.commit('setNextPath', false);
      this.$store.commit('resetHeimabendItems', []);
      this.$store.commit('setIsFirstEventLoaded', false);
    },
  },
  watch: {
    getFilterTags() {},
  },
};
</script>

<style scoped>
.allow-scroll {
  overflow-y: scroll; /* it works! */
}

.fixed {
  position: fixed;
}
</style>

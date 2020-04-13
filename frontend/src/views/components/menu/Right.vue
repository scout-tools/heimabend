   <template>
    <v-navigation-drawer
      right
      fixed
      app
      light
      v-if="!isMobil && isOverviewRoute"
      color="primary"
      class="test"
    >
      <template v-slot:prepend>
        <v-list-item>
          <v-list-item-content>
            <img
              v-on:click="onLoginClick()"
              src="https://dpbm.de/wp/wp-content/uploads/2019/02/mosaikWhite.svg"
              class="mr-2"
              height="100"
              alt = "Bundesabzeichen vom Deutschen Pfadfinderbund Mosaik"/>
             <v-divider/>
                <v-row class="px-3 py-5 mt-5">
                  <v-chip-group
                    multiple
                    column
                    light
                    v-model="filterTags"
                    @change="onChange()"
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
                </v-row>
          </v-list-item-content>
        </v-list-item>
      </template>
    <login ref="login"/>
    </v-navigation-drawer>
</template>

<script>
// eslint-disable-next-line import/no-unresolved
import Login from '@/views/components/dialogs/Login.vue';

export default {
  data: () => ({
    items: [],
    filterTags: [],
  }),
  components: {
    Login,
  },
  computed: {
    tags() {
      return this.$store.getters.tags;
    },
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    isOverviewRoute() {
      return this.$route.name === 'overview' || this.$route.name === 'overview-id';
    },
  },
  methods: {
    onLoginClick() {
      this.$refs.login.show();
    },
    onChange() {
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', this.filterTags);
    },
    resetTags() {
      this.filterTags = [];
      this.$emit('onTagFilterChanged', this.filterTags);
      this.$store.commit('changeFilterTags', []);
    },
    onClickTags() {
      this.$router.push({ name: 'tags' });
    },
  },
  watch: {
    getFilterTags() {
    },
  },
};
</script>

<style scoped>
.test {
  z-index: 0 !important;
}
</style>

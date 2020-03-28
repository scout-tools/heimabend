<template>
<div>
    <v-navigation-drawer
      v-model="isDrawer"
      app
      clipped
      width="300"
      color="accent"
    >
      <v-list>
          <v-row align="center">
             <v-card
              v-if="isAuthenticated"
              width="270"
              class="mx-auto"
            >
              <v-list-item class="lightPrimary pa-0 ma-0">
                <v-list-item-content>
                  <v-list-item-title>Filter</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-container>
                <v-row class="px-2 pb-2" v-if="isAuthenticated">
                  <v-col cols="10" class="pa-0 ma-0" align-self="center">
                  <v-switch
                    v-model="isJustActive"
                    @change="onToggleJustActive"
                    label="Veröffentlicht"
                    dense
                    color="secondary"
                    hide-details
                  />
                  </v-col>
                  <v-col class="pa-0 ma-0"  align-self="center">
                    <v-icon class="pt-5" color="red">
                      mdi-eye-off-outline
                    </v-icon>
                  </v-col>
                </v-row>
                </v-container>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <v-row>
            <v-card
              width="270"
              class="mx-auto"
            >
              <v-list-item class="lightPrimary">
                <v-list-item-content>
                  <v-list-item-title>
                    Themen-Auswahl
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-row class="px-2">
                  <v-chip-group
                    multiple
                    column
                    v-model="filterTags"
                    @change="onChange()"
                  >
                    <v-chip
                      filter
                      small
                      v-for="(tag, index) in tags"
                      :value="tag.id"
                      :key="index"
                      :color="tag.color">
                      {{ tag.name }}
                    </v-chip>
                  </v-chip-group>
                </v-row>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <v-row v-if="!$vuetify.breakpoint.mdAndUp">
            <v-card
              width="270"
              class="mx-auto"
            >
              <v-list-item class="lightPrimary pa-0 ma-0">
                <v-list-item-content>
                  <v-list-item-title>Sortierung</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
              <Sorter/>
              </v-list-item>
            </v-card>
          </v-row>
          <v-spacer dark class="my-6"/>
          <!-- <v-row>
            <v-card
              width="200"
              class="mx-auto"
            >
              <v-list-item class="secondary">
                <v-list-item-content>
                  <v-list-item-title>Likes</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-card-text mx-5>
                  <v-col cols="12">
                    Minimale Anzahl von Likes
                    <v-slider
                      prepend-icon="mdi-thumb-up"
                      icon-color="secondary"
                      thumb-label
                      dense
                      max="20"
                    ></v-slider>
                  </v-col>
                </v-card-text>
              </v-list-item>
            </v-card>
          </v-row> -->
          <!-- <v-spacer dark class="my-6"/> -->
      </v-list>
      <template v-slot:append>
        <v-list bottom>
          <v-divider v-if="isAuthenticated"/>

          <v-list-item v-if="isAuthenticated" link bottom>
            <v-list-item-icon>
              <v-icon>mdi-tag-text-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content @click="onClickTags()">
              <v-list-item-title>Tags</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider v-if="isAuthenticated"/>

          <v-list-item v-if="isAuthenticated" link bottom>
            <v-list-item-icon>
              <v-icon>mdi-message-text-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content @click="onClickMessage()">
              <v-list-item-title>Nachrichten</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider/>
          <v-list-item link bottom>
            <v-list-item-icon>
              <v-icon>mdi-help-circle-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content
              @click="onClickAboutProjectItem()"
            >
              <v-list-item-title>
                Über das Projekt
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        <v-divider/>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-information-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content @click="onClickImpressumItem()">
              <v-list-item-title>Impressum/Datenschutz</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
     </template>
    </v-navigation-drawer>
</div>
</template>

<script>
import Sorter from '@/views/components/dropdown/Sorter.vue'; //eslint-disable-line

export default {
  components: {
    Sorter,
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    filterTags: [],
    isDrawer: false,
  }),
  methods: {
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
    onClickHeimabendItem() {
      this.$router.push({ name: 'overview' });
    },
    onClickImpressumItem() {
      this.$router.push({ name: 'impressum' });
    },
    onClickAboutProjectItem() {
      this.$router.push({ name: 'aboutProject' });
    },
    onClickMessage() {
      this.$router.push({ name: 'messageOverview' });
    },
    onToggleJustActive() {
      this.$store.commit('toggleJustActive');
    },
    toggleDrawer() {
      this.isDrawer = !this.isDrawer;
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isJustActive: {
      get() {
        return this.$store.getters.justActive;
      },
      set() {
        return false;
      },
    },
    getFilterTags() {
      this.filterTags = this.$store.getters.filterTags; // eslint-disable-line
      return this.$store.getters.filterTags;
    },
    tags() {
      return this.$store.getters.tags;
    },
  },
};
</script>

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: limegreen
}
</style>

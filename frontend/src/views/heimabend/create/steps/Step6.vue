<template>
  <v-form
    ref="form6"
  >
<v-container>
  <v-row class="mt-6 ml-4">
    <span class="subtitle-1">
      Wähle so viele thematische Kategorien aus, wie zu deiner Heimabend-Idee passen. <br>
      <br>
      Wenn du noch eine Kategorie hinzufügen möchtest, kannst du dich
      gerne mit dem Kontaktformular direkt an uns wenden.
    </span>
  </v-row>
  <v-row class="ma-6">
    <v-select
      v-model="data.tags"
      :items="getSideBarTags"
      item-value="id"
      item-text="name"
      deletable-chips
      chips
      dense
      no-data-text="Wähle aus der Liste Probenordnung aus."
      multiple
      outlined
    >
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="index < 3" :color="item.color" small>
          <span>{{ item.name }}</span>
        </v-chip>
        <span
          v-if="index === 3"
          class="grey--text caption"
        >
          (+ ...)
        </span>
      </template>
    </v-select>
  </v-row>

    <v-divider class="my-2"/>
      <v-row class="ma-3" justify="center">
        <v-btn class="mx-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="mx-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right> mdi-chevron-right </v-icon>
        </v-btn>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                v-on="on"
                icon
                class="mx-1"
                color="secondary"
                @click="nextStep(true)"
              >
                <v-icon>
                  mdi-debug-step-over
                </v-icon>
              </v-btn>
            </template>
            <span>
              {{ 'Schritt überspringen' }}
            </span>
          </v-tooltip>
      </v-row>
</v-container>
        </v-form>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data: () => ({
    data: {
      executionTimeRating: 1,
      costsRating: 1,
    },
    n: 0,
  }),
  props: {
    data: Object,
  },
  computed: {
    ...mapGetters([
      'tags',
      'tagCategory',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    tags() {
      return this.$store.getters.tags;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getTopBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.isHeader);
      }
      return [];
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
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      this.$emit('nextStep');
    },
    getData() {
      return {
        tags: this.data.tags,
      };
    },
    getMandatoryBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.isMandatory);
      }
      return [];
    },
    getCategoryIdByTagId(categoryId) {
      if (this.categoryId) {
        return this.tags.filter(tag => tag.id === categoryId)[0];
      }
      return [];
    },
    getRulesByCategory(category) {
      let returnValue = this.rules.tags;
      if (!category.isMandatory) {
        return [];
      }

      if (this.data && this.data.tags) {
        const activeTags = this.tags.filter(tag => this.data.tags.includes(tag.id));
        const containsCategoryId = activeTags.filter(tag => tag.category === category.id); // eslint-disable-line
        if (containsCategoryId.length) {
          returnValue = [];
        }
      }
      return returnValue;
    },
  },
};
</script>

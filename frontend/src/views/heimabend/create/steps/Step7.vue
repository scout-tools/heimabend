<template>
  <v-form
    ref="form7"
    v-model="valid"
  >
    <v-container fluid class="mx-5 pa-0">
      <v-row
        v-for="(category, n) in getTopBarTagCategories"
        :key="category.id"
        class="ml-1 mr-10 my-5">
        <span class="subtitle-1 pa-1" style="text-align: left;">
          {{ texts[n] }}
        </span>
        <v-container class="ma-0 pa-0" fluid>
          <v-select
            v-model="data.tags"
            no-data-text="Wähle aus der Liste Themen aus."
            :items="filterTagByCategory(category.id)"
            :label="category.name"
            item-value="id"
            item-text="name"
            chips
            :rules="getRulesByCategory(category)"
            deletable-chips
            multiple
            dense
            single-line
            outlined
            required
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
        </v-container>
    </v-row>

      <v-row class="ma-3" justify="center">
        <v-btn class="ma-1" @click="prevStep()">
          <v-icon left> mdi-chevron-left </v-icon>
          Zurück
        </v-btn>
        <v-btn class="ma-1" color="primary" @click="nextStep()">
          Weiter
          <v-icon right> mdi-chevron-right </v-icon>
        </v-btn>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                v-on="on"
                icon
                class="ma-1"
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
  props: {
    data: Object,
  },
  data: () => ({
    rules: {
      tags: [
        v => (v && v.length >= 4 && false) || 'Wähle bitte mindestens einen Tag aus.',
      ],
    },
    valid: true,
    n: 0,
    texts: [
      'Pflichtfeld: Um welche Art von Heimabend-Ideen handelt es sich?',
      'Pflichtfeld: In welchen (Jahres-)Zeiten kann deine Idee durchgeführt werden?',
      'Pflichtfeld: An welchen Orten kann deine Idee durchgeführt werden?',
      'Pflichtfeld: Für welche Stufen ist deine Idee geeignet?',
      'Lässt sich deine Heimabend-Idee einem speziellen Thema zuordnen?',
      'Merkmale für den interen Gebrauch. Nur für Admins.',
    ],
  }),

  computed: {
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
    ]),
    getTopBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.isHeader);
      }
      return [];
    },
  },

  watch: {
    data() {
      if (this.data.tags && this.data.tags.length) {
        this.data.tags = this.setIntTags(this.data.tags);
      }
    },
  },

  methods: {
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
        const containsCategoryId = activeTags.filter(tag => this.convertUrlToId(tag.category) === category.id); // eslint-disable-line
        if (containsCategoryId.length) {
          returnValue = [];
        }
      }
      return returnValue;
    },
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => this.convertUrlToId(item.category) === categoryId);
    },
    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    setIntTags(urlTags) {
      const tagList = [];
      urlTags.forEach((tag) => {
        tagList.push(this.convertUrlToId(tag));
      });
      return tagList;
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep(skip = false) {
      if (!this.$refs.form7.validate() && !skip) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        selectedMandatoryFilter: this.data.tags,
      };
    },
  },
};
</script>

<style scoped>
</style>

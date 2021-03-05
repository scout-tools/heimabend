<template>
  <v-form
    ref="form6"
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
      <v-btn
        class="mr-5"
        @click="prevStep()"
      >
        Zurück
      </v-btn>

      <v-btn
        color="primary"
        @click="nextStep()"
      >
        Weiter
      </v-btn>
    </v-row>
    </v-container>
  </v-form>
</template>

<script>
import { mapGetters } from 'vuex';

export default {

  data: () => ({
    rules: {
      tags: [
        v => (v && v.length >= 4 && false) || 'Wähle bitte mindestens einen Tag aus.',
      ],
    },
    data: {
      tags: [],
    },
    valid: true,
    n: 0,
    texts: [
      'Pflichtfeld: In welchen (Jahres-)Zeiten kann deine Idee durchgeführt werden?',
      'Pflichtfeld: An welchen Orten kann deine Idee stattfinden?',
      'Pflichtfeld: Für welche Stufen ist deine Idee geeignet?',
      'Pflichtfeld: Um welche Art von Heimabend-Ideen handelt es sich?',
      'Lässt sich deine Heimabend-Idee einem speziellen Thema zuordnen?',
    ],
  }),

  computed: {
    tags() {
      return this.$store.getters.tags;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    getClassForTextContentSteps() {
      return this.isMobil ? 'mx-0 px-1' : '';
    },
    ...mapGetters([
      'tags',
      'tagCategory',
      'mandatoryFilter',
    ]),
    getTopBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.is_header);
      }
      return [];
    },
  },

  mounted() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },

  created() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },


  methods: {
    getMandatoryBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.is_mandatory);
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
      if (!category.is_mandatory) {
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
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category) === categoryId;
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form6.validate()) {
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

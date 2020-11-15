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
        v => (v && v.length >= 4 && false) || 'Ist zwingend erforderlich',
      ],
    },
    data: {
      selectedFilter: [],
    },
    valid: true,
    n: 0,
    texts: [
      'Pflicht: In welchen Jahreszeiten kann dein Heimabend durchgeführt werden?',
      'Pflicht: An welchen Orten kann dein Heimabend stattfinden?',
      'Pflicht: Für welche Stufen ist dein Heimabend geeignet?',
      'Pflicht: Was ist dein Heimabend für ein Typ?',
      'Hast du eine besonderes Thema?',
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
      if (this.data.tags && this.data.tags.length) {
        this.data.tags = this.setIntTags(this.data.tags);
      }
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
      let returnValue = [];
      if (!category.is_mandatory) {
        return returnValue;
      }

      if (this.data && this.data.tags) {
        this.tagCategory.filter(item => !!item.is_mandatory).forEach((item) => {
          console.log(category.name);
          const activeTags = this.tags.filter(tag => this.data.tags.includes(tag.id));
          const activeTags2 = activeTags.filter(tag => this.convertUrlToId(tag.category) === item.id); // eslint-disable-line
          debugger;
          if (activeTags2 && activeTags2.length) {
              if (this.convertUrlToId(activeTags2[0].category) !== category.id) { // eslint-disable-line
              returnValue = [];
            }
          } else {
            returnValue = this.rules.tags;
          }
        });
      }
      console.log(returnValue);
      return returnValue;
    },
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category === `${process.env.VUE_APP_API}basic/tag-category/${categoryId}/`);
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

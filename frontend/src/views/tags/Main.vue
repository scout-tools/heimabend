<template>
<div>
   <v-container>
    <v-tabs
     fixed-tabs
     centered>
      <v-tabs-slider/>
      <v-tab>Tags</v-tab>
      <v-tab>Tag Kategorien</v-tab>
      <v-tab-item>
        <tag-main/>
      </v-tab-item>
      <v-tab-item>
        <tag-category-main/>
      </v-tab-item>
    </v-tabs>
  </v-container>
</div>
</template>

<script>
import TagMain from './tag/Main.vue';
import TagCategoryMain from './tagCategory/Main.vue';


export default {
  components: {
    TagMain,
    TagCategoryMain,
  },

  data: () => ({
  }),

  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },

  methods: {
  },
  created() {
  },
};
</script>

<style scoped>
</style>

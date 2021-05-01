<template>
  <v-tabs vertical icons-and-text>
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      Tag
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      Tag Kategory
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <tag />
        </v-card-text>
      </v-card>
    </v-tab-item>

    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <tag-category />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import Tag from './tag/Main.vue';
import TagCategory from './tagCategory/Main.vue';

export default {
  components: {
    Tag,
    TagCategory,
  },
};
</script>

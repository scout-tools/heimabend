<template>
  <v-tabs vertical icons-and-text>
    <v-tab>
      <v-icon left> mdi-table-headers-eye </v-icon>
      Nachrichten
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      Kommenatre
    </v-tab>
    <v-tab>
      <v-icon left> mdi-table </v-icon>
      Themen
    </v-tab>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <post-box />
        </v-card-text>
      </v-card>
    </v-tab-item>

    <v-tab-item>
      <v-card flat class="ma-0">
        <v-card-text class="ma-0">
          <comments />
        </v-card-text>
      </v-card>
    </v-tab-item>

    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <category />
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import PostBox from './postBox/Main.vue';
import Comments from './comments/Main.vue';
import Category from './category/Main.vue';

export default {
  components: {
    PostBox,
    Category,
    Comments,
  },
};
</script>

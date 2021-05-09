<template>
  <div v-if="!loading">
    <v-container fluid style="text-align: left">
      <v-row max-width="600px" justify="center">
        <v-flex ma-3 lg7>
          <v-list-item-group active-class="" no-action>
            <v-list>
              <v-subheader inset>Heimabende</v-subheader>

              <v-list-item v-for="item in gerOrdered" :key="item.id">
                <v-list-item-avatar>
                  <v-icon :class="getActiveColor(item.isPublic)" dark>
                    {{ getActivIcon(item.isPublic) }}
                  </v-icon>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title
                    v-text="item.title + ' | ' + formatDate(item.createdAt)"
                  >
                  </v-list-item-title>

                  <v-list-item-subtitle
                    v-text="'von ' + item.createdBy"
                  ></v-list-item-subtitle>

                  <v-list-item-subtitle>
                    <v-chip-group>
                      <v-chip
                        v-for="(tag, index) in getEventTags(item.tags)"
                        :key="index"
                        active-class="''"
                        :color="tag.color"
                      >
                        {{ tag.name }}
                      </v-chip>
                    </v-chip-group>
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <action-button-menu
                    :data="item"
                    @onDeleteClick="onDeleteClick"
                    @onPublishClick="onPublishClick"
                  />
                </v-list-item-action>
              </v-list-item>
            </v-list>
          </v-list-item-group>
        </v-flex>
      </v-row>
      <delete-modal ref="deleteTagModal" @refresh="onRefresh" />
      <isPublicModal ref="isPublicModalRef" @refresh="onRefresh" />
    </v-container>
  </div>
  <div v-else>
    <v-subheader inset>Ein Moment bitte...</v-subheader>
    <div class="text-center">
      <v-progress-circular
        :size="80"
        :width="10"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

// eslint-disable-next-line import/no-unresolved
import DeleteModal from '@/views/heimabend/dialogs/DeleteModal.vue';
// eslint-disable-next-line import/no-unresolved
import isPublicModal from '@/components/dialog/isPublicModal.vue';
// eslint-disable-next-line import/no-unresolved
import ActionButtonMenu from '@/components/button/ActionButtonMenu.vue';
import store from '@/store'; // eslint-disable-line

export default {
  components: {
    ActionButtonMenu,
    DeleteModal,
    isPublicModal,
  },
  data() {
    return {
      loading: true,
      items: [],
      API_URL: process.env.VUE_APP_API,
    };
  },
  methods: {
    getCallHighscoreService() {
      this.loading = true;
      const path = `${
        this.API_URL
      }basic/admin-event/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((response) => {
          this.items = response.data;
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;
          this.responseObj = error;
          this.showError = true;
        });
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${
        dateObj.getMonth() + 1
      }.${dateObj.getFullYear()}`;
    },
    getActivIcon(isPublic) {
      if (isPublic) {
        return 'mdi-eye-outline';
      }
      return 'mdi-eye-off-outline';
    },
    getActiveColor(isPublic) {
      if (isPublic) {
        return 'green';
      }
      return 'red';
    },
    getEventTags(tagArray) {
      const tagsObject = this.tags.filter((item) => tagArray.includes(item.id)); // eslint-disable-line
      const containsCategoryId = tagsObject.filter(
        ( // eslint-disable-line
          tag // eslint-disable-line
        ) => [7].includes(tag.category) // eslint-disable-line
      ); // eslint-disable-line
      return containsCategoryId;
    },
    filterTagByCategory(tags, categoryId) {
      return this.tags.filter((item) => item.category === categoryId); // eslint-disable-line
    },
    onRefresh() {
      this.getCallHighscoreService();
    },
    onDeleteClick(item) {
      this.$refs.deleteTagModal.show(item);
    },
    onPublishClick(item) {
      this.$refs.isPublicModalRef.show(item);
    },
  },
  computed: {
    ...mapGetters(['tags']),
    gerOrdered() {
      return this._.sortBy(this.items, ['isPublic']);
    },
  },
  created() {
    this.getCallHighscoreService();
  },
};
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #f2f2f2;
}
th {
  font-size: 16px !important;
}
</style>

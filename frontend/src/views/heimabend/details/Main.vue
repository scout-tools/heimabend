<template>
<div>
  <div class="col-sm-12">
    <heimabend-card
      @refresh="refresh()"
      :items="getItem"
      :isDetailsView="true"
    />
    <v-progress-circular
      v-if="loading"
      color="primary"
      indeterminate
    />
  </div>
</div>
</template>


<script>
import axios from 'axios';

// eslint-disable-next-line import/no-unresolved
import HeimabendCard from '../cards/Heimabend.vue';

export default {
  components: {
    HeimabendCard,
  },
  computed: {
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    id() {
      return this.$route.params.id;
    },
    getItem() {
      return this.item;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    getFilterTags() {
      return this.$store.getters.filterTags;
    },
    tags() {
      return this.$store.getters.tags;
    },
  },

  methods: {
    refresh() {
      this.item = [];
      this.getEvent();
    },
    getEvent() {
      const path = `${this.API_URL}basic/event/${this.id}/`;
      this.loading = true;
      axios.get(path)
        .then((res) => {
          this.item = [res.data];
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },

    onUpdateClick(item) {
      this.$emit('onUpdateClick', item);
    },

    convertUrlToId(url) {
      if (url && typeof url === 'string') {
        const idStringArray = url.split('/');
        const id = idStringArray[idStringArray.length - 2];

        return parseInt(id, 10);
      }
      return url;
    },
    onResetClick() {
      this.$store.commit('clearFilters');
    },
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(this.convertUrlToId(tag)); // eslint-disable-line
      });
      if (this.getFilterTags && this.getFilterTags.length) {
        const matches = eventTagArray.filter(element => this.getFilterTags.includes(element));
        return !!matches.length;
      }
      return true;
    },
  },

  created() {
    this.getEvent();
    debugger;
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: {},
    loading: true,
  }),
};
</script>

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
    <v-container class="mx-auto ma-5">
      <v-row justify="center">
        <p :class="textColor">Diesen Heimabend versenden mit: </p>
      </v-row>
      <v-row justify="center">
        <social-sharing
          :url="getUrl()"
          title="Heimabend Inspirator"
          :description="getDescription()"
          quote="Der Inspirator ist eine Seite für Pfadfinder Heimabende."
          hashtags="pfadfinder, heimabend, Gruppenstude"
          v-cloak
          inline-template>
            <div class="container">
                <network network="email" id="email">
                  <font-awesome-icon :icon="['fas', 'at']" />
                </network>
                <network network="facebook" id="facebook">
                  <font-awesome-icon :icon="['fab', 'facebook']" />
                </network>
                <network network="whatsapp" id="whatsapp">
                  <font-awesome-icon :icon="['fab', 'whatsapp']" />
                </network>
                <network network="telegram" id="telegram">
                  <font-awesome-icon :icon="['fab', 'telegram']" />
                </network>
            </div>
          </social-sharing>
        </v-row>
      </v-container>
    <span v-if="!isMobil" class="bg"/>
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
    textColor() {
      return !this.isMobil ? 'white-text' : '';
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
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
    test() {
      return 'outer-margin';
    },
  },

  methods: {
    getUrl() {
      return `https://inspirator.dpbm.de/heimabend/${this.id}/`;
    },
    getDescription() {
      return 'Schau dir mal den Heimabend an.';
    },
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
  },

  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: {},
    loading: true,
  }),
};
</script>

<style>
#facebook{
  cursor: pointer;
  margin: 10px;
  padding: 5px;
  color: white;
  background-color: rgba(10, 151, 245, 0.829);;
  font-size: 32px;
  border: white;
  border-style: solid;
  border-width: 2px;
}

#email {
  cursor: pointer;
  margin: 10px;
  padding: 5px;
  color: white;
  background-color: rgb(0, 0, 0);
  font-size: 32px;
  color: white;
  border-style: solid;
  border-width: 2px;
}
#whatsapp {
  cursor: pointer;
  margin: 10px;
  padding: 5px;
  color: white;;
  background-color: rgba(5, 173, 89, 0.856);;
  font-size: 32px;
  border: white;
  border-style: solid;
  border-width: 2px;
}
#telegram {
  cursor: pointer;
  margin: 10px;
  padding: 5px;
  color: white;
  background-color: rgba(51, 172, 224, 0.836);
  font-size: 32px;
  border: white;
  border-style: solid;
  border-width: 2px;
}
.container {
  margin: 2px;
  padding: 2px;
}
</style>

<style scoped>
</style>

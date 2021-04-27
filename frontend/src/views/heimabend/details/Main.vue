<template>
  <v-container fluid class="ma-5" :max-width="getMaxWidth()">
    <v-row :max-width="getMaxWidth()">
      <v-card color="#F6F6F6"
        class="mx-auto" justify="center" :max-width="getMaxWidth()">
        <v-card-title class="ml-2 mt-2 pa-0" justify="center">
        <img
          :src="require('@/assets/inspi/inspi_flying.png')"
          class="mr-2"
          height="50"
          alt="Bild von Inspi"
        />
          Meine Empfehlungen:

        </v-card-title
        >
        <v-slide-group class="pa-0" active-class="success" show-arrows>
          <v-slide-item
            v-for="n in nextEvents"
            :key="n.id"
            v-slot="{ active, toggle }"
          >
            <v-card
              class="ma-4"
              height="120"
              width="250"
              @click="openViewNewTab(n.events[0].id)"
            >
              <v-card-subtitle
                class="whiteText justify-center text-center primary"
              >
                {{ n.events[0].title }}
              </v-card-subtitle>
              <v-img :src="getImageLink(n.events)" height="65px"></v-img>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-card>
    </v-row>
    <v-row align="center" justify="center" :max-width="getMaxWidth()">
      <heimabend-card
        @refresh="refresh()"
        :items="getItem"
        :isDetailsView="true"
      />
      <v-progress-circular v-if="loading" color="primary" indeterminate />
    </v-row>

    <v-row align="center" class="ma-5" justify="center" :max-width="getMaxWidth()">
      <comment-box color="#F6F6F6" :max-width="getMaxWidth()"/>
    </v-row>
    <v-row justify="center">
      <p :class="textColor">Diesen Heimabend versenden mit:</p>
    </v-row>
    <v-row justify="center">
      <social-sharing
        :url="getUrl()"
        title="Heimabend Inspirator"
        :description="getDescription()"
        quote="Der Inspirator ist eine Seite für Pfadfinder Heimabende."
        hashtags="pfadfinder, heimabend, Gruppenstude"
        v-cloak
        inline-template
      >
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
</template>


<script>
import axios from 'axios';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';
// eslint-disable-next-line import/no-unresolved
import HeimabendCard from '../cards/Heimabend.vue';
import CommentBox from './CommentBox.vue';

export default {
  mixins: [serviceMixin],
  components: {
    HeimabendCard,
    CommentBox,
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
  },
  methods: {
    getMaxWidth() {
      return '900';
    },
    getImageLink(item) {
      const imageId = item[0].headerImage_Image;
      if (imageId && imageId.length) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${imageId}.default.jpeg`;
      }
      return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/inspi_v2.png`;
    },
    getUrl() {
      return `https://inspirator.dpbm.de/heimabend/${this.id}/`;
    },
    getDescription() {
      return 'Schau dir mal diese Heimabend-Idee an.';
    },
    refresh() {
      this.item = [];
      this.getEvent();
    },
    openViewNewTab(id) {
      const routeData = this.$router.resolve({
        name: 'heimabendDetails',
        params: { id },
      });
      window.open(routeData.href, '_blank').focus();
    },
    getEvent() {
      const path = `${this.API_URL}basic/event/${this.id}/`;
      this.loading = true;
      axios
        .get(path)
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
    onResetClick() {
      this.$store.commit('clearFilters');
    },
    isTagMatchToEvent(item) {
      const eventTagArray = [];
      item.tags.forEach((tag) => {
        eventTagArray.push(tag); // eslint-disable-line
      });
      if (this.getFilterTags && this.getFilterTags.length) {
        const matches = eventTagArray.filter(
          ( // eslint-disable-line
            element // eslint-disable-line
          ) => this.getFilterTags.includes(element) // eslint-disable-line
        ); // eslint-disable-line
        return !!matches.length;
      }
      return true;
    },
    loadData(eventId) {
      this.getNextEvents(eventId).then((response) => {
        this.nextEvents = response.data;
      });
    },
  },

  created() {
    this.getEvent();
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
    this.loadData(this.id);
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    item: [],
    loading: true,
    nextEvents: [],
  }),
};
</script>

<style>
#facebook {
  cursor: pointer;
  margin: 10px;
  padding: 5px;
  color: white;
  background-color: rgba(10, 151, 245, 0.829);
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
  color: white;
  background-color: rgba(5, 173, 89, 0.856);
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

<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="3">
        <v-rating
          color="warning"
          background-color="warning"
          empty-icon="mdi-star-outline"
          full-icon="mdi-star"
          half-icon="mdi-star-half-full"
          hover
          readonly
          length="5"
          size="24"
          v-model="rating"
        ></v-rating>
      </v-col>
      <v-col cols="2">
        <v-btn :disabled="isAlreadyVoted(item)" icon @click="show = !show">
          <v-icon dark color="green"> mdi-star-plus </v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-row v-if="show" justify="center" align="center">
      <v-container class="ma-2">
        <v-row v-if="show" justify="center" align="center">
          <p>Bitte einen Stern auswählen</p>
        </v-row>
        <v-row v-if="show" justify="center" align="center">
          <v-col cols="5">
            <v-rating
              color="green"
              background-color="green"
              empty-icon="mdi-star-outline"
              full-icon="mdi-star"
              half-icon="mdi-star-half-full"
              hover
              length="5"
              size="24"
              v-model="addRating"
            >
            </v-rating>
          </v-col>
          <v-col cols="1">
            <v-btn
              @click="onRatingClick(item)"
              icon
              :disabled="addRating === 0"
            >
              <v-icon color="green"> mdi-send </v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import store from '@/store'; // eslint-disable-line
import { mapGetters } from 'vuex';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

export default {
  mixins: [serviceMixin],
  props: {
    item: Object,
  },
  data() {
    return {
      dataReady: false,
      delay: '0.1s',
      API_URL: process.env.VUE_APP_API,
      showError: false,
      showSuccess: false,
      showErrorLiked: false,
      timeout: 3000,
      showSuccessLiked: false,
      alreadyVotedSnackbar: false,
      emptyMaterialText: 'Juhu, kein Material nötig ^^',
      data: [],
      count: 0,
      show: false,
      rating: 3,
      addRating: 0,
    };
  },
  computed: {
    ...mapGetters(['tags', 'liked', 'isAuthenticated', 'isScoringMode']),
  },
  methods: {
    getLikeColor(item) {
      return this.isAlreadyVoted(item) ? 'red lighten-1' : 'red darken-2';
    },
    isAlreadyVoted(event) {
      return this.liked.includes(event.id);
    },
    onRatingClick(item) {
      this.show = false;
      if (!this.isAlreadyVoted(item)) {
        this.callEventLikeService(item.id);
      }
    },
    handleRatingChange(item) {
      this.addRating = item.index + 1;
    },
  },
};
</script>

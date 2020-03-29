<template>
<div>
<v-slide-y-transition  group>
  <v-card
    :max-width="getMaxWidth()"
    class="mx-auto ma-5"
    :style="{ transitionDelay: delay }"
    v-bind:id="`eventcard-${item.id}`"
    color="backgroundGrey"
    v-for="(item, index) in items"
    :key="index"
  >
    <v-list-item
      class="lightPrimary px-0"
      :class="paddingleftLebelIcons"
    >
      <v-img
        class="ml-1"
        :src="require('@/assets/wolfskopf.png')"
        v-if="item.isLvlOne"
        :max-width="maxWidthKnots"
      ></v-img>
      <v-img
        class="ml-1"
        :src="require('../../../assets/knot_blue.png')"
        v-if="item.isLvlTwo"
        :max-width="maxWidthKnots"
      ></v-img>
      <v-img
        class="ml-1"
        :src="require('../../../assets/knot_red.png')"
        v-if="item.isLvlThree"
        :max-width="maxWidthKnots"
      ></v-img>
      <v-divider class="mx-2" vertical></v-divider>
      <v-list-item-content>
        <v-list-item-title
          :class="titleClass()">
            {{ item.title }}
        </v-list-item-title>
      </v-list-item-content>
      <v-divider class="mx-2 ml-12" v-if="!item.isActive && isAuthenticated" vertical/>
        <v-tooltip
          nudge-left="80"
          v-if="!item.isActive && isAuthenticated"
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              class="ma-2"
              v-on="on"
              icon>
              <v-icon color="red">
                mdi-eye-off-outline
              </v-icon>
            </v-btn>
          </template>
          <span class="mx-1">
            Nicht Öffentlich
          </span>
        </v-tooltip>

      <v-divider class="mx-2 ml-2" v-if="isAuthenticated" vertical/>
      <v-btn
        class="ma-1 ml-0"
        text
        icon
        color="red lighten-2"
        v-if="isAuthenticated"
        @click="onDeleteClick(item)">
        <v-icon>mdi-delete-outline</v-icon>
      </v-btn>

        <v-divider class="mx-2 ml-2" v-if="isAuthenticated" vertical/>
        <v-btn
          class="ma-1 ml-0"
          text
          icon
          color="gray lighten-2"
          v-if="isAuthenticated"
          @click="onUpdateClick(item)">
          <v-icon>mdi-pencil-outline</v-icon>
        </v-btn>

      <v-divider
        v-if="!isAuthenticated && !isDetailsView"
        class="mx-2 ml-2"
        vertical/>
        <v-tooltip
          nudge-left="80"
          v-if="!isAuthenticated && !isDetailsView"
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              class="ma-1 ml-0"
              v-on="on"
              text
              icon
              color="black lighten-2"
              @click="onDetailsClick(item)">
              <v-icon>mdi-information-outline</v-icon>
            </v-btn>
          </template>
          <span class="mx-1">
            Weitere Informationen
          </span>
        </v-tooltip>
    </v-list-item>

    <v-divider/>
    <v-card-text>
      <p
        class="text-left subtitle-1"
        v-html="item.description">
      </p>
    </v-card-text>

    <v-divider class="mb-4"/>
    <div class="text-left ml-3">
      <u>
        Material
      </u>
    </div>
    <div
      v-if="item.material !== ''"
      class="text-left font-italic font-weight-light">
      <ul>
        <li
          v-for="(item, index4) in getMaterialArray(item.material)"
          :key="index4">
          {{ item }}
        </li>
      </ul>
    </div>
    <div
      v-else
      class="text-left font-weight-light"
    >
      <ul>
        <li>
          {{ emptyMaterialText }}
        </li>
      </ul>
    </div>

    <v-container>
      <v-tooltip
        v-for="(tag, index2) in item.tags"
        :key="index2"
        slot="append"
        bottom
        nudge-left="80"
      >
      <template v-slot:activator="{ on }">
      <v-chip
        v-on="on"
        class="ma-2"
        :color="getTagColorById(tag)"
      >
        {{ getTagNameById(tag) }}
      </v-chip>
      </template>
      <span>
        {{ getDescriptionNameById(tag) }}
      </span>
      </v-tooltip>
    </v-container>
    <v-divider />
    <v-card-actions class="accent">
      <!-- eslint-disable-next-line max-len -->
      <div class="caption mr-1" v-if="isDetailsView || !isMobil">
        {{ formatDate(item.createdAt) + '\n von ' + item.createdBy }}
      </div>
      <v-divider
        :class="verticalMargin"
        vertical
        v-if="isDetailsView"/>
      <v-tooltip
        nudge-left="80"
        bottom
        v-if="!isAuthenticated">
        <template v-slot:activator="{ on }">
          <v-btn
            class="ma-2"
            v-on="on"
            :color="getLikeColor(item)"
            text
            icon
            @click="onLikedClicked(item)">
            <v-icon>{{ getLikeIcon(item) }}</v-icon>
          </v-btn>
        </template>
          <span class="mx-1">
            Gefällt mir!
          </span>
      </v-tooltip>
      <v-divider
        :class="verticalMargin"
        vertical
        v-if="item.isPossibleDigital"/>

      <v-tooltip
        open-on-hover
        bottom
        nudge-left="80"
        v-if="item.isPossibleDigital">
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            :small="isMobil"
            v-on="on">
            <v-icon
              :size="getIconSize"
              color="red"
              v-if="item.isPossibleDigital">
              mdi-robot
            </v-icon>
          </v-btn>
        </template>
        <span>
          Dieser Heimabend ist mit deiner Sippe digital durchführbar
        </span>
      </v-tooltip>

      <v-divider
        :class="verticalMargin"
        vertical
        v-if="item.isPossibleAlone"/>
      <v-tooltip
        open-on-hover
        nudge-left="80"
        bottom
        v-if="item.isPossibleAlone">
        <template v-slot:activator="{ on }">
          <v-btn
            :small="isMobil"
            icon
            v-on="on">
            <v-icon
              :size="getIconSize"
              v-if="item.isPossibleAlone">
              mdi-account-cowboy-hat
            </v-icon>
          </v-btn>
        </template>
        <span>
          Dieser Heimabend ist alleine durchführbar
        </span>
      </v-tooltip>

      <v-divider :class="verticalMargin" vertical/>
        <v-tooltip
          v-if="item.costsRating > 0"
          open-on-hover
          bottom
          nudge-left="80">
          <template v-slot:activator="{ on }">
            <v-btn
              :x-small="isMobil"
              depressed
              color="accent"
              v-on="on">
              <v-rating
                v-model="item.costsRating"
                emptyIcon="mdi-currency-usd"
                fullIcon="mdi-currency-usd"
                color="orange"
                background-color="grey"
                dense
                length="3"
                :size="ratingSize"
                readonly/>
            </v-btn>
          </template>
          <span>
            {{ getCostsToolTip(item.costsRating) }}
          </span>
        </v-tooltip>

        <v-tooltip
          v-if="item.costsRating === 0"
          open-on-hover
          bottom
          nudge-left="80">
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              v-on="on">
              <v-icon
                :size="getIconSize"
                color="red">
                mdi-currency-usd-off
              </v-icon>
            </v-btn>
          </template>
          <span>Ohne Einkaufskosten</span>
        </v-tooltip>

        <v-divider
          :class="verticalMargin"
          v-if="!item.isPrepairationNeeded"
          vertical/>
        <v-tooltip
          v-if="!item.isPrepairationNeeded"
          open-on-hover
          nudge-left="80"
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              color="accent"
              v-on="on">
              <v-icon
                v-model="item.isPrepairationNeeded"
                color="black"
                :size="getIconSize"
                v-if="!item.isPrepairationNeeded">
                mdi-card-bulleted-off-outline
              </v-icon>
            </v-btn>
          </template>
          <span>
            Ohne Vorbereitungen
          </span>
        </v-tooltip>

        <v-divider
          :class="verticalMargin"
          vertical/>
        <v-tooltip
          nudge-left="80"
          v-if="item.executionTimeRating > 0"
          open-on-hover
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              :x-small="isMobil"
              depressed
              color="accent"
              v-on="on">
              <v-rating
                v-model="item.executionTimeRating"
                emptyIcon="mdi-clock"
                fullIcon="mdi-clock"
                color="black"
                background-color="grey"
                dense
                length="3"
                :size="ratingSize"
                readonly/>
            </v-btn>
          </template>
          <span>
            {{ getExecutionTimeRatingTooltip(item.executionTimeRating)}}
          </span>
        </v-tooltip>

        <v-tooltip
          v-if="item.executionTimeRating === 0"
          open-on-hover
          bottom
          nudge-left="80"
        >
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              v-on="on"
            >
              <v-icon
                :size="getIconSize"
                color="black"
              >
                mdi-table-large
              </v-icon>
            </v-btn>
          </template>
          <span>Großprojekt</span>
        </v-tooltip>
        <v-spacer />
        <v-divider
          :class="verticalMargin"
          vertical/>
        <v-tooltip
          nudge-left="80"
          open-on-hover
          bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              :x-small="isMobil"
              depressed
              color="accent"
              v-on="on">
              <v-rating
                v-model="item.like_score"
                emptyIcon="mdi-star-face"
                fullIcon="mdi-star-face"
                color="primary"
                background-color="grey"
                dense
                length="3"
                :size="ratingSize"
                readonly/>
            </v-btn>
          </template>
          <span>
            {{ getLikeScoreTooltip(item.like_score)}}
          </span>
        </v-tooltip>

    </v-card-actions>
  </v-card>
  </v-slide-y-transition>
  <v-snackbar
    v-model="showError"
    color="error"
    y='top'
    :timeout="timeout"
  >
    {{ 'Fehler beim Speichern des Heimabends' }}
  </v-snackbar>
  <v-snackbar
    v-model="showSuccess"
    color="success"
    y='top'
    :timeout="timeout"
  >
    {{ 'Der Heimabend wurde erfolgreich gelöscht' }}
  </v-snackbar>
  <DeleteModal
    ref="deleteTagModal"
    @refresh="onRefreshHeimabende"
  />
  <v-snackbar
    v-model="showSuccessLiked"
    color="success"
    y='top'
    :timeout="timeout"
  >
    {{ 'Danke, für deine Meinung' }}
  </v-snackbar>
  <v-snackbar
    v-model="showErrorLiked"
    color="error"
    y='top'
    :timeout="timeout"
  >
    {{ 'Dein Like konnte nicht entgegen genonnen werden' }}
  </v-snackbar>
</div>
</template>

<script>
import axios from 'axios';

import store from '@/store'; // eslint-disable-line
import DeleteModal from '../dialogs/DeleteModal.vue';

export default {
  props: {
    items: Array,
    isDetailsView: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    DeleteModal,
  },
  methods: {
    onLikedClicked(item) {
      const eventId = item.id;
      if (!this.isAlreadyVoted(item)) {
        this.callEventLikeService(eventId);
      }
    },
    getLikeColor(item) {
      return this.isAlreadyVoted(item) ? 'green lighten-2' : 'darkgray';
    },
    getLikeIcon(item) {
      return this.isAlreadyVoted(item) ? 'mdi-thumb-up' : 'mdi-thumb-up-outline';
    },
    isAlreadyVoted(event) {
      return this.liked.includes(event.id);
    },
    callEventLikeService(eventId) {
      const me = this; // eslint-disable-line
      store.commit('setLiked', eventId); // delete that line
      axios.post(`${this.API_URL}basic/like/`, {
        eventId: `${process.env.VUE_APP_API}basic/event/${eventId}/`,
      })
        .then(() => {
          store.commit('setLiked', eventId);
          this.showSuccessLiked = true;
        })
        .catch((error) => {
          this.responseObj = error;
          this.showError = true;
        });
    },
    getCostsToolTip(costsRating) {
      switch (costsRating) {
        case 1:
          return '0,00€ - 0,50€ pro Person';
        case 2:
          return '1€ - 2€ pro Person';
        case 3:
          return 'mehr als 2€ pro Person';
        default:
          return 'Fehler';
      }
    },
    getExecutionTimeRatingTooltip(executionTimeRating) {
      switch (executionTimeRating) {
        case 1:
          return 'bis 30 min';
        case 2:
          return '30 min - 60 min ';
        case 3:
          return 'mehr als 60 min ';
        default:
          return 'Fehler';
      }
    },
    getLikeScoreTooltip(score) {
      switch (score) {
        case 0:
          return '0 Beliebheits-Sterne';
        case 1:
          return '1 Beliebheits-Sterne';
        case 2:
          return '2 Beliebheits-Sterne';
        case 3:
          return '3 Beliebheits-Sterne';
        default:
          return 'Fehler';
      }
    },
    onRefreshHeimabende() {
      this.$emit('refresh');
    },
    titleClass() {
      return this.$vuetify.breakpoint.mdAndUp ? 'headline font-weight-medium' : 'title';
    },
    getMaxWidth() {
      return this.isDetailsView ? '1000' : '800';
    },
    verticalMargin() {
      return !this.$vuetify.breakpoint.mdAndUp ? 'mx-2' : 'mx-0';
    },
    getDescriptionNameById(idString) {
      let id;
      if (idString && typeof idString === 'string') {
        const idStringArray = idString.split('/');
        id = idStringArray[idStringArray.length - 2];
      } else {
        id = idString;
      }
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.description) {
        return returnTag.description;
      }
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      return 'Keine Beschreibung vorhanden';
    },
    getTagNameById(idString) {
      let id;
      if (idString && typeof idString === 'string') {
        const idStringArray = idString.split('/');
        id = idStringArray[idStringArray.length - 2];
      } else {
        id = idString;
      }
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      return false;
    },
    getTagColorById(idString) {
      let id;
      if (idString && typeof idString === 'string') {
        const idStringArray = idString.split('/');
        id = idStringArray[idStringArray.length - 2];
      } else {
        id = idString;
      }
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.color) {
        return returnTag.color;
      }
      return false;
    },
    onUpdateClick(params) {
      this.$router.push({ name: 'heimabendUpdate', params });
    },
    onDetailsClick(params) {
      this.$router.push({ name: 'heimabendDetails', params });
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${dateObj.getMonth() + 1}.${dateObj.getFullYear()} `;
    },
    getMaterialArray(string) {
      return string.split(',');
    },
    onDeleteClick(item) {
      this.$refs.deleteTagModal.show(item);
    },
    scrollToId() {
      const searchId = `eventcard-${this.getId()}`;
      const elem = document.getElementById(searchId);
      if (elem) {
        elem.scrollIntoView(false);
      }
    },
    getId() {
      return this.$route.params.id;
    },
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
      emptyMaterialText: 'Juhu, kein Material nötig ^^',
    };
  },
  mounted() {
    this.scrollToId();
  },
  computed: {
    ratingSize() {
      return !this.isMobil ? 20 : 16;
    },
    getIconSize() {
      return !this.isMobil ? 20 : 16;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    liked() {
      return this.$store.getters.liked;
    },
    paddingleftLebelIcons() {
      return !this.isMobil ? 'pl-2' : 'pl-1';
    },
    maxWidthKnots() {
      return !this.isMobil ? '30' : '18';
    },
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
    tags() {
      return this.$store.getters.tags;
    },
  },
};
</script>

<style scoped>
</style>

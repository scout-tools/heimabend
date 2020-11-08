<template>
<v-container class="max-width-class" ma-0 pa-0>
  <v-row no-gutters >
  <v-col :cols="getMainCols" >
  <h2
    class="deinHeimabendSpan"
    :class="yourHeimabendSpan()">
    dein Heimabend.
  </h2>
  <div>
    <v-card
      :max-width="getMaxWidth()"
      elevation=30

      class="mx-auto ma-3 mb-10 test-color"
      :style="{ transitionDelay: delay }"
      v-bind:id="`eventcard-${item.id}`"
      v-for="(item, index) in items"
      :key="index"
    >
      <v-list-item
        class="primary px-0"
        :class="paddingleftLebelIcons"
      >
      <keep-alive>
        <v-img
          class="ml-1"
          :src="require('@/assets/wolfskopf.png')"
          v-if="item.isLvlOne && isDetailsView"
          :max-width="maxWidthKnots"
        />
      </keep-alive>
        <v-img
          class="ml-1"
          :src="require('../../../assets/knot_blue.png')"
          v-if="item.isLvlTwo && isDetailsView"
          :max-width="maxWidthKnots"
        />
        <v-img
          class="ml-1"
          :src="require('../../../assets/knot_red.png')"
          v-if="item.isLvlThree && isDetailsView"
          :max-width="maxWidthKnots"
        />

        <v-divider
          v-if="isDetailsView"
          class="mx-2"
          vertical
        />

        <v-list-item-content>
          <v-list-item-title
            class="whiteText"
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
                class="ma-2 info-cursor"
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
          color="red lighten-3"
          v-if="isAuthenticated"
          @click="onDeleteClick(item)">
          <v-icon>mdi-delete-outline</v-icon>
        </v-btn>

          <v-divider class="mx-2 ml-2" v-if="isAuthenticated" vertical/>
          <v-btn
            class="ma-1 ml-0"
            text
            icon
            color="lightPrimary"
            v-if="isAuthenticated"
            @click="onUpdateClick(item)">
            <v-icon>mdi-pencil-outline</v-icon>
          </v-btn>

          <v-divider class="mx-2 ml-2" v-if="isAuthenticated" vertical/>
          <v-tooltip
            v-if="!isMobil && !isAuthenticated && item.like_score > 0"
            nudge-left="80"
            open-on-hover
            bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                class="px-2 info-cursor"
                :x-small="isMobil"
                depressed
                color="primary"
                v-on="on">
                <v-icon
                  v-for="i in item.like_score"
                  color="#F6D300"
                  :key="i"
                  :size="30"
                  readonly>
                  mdi-star-face
                </v-icon>
              </v-btn>
            </template>
            <span>
              {{ getLikeScoreTooltip(item.like_score)}}
            </span>
          </v-tooltip>
      </v-list-item>

      <v-divider/>
      <v-card-text>
        <div>
          <p
            class="text-left subtitle-1 test-color-text"
            :class="getDescriptionClass()"
            v-html="item.description">
          </p>
          <v-container
            v-if="!isDetailsView"
          >
            <v-row>
              <v-col cols="2">
              </v-col>
              <v-col cols="8">
                <v-tooltip
                  nudge-left="80"
                  bottom>
                  <template v-slot:activator="{ on }">
                   <router-link
                      :to="{ name: 'heimabendDetails',
                      params: { id: item.id } }"
                      class="no-underline"
                    >
                    <v-btn
                      depressed
                      @click="onDetailsClick(item)"
                      outlined
                      class="test-color-text"
                      block
                      v-on="on">
                      {{ getLikeButtonText }}
                    </v-btn>
                    </router-link>
                  </template>
                  <span class="mx-1">
                    Hier gelangst du zur Detailierten Heimabendansicht mit vielen
                    weiteren Informationen und Möglichkeiten
                  </span>
                </v-tooltip>
              </v-col>
              <v-col cols="2">
                <v-tooltip
                  nudge-left="80"
                  bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      icon
                      v-on="on"
                      :color="getLikeColor(item)"
                      @click="onLikedClicked(item)">
                      <v-icon
                        :size="getLikeIconSize">
                        {{ getLikeIcon(item) }}
                      </v-icon>
                    </v-btn>
                  </template>
                    <span class="mx-1">
                      Gefällt mir!
                    </span>
                </v-tooltip>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </v-card-text>

      <v-divider v-if="isDetailsView" class="my-2"/>
      <div v-if="isDetailsView">
        <div class="text-left ml-10">
          <u>
            Material
          </u>
        </div>

        <div
          v-if="item.material !== ''"
          class="text-left font-italic ml-10">
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
          class="text-left"
        >
          <ul>
            <li>
              {{ emptyMaterialText }}
            </li>
          </ul>
        </div>
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
          class="ma-2 info-cursor"
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

      <v-divider
        v-if="item.isPossibleDigital"
      />

      <v-card-actions px-0 class="lightPrimary pa-0">
        <v-tooltip
          open-on-hover
          bottom
          nudge-left="80"
          v-if="item.isPossibleDigital">
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              :small="isMobil"
              class="info-cursor"
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
          v-if="item.isPossibleAlone && item.isPossibleDigital"/>
        <v-tooltip
          open-on-hover
          nudge-left="80"
          bottom
          v-if="item.isPossibleAlone">
          <template v-slot:activator="{ on }">
            <v-btn
              :small="isMobil"
              icon
              class="info-cursor"
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

        <v-divider
          v-if="item.isPossibleAlone || item.isPossibleDigital"
          :class="verticalMargin"
          vertical
        />
          <v-tooltip
            v-if="item.costsRating > 0"
            open-on-hover
            bottom
            nudge-left="80">
            <template v-slot:activator="{ on }">
              <v-btn
                :x-small="isMobil"
                depressed
                color="lightPrimary"
                class="info-cursor"
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
                class="info-cursor"
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
                class="info-cursor"
                color="lightPrimary"
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
            v-if="item.executionTimeRating"
            :class="verticalMargin"
            vertical
          />
          <v-tooltip
            nudge-left="80"
            v-if="item.executionTimeRating > 0"
            open-on-hover
            bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                :x-small="isMobil"
                depressed
                color="lightPrimary"
                class="info-cursor"
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
                class="info-cursor"
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
            vertical
          />
          <div class="body-2 ma-2">
            {{ formatDate(item.createdAt) + '\n' + item.createdBy }}
          </div>
      </v-card-actions>
    </v-card>
  </div>
  <!-- </v-slide-y-transition> -->
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
    {{ 'Danke für deine Bewertung!' }}
  </v-snackbar>
  <v-snackbar
    v-model="showErrorLiked"
    color="error"
    y='top'
    :timeout="timeout"
  >
    {{ 'Dein Like konnte nicht entgegen genonnen werden' }}
  </v-snackbar>
  <v-snackbar
    v-model="alreadyVotedSnackbar"
    color="success"
    y='top'
    :timeout="timeout"
  >
    {{ 'Du hast diese Heimabend-Idee bereits bewertet' }}
  </v-snackbar>
    <v-progress-circular
      v-show="loading && !isDetailsView"
      indeterminate
      size="40"
      color="white"
    ></v-progress-circular>
    <Fab/>
  </v-col>
  <v-col
    v-if="!isMobil && !isDetailsView"
    cols="2"
    class="negativ-top-margin"
  >
    <menu-right
      pa-5
      class="fixed menu-right" style="padding-top: 110px; padding-left: 5px; padding-right: 5px;"
    />
  </v-col>
  </v-row>
</v-container>

</template>

<script>
import axios from 'axios';

import store from '@/store'; // eslint-disable-line
import { mapGetters } from 'vuex';
// eslint-disable-next-line import/no-unresolved
import MenuRight from '@/views/components/menu/Right.vue';
// eslint-disable-next-line import/no-unresolved
import Fab from '@/views/components/fab/Standard.vue';
// eslint-disable-next-line import/no-unresolved
import DeleteModal from '../dialogs/DeleteModal.vue';


export default {
  props: {
    items: Array,
    loading: {
      type: Boolean,
      default: true,
    },
    isDetailsView: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    DeleteModal,
    MenuRight,
    Fab,
  },
  methods: {

    scroll() {
      window.onscroll = () => {
        const bottomOfWindow = document.documentElement.scrollTop
          + window.innerHeight + 1000 > document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.loadMore();
        }
      };
    },
    loadMore() {
      this.$emit('loadMore');
    },
    yourHeimabendSpan() {
      return this.isMobil ? 'headerIsMobile' : 'headerIsDesktop';
    },
    getDescriptionClass() {
      let string = '';
      if (!this.isDetailsView) {
        string = string.concat('giveMeEllipsis');
      }
      if (!this.isMobil) {
        string = string.concat(' mx-10');
      } else {
        string = string.concat(' mx-2');
      }
      return string;
    },
    onLikedClicked(item) {
      const eventId = item.id;
      if (!this.isAlreadyVoted(item)) {
        this.callEventLikeService(eventId);
      } else {
        this.alreadyVotedSnackbar = true;
      }
    },
    getLikeColor(item) {
      return this.isAlreadyVoted(item) ? 'red lighten-1' : 'red darken-2';
    },
    getLikeIcon(item) {
      return this.isAlreadyVoted(item) ? 'mdi-heart' : 'mdi-heart-outline';
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
          // eslint-disable-next-line no-undef
          _paq.push(['trackEvent', 'like', eventId]);
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
          return 'Dieser Heimabend hat sich Inspirator-Stern verdient';
        case 1:
          return 'Dieser Heimabend hat sich einen Inspirator-Stern verdient';
        case 2:
          return 'Dieser Heimabend hat sich zwei Inspirator-Sterne verdient';
        case 3:
          return 'Dieser Heimabend hat sich drei Inspirator-Sterne verdient';
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
      return this.isDetailsView ? '900' : '800';
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
      return 'gray';
    },
    onUpdateClick(params) {
      this.$router.push({ name: 'heimabendUpdate', params });
    },
    onDetailsClick(item) {
      // eslint-disable-next-line no-undef
      _paq.push(['trackContentInteraction', 'clicked', item.title, item.id]);
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
      alreadyVotedSnackbar: false,
      emptyMaterialText: 'Juhu, kein Material nötig ^^',
      data: [],
      count: 0,
    };
  },
  mounted() {
    this.scrollToId();
    this.scroll();
  },
  computed: {
    ...mapGetters([
      'tags',
      'liked',
      'isAuthenticated',
    ]),
    isMainPage() {
      return this.currentRouteName === 'overview';
    },
    currentRouteName() {
      return this.$route.name;
    },
    ratingSize() {
      return !this.isMobil ? 24 : 18;
    },
    getIconSize() {
      return !this.isMobil ? 24 : 18;
    },
    getLikeIconSize() {
      return !this.isMobil ? 30 : 28;
    },
    getLikeButtonText() {
      return !this.isMobil ? 'Mehr Details' : 'Mehr';
    },
    paddingleftLebelIcons() {
      return !this.isMobil ? 'pl-2' : 'pl-1';
    },
    maxWidthKnots() {
      return !this.isMobil ? '30' : '18';
    },
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    getMainCols() {
      return !this.isMobil && !this.isDetailsView ? 10 : 12;
    },
  },
};
</script>

<style>
  .giveMeEllipsis {
    overflow: hidden;
    max-height: 500px;
  }
  .test-color {
    background-color: rgba(121, 121, 121, 0.068) !important;
  }
  .test-color-text {
    color: rgba(0, 0, 0, 0.829)
  }
  .whiteText {
    color: white !important;
  }
  .deinHeimabendSpan {
    font-family: "Special Elite", sans-serif !important;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .headerIsMobile {
    letter-spacing: 0.1em;
    font-size: 2.0rem !important;
    color: rgba(14, 12, 12, 0.692);
  }

  .headerIsDesktop {
    font-size: 3.5rem !important;
    letter-spacing: 0.4em;
  }
  .max-width-class {
    max-width: 100% !important;
    height: 100% !important;
  }
.fixed {
  position: fixed;
}
.menu-right {
  height: 100vh !important;
}
.negativ-top-margin {
  margin-top: -150px !important;
}
</style>

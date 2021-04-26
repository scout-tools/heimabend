<template>
  <v-container class="max-width-class" ma-0 pa-0>
    <v-row no-gutters>
      <v-col :cols="getMainCols">
        <v-spacer class="ml-8" />
        <h2 class="deinHeimabendSpan" v-if="!isDetailsView" :class="yourHeimabendSpan()">
          {{ getHeaderText(items) }}
        </h2>
        <v-spacer />
        <v-card
          :max-width="getMaxWidth()"
          class="mx-auto ma-3 mb-10 test-color"
          :style="{ transitionDelay: delay }"
          v-for="(item, index) in items"
          :key="index"
        >
          <!-- <v-card-title
            class="whiteText justify-center text-center primary"
            :class="titleClass()"
          >
            {{ item.title }}
          </v-card-title> -->
    <v-list-item
      two-line
      class="whiteText justify-center text-center primary"
      :class="titleClass()"
    >
      <v-list-item-content>
        <v-list-item-title
          class="whiteText justify-center text-center primary"
          :class="titleClass()"
        >
          {{item.title}}
        </v-list-item-title>
        <v-list-item-subtitle
          class="whiteText justify-center text-center primary">
          {{ getType(item) }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
          <v-img
            v-if="getImageLink(item)"
            max-height="250"
            aspect-ratio="2"
            :src="getImageLink(item)"
          ></v-img>
          <v-card-text>
            <p
              class="text-left subtitle-1 mt-2 test-color-text"
              :class="getDescriptionClass()"
              v-html="item.description"
            ></p>
            <v-container v-if="!isDetailsView">
              <v-row>
                <v-col cols="2"> </v-col>
                <v-col cols="8">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <router-link
                        :to="{
                          name: 'heimabendDetails',
                          params: { id: item.id },
                        }"
                        class="no-underline"
                      >
                        <v-btn
                          @click="onDetailsClick(item)"
                          elevation="2"
                          color="#EEEEEE"
                          block
                          v-on="on"
                        >
                          <v-icon left> mdi-page-next-outline </v-icon>
                          {{ getLikeButtonText }}
                        </v-btn>
                      </router-link>
                    </template>
                    <span class="mx-1">
                      Hier gelangst du zur Detailierten Heimabendansicht mit
                      vielen weiteren Informationen und Möglichkeiten
                    </span>
                  </v-tooltip>
                </v-col>
              </v-row>
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
                      <v-btn @click="onRatingClick(item)" icon :disabled="addRating === 0">
                        <v-icon color="green"> mdi-send </v-icon>
                      </v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
              </v-row>
            </v-container>
          </v-card-text>

          <v-divider v-if="isDetailsView" class="my-2" />
          <div v-if="isDetailsView">
            <div class="text-left ml-10">
              <u> Material </u>
            </div>

            <div
              v-if="item.material !== ''"
              class="text-left font-italic ml-10"
            >
              <ul>
                <li
                  v-for="(item, index4) in getMaterialArray(item.material)"
                  :key="index4"
                >
                  {{ item }}
                </li>
              </ul>
            </div>
            <div v-else class="text-left">
              <ul>
                <li>
                  {{ emptyMaterialText }}
                </li>
              </ul>
            </div>
          </div>

          <v-container>
            <v-chip-tooltip
              v-for="(tag, index2) in getEventTags(item.tags)"
              :key="index2"
              :tag="tag"
              margin="ma-2"
              cursor="info-cursor"
            />
          </v-container>

          <v-divider v-if="item.isPossibleDigital" />

          <v-divider
            class="mx-2 ml-12"
            v-if="!item.isActive && isAuthenticated"
            vertical
          />
          <v-tooltip
            nudge-left="80"
            v-if="!item.isActive && isAuthenticated"
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn class="ma-2 info-cursor" v-on="on" icon>
                <v-icon color="red"> mdi-eye-off-outline </v-icon>
              </v-btn>
            </template>
            <span class="mx-1"> Nicht Öffentlich </span>
          </v-tooltip>

          <v-divider v-if="isAuthenticated" vertical />
          <v-btn
            class="ma-1"
            text
            icon
            color="red lighten-3"
            v-if="isAuthenticated"
            @click="onDeleteClick(item)"
          >
            <v-icon>mdi-delete-outline</v-icon>
          </v-btn>

          <v-divider v-if="isAuthenticated" vertical />
          <v-btn
            class="ma-1"
            text
            icon
            color="lightPrimary"
            v-if="isAuthenticated"
            @click="onUpdateClick(item)"
          >
            <v-icon>mdi-pencil-outline</v-icon>
          </v-btn>
          <v-tooltip
            v-if="!isMobil && !isAuthenticated && item.likeScore === 10"
            nudge-left="80"
            open-on-hover
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-btn
                class="px-2 info-cursor"
                :x-small="isMobil"
                depressed
                color="primary"
                v-on="on"
              >
                <v-icon
                  v-for="i in item.likeScore"
                  color="#F6D300"
                  :key="i"
                  :size="30"
                  readonly
                >
                  mdi-star-face
                </v-icon>
              </v-btn>
            </template>
            <span>
              {{ getLikeScoreTooltip(item.likeScore) }}
            </span>
          </v-tooltip>

          <v-card-actions px-0 class="lightPrimary pa-0">
            <v-tooltip
              open-on-hover
              bottom
              nudge-left="80"
              v-if="item.isPossibleDigital"
            >
              <template v-slot:activator="{ on }">
                <v-btn icon :small="isMobil" class="info-cursor" v-on="on">
                  <v-icon
                    :size="getIconSize"
                    color="red"
                    v-if="item.isPossibleDigital"
                  >
                    mdi-robot
                  </v-icon>
                </v-btn>
              </template>
              <span>
                Diese Idee ist mit deiner Sippe digital durchführbar
              </span>
            </v-tooltip>

            <v-divider
              :class="verticalMargin"
              vertical
              v-if="item.isPossibleAlone && item.isPossibleDigital"
            />
            <v-tooltip
              open-on-hover
              nudge-left="80"
              bottom
              v-if="item.isPossibleAlone"
            >
              <template v-slot:activator="{ on }">
                <v-btn :small="isMobil" icon class="info-cursor" v-on="on">
                  <v-icon :size="getIconSize" v-if="item.isPossibleAlone">
                    mdi-account-cowboy-hat
                  </v-icon>
                </v-btn>
              </template>
              <span> Diese Idee ist alleine durchführbar </span>
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
              nudge-left="80"
            >
              <template v-slot:activator="{ on }">
                <v-btn
                  :x-small="isMobil"
                  depressed
                  color="lightPrimary"
                  class="info-cursor"
                  v-on="on"
                >
                  <v-rating
                    v-model="item.costsRating"
                    emptyIcon="mdi-currency-usd"
                    fullIcon="mdi-currency-usd"
                    color="orange"
                    background-color="grey"
                    dense
                    length="3"
                    :size="ratingSize"
                    readonly
                  />
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
              nudge-left="80"
            >
              <template v-slot:activator="{ on }">
                <v-btn icon class="info-cursor" v-on="on">
                  <v-icon :size="getIconSize" color="red">
                    mdi-currency-usd-off
                  </v-icon>
                </v-btn>
              </template>
              <span>Ohne Einkaufskosten</span>
            </v-tooltip>

            <v-divider
              :class="verticalMargin"
              v-if="!item.isPrepairationNeeded"
              vertical
            />
            <v-tooltip
              v-if="!item.isPrepairationNeeded"
              open-on-hover
              nudge-left="80"
              bottom
            >
              <template v-slot:activator="{ on }">
                <v-btn icon class="info-cursor" color="lightPrimary" v-on="on">
                  <v-icon
                    v-model="item.isPrepairationNeeded"
                    color="black"
                    :size="getIconSize"
                    v-if="!item.isPrepairationNeeded"
                  >
                    mdi-card-bulleted-off-outline
                  </v-icon>
                </v-btn>
              </template>
              <span> Ohne Vorbereitungen </span>
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
              bottom
            >
              <template v-slot:activator="{ on }">
                <v-btn
                  :x-small="isMobil"
                  depressed
                  color="lightPrimary"
                  class="info-cursor"
                  v-on="on"
                >
                  <v-rating
                    v-model="item.executionTimeRating"
                    emptyIcon="mdi-clock"
                    fullIcon="mdi-clock"
                    color="black"
                    background-color="grey"
                    dense
                    length="3"
                    :size="ratingSize"
                    readonly
                  />
                </v-btn>
              </template>
              <span>
                {{ getExecutionTimeRatingTooltip(item.executionTimeRating) }}
              </span>
            </v-tooltip>

            <v-tooltip
              v-if="item.executionTimeRating === 0"
              open-on-hover
              bottom
              nudge-left="80"
            >
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" class="info-cursor">
                  <v-icon :size="getIconSize" color="black">
                    mdi-table-large
                  </v-icon>
                </v-btn>
              </template>
              <span>Großprojekt</span>
            </v-tooltip>
            <v-spacer />
            <v-divider
              v-if="item.viewCount > 1"
              :class="verticalMargin"
              vertical
            />
            <v-tooltip
              v-if="item.viewCount > 1"
              open-on-hover
              bottom
              nudge-left="80"
            >
              <template v-slot:activator="{ on }">
                <v-badge v-on="on" :content="item.viewCount" overlap>
                  <v-icon v-on="on"> mdi-eye </v-icon>
                </v-badge>
              </template>
              <span>Bisherige Aufrufe</span>
            </v-tooltip>
            <v-divider :class="verticalMargin" vertical />
            <div class="body-2 ma-2">
              {{ formatDate(item.createdAt) + '\n' + item.createdBy }}
            </div>
          </v-card-actions>
        </v-card>
        <v-snackbar
          v-model="showError"
          color="error"
          y="top"
          :timeout="timeout"
        >
          {{ 'Fehler beim Speichern der Heimabend-Idee' }}
        </v-snackbar>
        <v-snackbar
          v-model="showSuccess"
          color="success"
          y="top"
          :timeout="timeout"
        >
          {{ 'Diese Heimabend-Idee wurde erfolgreich gelöscht' }}
        </v-snackbar>
        <delete-modal ref="deleteTagModal" @refresh="onRefreshHeimabende" />
        <v-snackbar
          v-model="showSuccessLiked"
          color="success"
          y="top"
          :timeout="timeout"
        >
          {{ 'Danke für deine Bewertung!' }}
        </v-snackbar>
        <v-snackbar
          v-model="showErrorLiked"
          color="error"
          y="top"
          :timeout="timeout"
        >
          {{ 'Dein Like konnte nicht entgegen genonnen werden' }}
        </v-snackbar>
        <v-snackbar
          v-model="alreadyVotedSnackbar"
          color="success"
          y="top"
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
        <fab v-if="!isScoringMode" />
      </v-col>
      <v-col
        v-if="!isMobil && !isDetailsView"
        cols="2"
        class="negativ-top-margin"
      >
        <menu-right
          pa-5
          class="fixed menu-right"
          style="padding-top: 45px; padding-left: 5px; padding-right: 5px z-index: 10"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import store from '@/store'; // eslint-disable-line
import { mapGetters } from 'vuex';
// eslint-disable-next-line import/no-unresolved
import MenuRight from '@/views/components/menu/Right.vue';
// eslint-disable-next-line import/no-unresolved
import Fab from '@/views/components/fab/Standard.vue';
// eslint-disable-next-line import/no-unresolved
import VChipTooltip from '@/views/components/chip/ChipTooltip.vue';
// eslint-disable-next-line import/no-unresolved
import DeleteModal from '../dialogs/DeleteModal.vue';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

export default {
  mixins: [serviceMixin],
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
    VChipTooltip,
  },
  methods: {
    getType(event) {
      const tagsObject = this.tags.filter((item) => event.tags.includes(item.id)); // eslint-disable-line
      const containsCategoryId = tagsObject.filter(
        ( // eslint-disable-line
          tag // eslint-disable-line
        ) => [4].includes(tag.category) // eslint-disable-line
      ); // eslint-disable-line
      if (containsCategoryId.length) {
        return containsCategoryId[0].name;
      }
      return 'kein Typ';
    },
    getHeaderText(items) {
      if (!items.length) {
        return 'Kein Treffer';
      }
      return !this.isScoringMode ? 'dein Heimabend' : 'Gut beschrieben?';
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
    scroll() {
      window.onscroll = () => {
        const bottomOfWindow = // eslint-disable-line
          document.documentElement.scrollTop + window.innerHeight + 1000 > // eslint-disable-line
          document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.loadMore();
        }
      };
    },
    loadMore() {
      this.$emit('loadMore');
    },
    getImageLink(item) {
      if (item.headerImage) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${item.headerImage}.default.jpeg`;
      }
      return null;
    },
    yourHeimabendSpan() {
      return this.isMobil ? 'headerIsMobile' : 'headerIsDesktop';
    },
    getMandatoryBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory.filter((item) => item.isEventOverview); // eslint-disable-line
      }
      return [];
    },
    convertUrlArray(ary) {
      return ary.map((e) => e); // eslint-disable-line
    },
    getEventTags(tagArray) {
      const tagsObject = this.tags.filter((item) => tagArray.includes(item.id)); // eslint-disable-line
      const containsCategoryId = tagsObject.filter(
        ( // eslint-disable-line
          tag // eslint-disable-line
        ) => [2, 4, 5, 9].includes(tag.category) // eslint-disable-line
      ); // eslint-disable-line
      return containsCategoryId;
    },
    filterTagByCategory(tags, categoryId) {
      return this.tags.filter((item) => item.category === categoryId); // eslint-disable-line
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
    getLikeColor(item) {
      return this.isAlreadyVoted(item) ? 'red lighten-1' : 'red darken-2';
    },
    isAlreadyVoted(event) {
      return this.liked.includes(event.id);
    },
    callEventLikeService(eventId) {
      const me = this;
      this.eventId = eventId; // eslint-disable-line
      store.commit('setLiked', eventId); // delete that line

      this.postExperimentItem(eventId, 1, this.addRating).then(() => {
        me.showSuccessLiked = true;
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
          return 'Diese Idee hat sich Inspirator-Stern verdient';
        case 1:
          return 'Diese Idee hat sich einen Inspirator-Stern verdient';
        case 2:
          return 'Diese Idee hat sich zwei Inspirator-Sterne verdient';
        case 3:
          return 'Diese Idee hat sich drei Inspirator-Sterne verdient';
        default:
          return 'Fehler';
      }
    },
    onRefreshHeimabende() {
      this.$emit('refresh');
    },
    titleClass() {
      return this.$vuetify.breakpoint.mdAndUp
        ? 'headline font-weight-medium'
        : 'title';
    },
    getMaxWidth() {
      return this.isDetailsView ? '900' : '800';
    },
    verticalMargin() {
      return !this.$vuetify.breakpoint.mdAndUp ? 'mx-2' : 'mx-0';
    },
    onUpdateClick(params) {
      store.commit('setScollPosition', window.scrollY);
      this.$router.push({ name: 'heimabendUpdate', params });
    },
    onDetailsClick() {
      store.commit('setScollPosition', window.scrollY);
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${
        dateObj.getMonth() + 1
      }.${dateObj.getFullYear()} `;
    },
    getMaterialArray() {
      return [];
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
      show: false,
      rating: 3,
      addRating: 0,
    };
  },
  mounted() {
    this.scrollToId();
    this.scroll();
  },
  computed: {
    ...mapGetters(['tags', 'liked', 'isAuthenticated', 'isScoringMode']),
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
    getLikeButtonText() {
      return !this.isMobil ? 'Mehr Details zur Idee' : 'Mehr';
    },
    paddingleftLebelIcons() {
      return !this.isMobil ? 'pl-2' : 'pl-1';
    },
    maxWidthKnots() {
      return !this.isMobil ? '18' : '14';
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
  color: rgba(0, 0, 0, 0.829);
}
.whiteText {
  color: white !important;
}
.deinHeimabendSpan {
  font-family: 'Special Elite', sans-serif !important;
  margin-top: 5px;
  margin-bottom: 5px;
}

.headerIsMobile {
  letter-spacing: 0.1em;
  font-size: 2rem !important;
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
  min-width: 200px;
}
.negativ-top-margin {
  margin-top: -140px !important;
}
.v-tooltip__content {
  pointer-events: initial;
}
</style>

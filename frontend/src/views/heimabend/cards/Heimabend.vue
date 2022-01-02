<template>
  <v-container fluid class="max-width-class" ma-0 pa-0>
    <!-- <v-row class="lightred ma-0" align="center" justify="center" v-if="!isDetailsView">
      <v-col align="center" justify="center" :cols=" isMobil ? 3 : 1" >
        <v-img :src="require('@/assets/inspi/inspi_party.png')" contain max-height="80"/>
      </v-col>
      <v-col align="center" justify="center" cols="6">
        <h2>Heimabend der Woche: <br>
          <router-link
          :to="{ name: 'heimabendDetails',
          params: { id: eventOfTheWeek.event} }"
          class="no-underline">
          {{ eventOfTheWeek.title }}
        </router-link>
        </h2>
      </v-col>
      <v-col :cols=" isMobil ? 1 : 3" >
      </v-col>
    </v-row> -->
    <v-row no-gutters>
      <v-col cols=12>
        <v-spacer class="mt-8" />
        <h2
          class="deinHeimabendSpan"
          v-if="!isDetailsView"
          :class="yourHeimabendSpan()"
        >
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
          <HeimabendCardHeader :item="item"/>
          <v-img
            v-if="getImageLink(item)"
            max-height="250"
            aspect-ratio="2"
            :src="getImageLink(item)"
          ></v-img>
          <v-card-text>
          <v-container>
            <v-chip-tooltip
              v-for="(tag, index2) in getEventTags(item.tags)"
              :key="index2"
              :tag="tag"
              :margin="isMobil ? 'ma-1' : 'ma-2'"
              cursor="info-cursor"
              :small="isMobil"
            />
          </v-container>
          <v-divider/>
            <v-container>
              <v-row>
                <v-col cols="2.5" v-for="(scoreObj, index) in scoreConfig" :key="index">
                  <v-icon large :color="scoreObj.color" class="ma-2">
                    {{ scoreObj.icon }}
                  </v-icon>
                  <br>
                  <h4 v-if="isMobil">{{ getText(scoreObj, item)}}</h4>
                  <h3 v-else>{{ getText(scoreObj, item)}}</h3>
                  <h6 v-if="isMobil">{{ scoreObj.name}}</h6>
                  <h5 v-else>{{ scoreObj.name}}</h5>
                </v-col>
              </v-row>
            </v-container>
            <v-divider class="my-2"/>
            <p
              class="text-left subtitle-1 mt-2 test-color-text max-width-screen-size"
              :class="getDescriptionClass()"
              v-html="item.description"
            >
            </p>
            <v-container class="ma-0" fluid v-if="!isDetailsView">
              <v-row>
                <v-col cols="2"> </v-col>
                <v-col cols="8" class="pa-0">
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
                          color="#EEEEEE"
                          block
                          v-on="on"
                        >
                          <v-icon left> mdi-chevron-down </v-icon>
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

              <v-divider class="my-4" v-if="isAuthenticated"/>

              <HeimabendRating v-if="false" :item="item" />
            </v-container>
            <v-container v-else>
              <v-row align="center" justify="center">
                <MaterialBox :materialList="item.materialList"/>
              </v-row>
            </v-container>
          </v-card-text>

          <v-divider
            class="mx-2 ml-12"
            v-if="!item.isPublic && isAuthenticated"
            vertical
          />
          <v-tooltip
            nudge-left="80"
            v-if="!item.isPublic && isAuthenticated"
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
          <v-card-actions class="pa-0">
            <v-spacer />
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
      <!-- <v-col
        v-if="!isMobil && !isDetailsView"
        cols="2"
        class="negativ-top-margin"
      >
        <menu-right
          pa-5
          class="fixed menu-right"
          style="padding-top: 45px; padding-left: 5px; padding-right: 5px z-index: 10"
        />
      </v-col> -->
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';

// eslint-disable-next-line import/no-unresolved
// import MenuRight from '@/views/components/menu/Right.vue';
// eslint-disable-next-line import/no-unresolved
import HeimabendRating from '@/components/rating/heimabend/Main.vue';
// eslint-disable-next-line import/no-unresolved
import MaterialBox from '@/components/box/Material.vue';
// eslint-disable-next-line import/no-unresolved
import HeimabendCardHeader from '@/components/heimabend/CardHeader.vue';
// eslint-disable-next-line import/no-unresolved
import Fab from '@/views/components/fab/Standard.vue';
// eslint-disable-next-line import/no-unresolved
import VChipTooltip from '@/views/components/chip/ChipTooltip.vue';
// eslint-disable-next-line
import DeleteModal from '../dialogs/DeleteModal.vue';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';
// eslint-disable-next-line
import { configData } from '@/mixins/configData.js';

export default {
  mixins: [serviceMixin, configData],
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
    // MenuRight,
    Fab,
    VChipTooltip,
    HeimabendRating,
    HeimabendCardHeader,
    MaterialBox,
  },
  methods: {
    getText(obj, item) {
      const returnArray = obj.rankings.filter(r => r.score === item[obj.techname]);
      if (returnArray && returnArray.length) {
        return returnArray[0].name;
      }
      return '';
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
    getEventOfTheWeek() {
      this.getEventOfTheWeekHistory(
        new URLSearchParams({ ordering: '-release_date', past: true }) // eslint-disable-line
      ).then((response0) => {
        this.eventOfTheWeek = response0.data[0]; // eslint-disable-line
      });
    },
    getImageLink(item) {
      if (
        item.headerImage && // eslint-disable-line
        item.headerImage.imageUuid && // eslint-disable-line
        item.headerImage.imageUuid.imageUuid
      ) {
        return `${process.env.VUE_APP_AWS_MEDIA_URL}media/images/${item.headerImage.imageUuid.imageUuid}.default.jpeg`;
      }
      return false;
    },
    yourHeimabendSpan() {
      return this.isMobil ? 'headerIsMobile' : 'headerIsDesktop';
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
    titleClass(item) {
      let styleClass = '';
      styleClass = this.$vuetify.breakpoint.mdAndUp
        ? 'headline font-weight-medium'
        : 'title';
      styleClass = `${styleClass} ${this.getHeaderColorClass(item.tags)}`;
      return styleClass;
    },
    getHeaderColorClass(tags) {
      let colorclass = 'color-scout';

      const hasWo = tags.includes(50);
      const hasScout = tags.includes(51);
      if (hasWo && hasScout) {
        colorclass = 'color-wo-scout';
      } else if (hasWo) {
        colorclass = 'color-wo';
      }
      return colorclass;
    },
    getMaxWidth() {
      return this.isDetailsView ? '900' : '800';
    },
    verticalMargin() {
      return !this.$vuetify.breakpoint.mdAndUp ? 'mx-2' : 'mx-0';
    },
    onUpdateClick(params) {
      this.$store.commit('setScollPosition', window.scrollY);
      this.$router.push({ name: 'heimabendUpdate', params });
    },
    onDetailsClick() {
      this.$store.commit('setScollPosition', window.scrollY);
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${
        dateObj.getMonth() + 1
      }.${dateObj.getFullYear()} `;
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
    getHeaderText(items) {
      if (!items.length) {
        return 'Kein Treffer';
      }
      return !this.isScoringMode ? 'dein Heimabend' : 'Gut beschrieben?';
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
      eventOfTheWeek: {
        event: 1,
        title: '',
      },
    };
  },
  mounted() {
    this.scrollToId();
    this.scroll();
  },
  computed: {
    ...mapGetters(['tags', 'liked', 'isAuthenticated', 'isScoringMode']),
    ratingSize() {
      return !this.isMobil ? 24 : 18;
    },
    getIconSize() {
      return !this.isMobil ? 24 : 18;
    },
    getLikeButtonText() {
      return !this.isMobil ? 'Vollständigen Heimabend anzeigen' : 'Vollständig';
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
  max-height: 350px;
}
.test-color {
  background-color: rgba(121, 121, 121, 0.068) !important;
}
.test-color-text {
  color: rgba(0, 0, 0, 0.829);
  max-width: 95vw;
}
.whiteText {
  color: white !important;
}
.deinHeimabendSpan {
  font-family: 'Special Elite', sans-serif !important;
  margin-top: 10px;
  margin-bottom: 10px;
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
  margin-top: -260px !important;
}
.v-tooltip__content {
  pointer-events: initial;
}
.max-width-screen-size {
  overflow: hidden;
}
.lightred {
  margin-top: 10px !important;
  background-color: #ff7f7f !important;
}
</style>

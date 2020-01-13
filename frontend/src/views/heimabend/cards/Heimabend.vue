<template>
<div v-if="dataReady">
<v-slide-y-transition  group>
  <v-card
    max-width="800"
    shaped
    class="mx-auto ma-5"
    :style="{ transitionDelay: delay }"
    color="backgroundGrey"
    v-for="(item, index) in items"
    :key="index"
  >
    <v-list-item
      class="lightPrimary pr-0"
      :class="paddingleftLebelIcons"
    >
      <v-img
        class="ml-1"
        :src="require('../../../assets/knot_orange.png')"
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
      <v-divider class="mx-2 ml-12" v-if="!item.isActive" vertical/>
      <v-icon color="red" v-if="!item.isActive">
        mdi-eye-off-outline
      </v-icon>
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
    </v-list-item>
    <v-divider />
    <!-- <v-card-text big class="text--primary" :v-html="item.description"/> -->
    <v-card-text>
      <p
        class="text-left subtitle-1"
        v-html="htmlText(item)"
      >
      </p>
    </v-card-text>
    <v-divider class="mb-4"/>

    <div class="text-left font-italic font-weight-light">
      <ul>
          <li
            v-for="(item, index4) in getMaterialArray(item.material)"
            :key="index4">
          {{ item }}
        </li>
      </ul>
    </div>

    <v-container>
      <v-chip
        class="ma-2"
        :color="getTagColorById(tag)"
        v-for="(tag, index2) in item.tags"
        :key="index2"
      >{{ getTagNameById(tag) }}</v-chip>
    </v-container>
    <v-divider />
    <v-card-actions class="accent">
      <div class="caption mr-1">{{ formatDate(item.createdAt) + '\n von ' + item.createdBy }}</div>

      <v-divider
        :class="verticalMargin"
        vertical
        v-if="item.isPossibleOutside"
      />

      <v-tooltip
        open-on-hover
        bottom
        nudge-left="80"
        v-if="item.isPossibleOutside"
      >
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            :small="isMobil"
            v-on="on">
            <v-icon
              :size="getIconSize"
              color="green"
              v-if="item.isPossibleOutside"
            >
              mdi-nature-people
            </v-icon>
          </v-btn>
        </template>
        <span>
          Für Draußen geeignet
        </span>
      </v-tooltip>

      <v-divider
        :class="verticalMargin"
        vertical
        v-if="item.isPossibleInside"
      />
      <v-tooltip
        open-on-hover
        nudge-left="80"
        bottom
        v-if="item.isPossibleInside">
        <template v-slot:activator="{ on }">
          <v-btn
            :small="isMobil"
            icon
            v-on="on"
          >
            <v-icon
              :size="getIconSize"
              v-if="item.isPossibleInside"
            >
              mdi-home
            </v-icon>
          </v-btn>
        </template>
        <span>
          Für das Haus geeignet
        </span>
      </v-tooltip>
      <v-divider :class="verticalMargin" vertical v-if="item.needPrepairaion" />
      <v-tooltip open-on-hover bottom v-if="item.needPrepairaion">
        <template v-slot:activator="{ on }">
          <v-btn
            :small="isMobil"
            icon
            v-on="on"
          >
            <v-icon
              color="green"
              v-if="item.needPrepairaion"
            >
              mdi-card-bulleted-off-outline
            </v-icon>
          </v-btn>
        </template>
        <span>
          Es ist keine Vorbereitung notwendig
        </span>
      </v-tooltip>
         <v-divider :class="verticalMargin" vertical/>
                <v-tooltip
                  v-if="item.costsRating > 1"
                  open-on-hover
                  bottom
                  nudge-left="80"
                >
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
                        readonly
                      />
                    </v-btn>
                  </template>
                  <span>Höhe der Kosten</span>
                </v-tooltip>

                <v-tooltip
                  v-if="item.costsRating === 1"
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
                        color="red"
                      >
                        mdi-currency-usd-off
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>Keine Kosten</span>
                </v-tooltip>

              <v-divider
                :class="verticalMargin"
                v-if="item.costsRating === 1"
                vertical
              />

                <v-tooltip
                  v-if="item.isPrepairationNeeded"
                  open-on-hover
                  nudge-left="80"
                  bottom
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      icon
                      color="accent"
                      v-on="on"
                    >
                      <v-icon
                        v-model="item.isPrepairationNeeded"
                        color="black"
                        :size="getIconSize"
                        v-if="item.isPrepairationNeeded">
                        mdi-card-bulleted-off-outline
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>
                    Es ist keine Vorbereitung notwendig
                  </span>
                </v-tooltip>
                <v-divider
                  v-if="item.isPrepairationNeeded"
                  :class="verticalMargin"
                  vertical
                />
                <v-tooltip
                  nudge-left="80"
                  open-on-hover
                  bottom
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="accent"
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
                  <span>Zeit für die Durchführung</span>
                </v-tooltip>
              <v-divider class="mx-2" vertical/>
              <v-spacer />
      <!-- <v-divider vertical></v-divider>
            <div>
              <v-btn class="ma-2" text icon color="green lighten-2">
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>
      </div>-->
    </v-card-actions>
  </v-card>
  </v-slide-y-transition>
</div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    items: Array,
  },
  methods: {
    titleClass() {
      return this.$vuetify.breakpoint.mdAndUp ? 'headline font-weight-medium' : 'title';
    },

    verticalMargin() {
      return !this.$vuetify.breakpoint.mdAndUp ? 'mx-2' : 'mx-0';
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
    onUpdateClick(item) {
      this.$emit('onUpdateClick', item);
    },
    ready() {
      const me = this;
      // here is code that should be done first before vue render all authData
      const path = `${this.API_URL}basic/tag/`;
      axios.get(path)
        .then((res) => {
          me.tags = res.data;
          me.dataReady = true;
        })
        .catch(() => {
        });
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${dateObj.getMonth() + 1}.${dateObj.getFullYear()} `;
    },
    htmlText(item) {
      return item.description.replace(/(?:\r\n|\r|\n)/g, '<br>');
    },
    getMaterialArray(string) {
      return string.split(',');
    },
  },
  mounted() {
    this.ready();
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      dataReady: false,
      delay: '0.1s',
    };
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
    paddingleftLebelIcons() {
      return !this.isMobil ? 'pl-6' : 'pl-1';
    },
    maxWidthKnots() {
      return !this.isMobil ? '30' : '18';
    },
    isMobil() {
      return this.$vuetify.breakpoint.smAndDown;
    },
  },
};
</script>

<style scoped>
</style>

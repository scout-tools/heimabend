<template>
<v-slide-y-transition>
<div v-if="dataReady">
  <v-card
    max-width="800"
    shaped
    class="mx-auto ma-5"
    color="backgroundGrey"
    v-for="(item, index) in items"
    :key="index"
  >
    <v-list-item
      class="lightPrimary pl-6 pr-0">
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_orange.png')"
        v-if="item.isLvlOne"
        max-width="30"
      ></v-img>
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_blue.png')"
        v-if="item.isLvlTwo"
        max-width="30"
      ></v-img>
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_red.png')"
        v-if="item.isLvlThree"
        max-width="30"
      ></v-img>
      <v-divider class="mx-2" vertical></v-divider>
      <v-list-item-content>
        <v-list-item-title
          :class="titleClass">
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
    <v-card-text big class="text--primary">
      {{ item.description }}
    </v-card-text>
    <v-card-text>{{ `Material: ${item.material}` }}</v-card-text>
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
      <div class="caption mr-1">{{ formatDate(item.createdAt)}}</div>

      <v-divider :class="verticalMargin" vertical v-if="item.isPossibleOutside" />
      <v-tooltip open-on-hover bottom v-if="item.isPossibleOutside">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="green" v-if="item.isPossibleOutside">mdi-nature-people</v-icon>
          </v-btn>
        </template>
        <span>Für Draußen geeignet</span>
      </v-tooltip>
      <v-divider :class="verticalMargin" vertical v-if="item.isPossibleInside" />
      <v-tooltip open-on-hover bottom v-if="item.isPossibleInside">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon v-if="item.isPossibleInside">mdi-home</v-icon>
          </v-btn>
        </template>
        <span>Für das Haus geeignet</span>
      </v-tooltip>
      <v-divider :class="verticalMargin" vertical v-if="item.needPrepairaion" />
      <v-tooltip open-on-hover bottom v-if="item.needPrepairaion">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="green" v-if="item.needPrepairaion">mdi-clipboard-list-outline</v-icon>
          </v-btn>
        </template>
        <span>Vorbereitung nötig?</span>
      </v-tooltip>
         <v-divider :class="verticalMargin" vertical/>
                <v-tooltip open-on-hover bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="backgroundGrey"
                      v-on="on">
                      <v-rating
                        v-model="item.costsRating"
                        emptyIcon="mdi-currency-eur"
                        fullIcon="mdi-currency-eur"
                        color="orange"
                        background-color="grey"
                        dense
                        length="3"
                        :size="ratingSize"
                        readonly
                      />
                    </v-btn>
                  </template>
                  <span>Kosten</span>
                </v-tooltip>
              <v-divider :class="verticalMargin" vertical/>
                <v-tooltip open-on-hover bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="backgroundGrey"
                      v-on="on"
                    >
                      <v-icon
                        v-model="item.isPrepairationNeeded"
                        :color="item.isPrepairationNeeded ? 'black': 'grey'">
                        mdi-clipboard-list-outline
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>Mit Vorbereitung?</span>
                </v-tooltip>
                <v-divider :class="verticalMargin" vertical/>
                <v-tooltip open-on-hover bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :x-small="isMobil"
                      depressed
                      color="backgroundGrey"
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
                  <span>Durchführungszeit</span>
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
</div>
</v-slide-y-transition>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    items: Array,
    tags: Array,
    isMobil: Boolean,
  },
  methods: {
    titleClass() {
      return !this.isMobil ? 'headline' : 'subtitle-1';
    },
    verticalMargin() {
      return !this.isMobil ? 'mx-2' : 'mx-0';
    },
    getTagNameById(idString) {
      debugger;
      console.log(idString);
      const idStringArray = idString.split('/');
      const id = idStringArray[idStringArray.length - 2];
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      return false;
    },
    getTagColorById(idString) {
      debugger;
      console.log(idString);
      const idStringArray = idString.split('/');
      const id = idStringArray[idStringArray.length - 2];
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
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return `${dateObj.getDate()}.${dateObj.getMonth() + 1}.${dateObj.getFullYear()} `;
    },
  },
  mounted() {
    this.ready();
  },
  data() {
    return {
      API_URL: process.env.VUE_APP_API,
      dataReady: false,
    };
  },
  computed: {
    ratingSize() {
      return !this.isMobil ? 20 : 12;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>

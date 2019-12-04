<template>
<div v-if="dataReady">
  <v-card
    max-width="800"
    shaped
    class="mx-auto ma-5"
    color="lightgrey"
    v-for="(item, index) in items"
    :key="index"
  >
    <v-list-item
      class="blue lighten-4 pl-6 pr-0">
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_orange.png')"
        max-width="30"
      ></v-img>
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_blue.png')"
        max-width="30"
      ></v-img>
      <v-img
        class="mx-1"
        :src="require('../../../assets/knot_red.png')"
        max-width="30"
      ></v-img>
      <v-divider class="mx-2" vertical></v-divider>
      <v-list-item-content>
        <v-list-item-title
          :class="titleClass">
            {{ item.title }}
        </v-list-item-title>
      </v-list-item-content>
      <v-divider class="mx-2 ml-12" vertical></v-divider>
      <v-btn class="ma-1 ml-0" text icon color="gray lighten-2" @click="onUpdateClick(item)">
        <v-icon>mdi-eye</v-icon>
      </v-btn>
    </v-list-item>
    <v-divider />
    <v-card-text big class="text--primary">{{ item.beschreibung}}</v-card-text>
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
    <v-card-actions class="grey lighten-4">
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
                      color="lightgrey"
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
                      color="lightgrey"
                      v-on="on"
                    >
                      <v-rating
                        v-model="item.prepairationRating"
                        emptyIcon="mdi-clock"
                        fullIcon="mdi-clock"
                        color="black"
                        background-color="grey"
                        dense
                        length="4"
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
      const idStringArray = idString.split('/');
      const id = idStringArray[idStringArray.length - 2];
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.name) {
        return returnTag.name;
      }
      debugger;
      return false;
    },
    getTagColorById(idString) {
      const idStringArray = idString.split('/');
      const id = idStringArray[idStringArray.length - 2];
      const returnTag = this.tags.find(tag => tag.id === parseInt(id, 10));
      if (returnTag && returnTag.color) {
        return returnTag.color;
      }
      return false;
    },
    ready() {
      const me = this;
      // here is code that should be done first before vue render all authData
      const path = 'http://localhost:8000/basic/tag/';
      axios.get(path)
        .then((res) => {
          debugger;
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
      dataReady: false,
    };
  },
  computed: {
    ratingSize() {
      return !this.isMobil ? 20 : 12;
    },
  },
};
</script>

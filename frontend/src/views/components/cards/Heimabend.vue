<template>
<div>
  <v-card
    max-width="800"
    shaped
    class="mx-auto ma-5"
    color="lightgrey"
    v-for="(item, index) in items"
    :key="index"
  >
    <v-list-item class="blue lighten-4 pl-6 pr-0">
      <v-list-item-content>
        <v-list-item-title :class="titleClass">{{ item.title }}</v-list-item-title>
      </v-list-item-content>
      <v-divider class="mx-2" vertical></v-divider>
      <v-btn class="ma-1 ml-0" text icon color="gray lighten-2" @click="onUpdateClick(item)">
        <v-icon>mdi-eye</v-icon>
      </v-btn>
    </v-list-item>
    <v-divider />
    <v-card-text big class="text--primary">{{ item.shortDescription}}</v-card-text>
    <v-card-text>{{ `Material: ${item.material}` }}</v-card-text>
    <v-container>
      <v-chip
        class="ma-2"
        :color="getTagById(tag).color"
        v-for="(tag, index2) in item.tags"
        :key="index2"
      >{{ getTagById(tag).name }}</v-chip>
    </v-container>
    <v-divider />
    <v-card-actions class="grey lighten-4">
      <div class="caption mr-1">{{ item.createdAt}}</div>
      <v-divider :class="verticalMargin" vertical v-if="item.outside" />
      <v-tooltip open-on-hover bottom v-if="item.outside">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="green" v-if="item.outside">mdi-nature-people</v-icon>
          </v-btn>
        </template>
        <span>Für Draußen geeignet</span>
      </v-tooltip>
      <v-divider :class="verticalMargin" vertical v-if="item.inside" />
      <v-tooltip open-on-hover bottom v-if="item.inside">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon v-if="item.inside">mdi-home</v-icon>
          </v-btn>
        </template>
        <span>Für das Haus geeignet</span>
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
                        color="red"
                        background-color="grey"
                        dense
                        length="3"
                        :size="ratingSize"
                        readonly
                      />
                    </v-btn>
                  </template>
                  <span>Vorbereitungszeit</span>
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
    getTagById(id) {
      return this.tags.find(tag => tag.id === id);
    },
  },
  data() {
    return {
    };
  },
  computed: {
    ratingSize() {
      return !this.isMobil ? 20 : 12;
    },
  },
};
</script>

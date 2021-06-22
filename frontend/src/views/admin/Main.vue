<template>
  <v-container fluid>
    <v-row justify="center">
      <v-flex ma-3 lg9>
        <v-layout column>
          <v-card>
            <v-tabs
              v-model="tab"
              background-color="primary"
              grow
              centered
              dark
              icons-and-text
            >
              <v-tabs-slider></v-tabs-slider>

              <v-tab v-for="tab in tabs" :key="tab.id" :to="tab.route" exact>
                {{ tab.name }}
              </v-tab>
            </v-tabs>

            <router-view></router-view>
          </v-card>
        </v-layout>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import Overview from './overview/Main.vue';
import Heimabend from './heimabend/Main.vue';
import Tag from './tag/Main.vue';
import Score from './score/Main.vue';
import Message from './message/Main.vue';
import Material from './material/Main.vue';

export default {
  components: {
    Overview, // eslint-disable-line
    Heimabend, // eslint-disable-line
    Tag, // eslint-disable-line
    Score, // eslint-disable-line
    Message, // eslint-disable-line
    Material, // eslint-disable-line
  },
  data() {
    return {
      tab: '/admin',
      selected: null,
      tabs: [
        // {
        //   name: 'Übersicht',
        //   route: '/admin',
        //   icon: 'mdi-clipboard',
        // },
        {
          name: 'Heimabend',
          route: '/admin/heimabend',
          icon: 'mdi-lightbulb-on',
        },
        {
          name: 'Tag',
          route: '/admin/tag',
          icon: 'mdi-tag',
        },
        {
          name: 'Nachricht',
          route: '/admin/message',
          icon: 'mdi-message',
        },
        {
          name: 'Inspi-Score',
          route: '/admin/score',
          icon: 'mdi-calculator-variant',
        },
        {
          name: 'Material',
          route: '/admin/material',
          icon: 'mdi-calculator-variant',
        },
      ],
    };
  },
  created() {
    this.$store.commit('setHeaderString', 'Admin');
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
  },
};
</script>

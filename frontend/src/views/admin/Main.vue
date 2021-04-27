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

              <v-tab href="#tab-1">
                Übersicht
                <v-icon>mdi-clipboard</v-icon>
              </v-tab>

              <v-tab href="#tab-2">
                Heimabende
                <v-icon>mdi-lightbulb-on</v-icon>
              </v-tab>

              <v-tab href="#tab-3">
                Tags
                <v-icon>mdi-tag</v-icon>
              </v-tab>

              <v-tab href="#tab-4">
                Nachrichten
                <v-icon>mdi-message</v-icon>
              </v-tab>

              <v-tab href="#tab-5">
                Inspi-Score
                <v-icon>mdi-calculator-variant</v-icon>
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item v-for="i in 5" :key="i" :value="'tab-' + i">
                <v-card-text>
                  <overview v-if="i === 1" />
                  <heimabend v-if="i === 2" />
                  <tags v-if="i === 3" />
                  <message v-if="i === 4" />
                  <score v-if="i === 5" />
                </v-card-text>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-layout>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

import Overview from './overview/Main.vue';
import Heimabend from './heimabend/Main.vue';
import Tags from './tags/Main.vue';
import Score from './score/Main.vue';
import Message from './message/Main.vue';

export default {
  components: {
    Overview,
    Heimabend,
    Tags,
    Score,
    Message,
  },
  data() {
    return {
      tab: null,
      selected: null,
    };
  },
  methods: {
    getMessageType() {
      const path = `${
        this.API_URL
      }basic/message-type/?&timestamp=${new Date().getTime()}`;
      axios
        .get(path)
        .then((res) => {
          this.$store.commit('setMessageType', res.data);
        })
        .catch(() => {
          this.showError = true;
        });
    },
  },
  created() {
    this.$store.commit('setHeaderString', 'Admin');
    this.$store.commit('setIsSubPage', true);
    this.$store.commit('setDrawer', false);
    this.getMessageType();
  },
};
</script>

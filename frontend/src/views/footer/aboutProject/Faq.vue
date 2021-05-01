<template>
  <v-container ma-3 fluid>
    <v-row class="mt-5" justify="center">
      <v-col cols="3">
      <div class="box-2 sb1-2 fade-in">
        Hallo, Ich bin Inspi. <br>Wie kann ich dir helfen?
      </div>
      </v-col>
      <v-col cols="1">
      <v-img
        :src="require('@/assets/inspi/inspi_front_kopfhoerer.png')"
        max-width="100"
      />
      </v-col>
    </v-row>
    <v-row justify="center">
        <v-expansion-panels>
          <v-expansion-panel v-for="(faq, i) in items" :key="i">
            <v-expansion-panel-header color="#F6F6F6">
              <v-container fluid>
                <v-row align="center" justify="center">
                  <v-col cols="1">
                    <v-icon large color="green">mdi-chat-question</v-icon>
                  </v-col>
                  <v-col cols="10">
                    <p class="text-left title ma-3">{{ faq.question }}</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-expansion-panel-header>
            <v-expansion-panel-content color="#F6F6F6" class="text-left">
              <p class="text-left subtitle-1 pa-3" v-html="faq.answer"></p>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
    </v-row>
    <v-row justify="center">
      <CommentBox
        :showType="false"
        allowedMessageTypes="question"
        />
    </v-row>
  </v-container>
</template>

<script>
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

// eslint-disable-next-line
import CommentBox from '@/components/box/Comment.vue';

export default {
  mixins: [serviceMixin],
  components: {
    CommentBox,
  },
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    items: [],
    serviceName: 'faq',
  }),

  created() {
    this.getItems(this.serviceName);
    this.$store.commit('setHeaderString', 'Fragen + Antworten');
  },
};
</script>

<style scoped>
.v-expansion-panel {
  max-width: 900px;
}

.box-2 {
  width: 300px;
  margin: 50px auto;
  background: #A6BF98;
  padding: 20px;
  text-align: center;
  font-weight: 900;
  color: #fff;
  font-family: arial;
  position: relative;
  z-index: 10;
  border-radius: 0.4em;
}

.sb1-2:before {
  content: '';
  width: 0px;
  height: 0px;
  position: absolute;
  border-left: 10px solid #A6BF98;
  border-right: 10px solid transparent;
  border-top: 10px solid #A6BF98;
  border-bottom: 10px solid transparent;
  z-index: 10;
  right: -19px;
  top: 6px;
}


#hideMe6 {
  -webkit-animation: cssAnimation2 7s forwards;
  animation: cssAnimation2 7s forwards;
}
@keyframes cssAnimation2 {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@-webkit-keyframes cssAnimation2 {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>

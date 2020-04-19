<template>
<v-container>
  <v-row justify="center">
    <v-flex
      ma-3
      lg7
    >
    <div class="display-2 ma-5">
      Fragen/Antworten
    </div>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="(faq,i) in faqs"
        :key="i">
        <v-expansion-panel-header>
          <span class="title"> {{ faq.question }}</span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <p class="text-left">
            {{faq.answer}}
          </p>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    </v-flex>
  </v-row>
</v-container>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    API_URL: process.env.VUE_APP_API,
    faqs: [
      {
        question: 'Was sollten wir hier eintragen?',
        answer: 'z.B. das hier',
      },
      {
        question: 'Was ist leckerer als Döner?',
        answer: 'Nichts!',
      },
    ],
  }),

  computed: {
  },

  methods: {
    getFaqs() {
      const path = `${this.API_URL}basic/faq/`;
      axios.get(path)
        .then((res) => {
          this.faqs = res.data;
        })
        .catch(() => {
        });
    },
  },

  created() {
    this.getFaqs();
  },
};
</script>

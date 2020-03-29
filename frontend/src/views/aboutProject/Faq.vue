<template>
  <v-expansion-panels>
    <v-expansion-panel
      v-for="(faq,i) in faqs"
      :key="i">
      <v-expansion-panel-header>
        {{faq.question}}
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-btn icon>
          <v-icon>
            mdi-pencil-outline
          </v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>
            mdi-delete
          </v-icon>
        </v-btn>
        <br>
        <br>
          {{faq.answer}}
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
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

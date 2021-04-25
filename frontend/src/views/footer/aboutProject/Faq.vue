<template>
<v-container fluid>
  <v-row justify="center">
            <v-img :src="require('@/assets/inspi/inspi_front_kopfhoerer.png')" max-width="100" />
  </v-row>
  <v-row justify="center">
    <v-flex
      ma-3
      lg7
    >
    <v-expansion-panels>
      <v-expansion-panel
        v-for="(faq,i) in faqs"
        :key="i">
        <v-expansion-panel-header>
          <v-icon large color="green">mdi-chat-question</v-icon>
          <span class="text-left title ma-3"> {{ faq.question }}</span>
        </v-expansion-panel-header>
        <v-expansion-panel-content class="text-left">
          <p
            class="text-left subtitle-1 pa-3"
            v-html="faq.answer">
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
        question: 'Wie läuft die Veröffentlichung einer Heimabend-Idee ab?',
        answer: 'Über das grüne Plus rechts unten auf deinem Bildschirm hast du die Möglichkeit, wenn du auf das blaue auftauchende Icon klickst, deine Heimabend-Idee hinzuzufügen. Es öffnet sich ein Fenster mit 4 verschiedenen Schritten, die einzeln erläutert werden und in denen du die einzelnen Fragen zu deiner Idee beantworten bzw. Textfelder ausfüllen kannst.'
         + ' <br> <br> Nachdem du die einzelnen Fenster ausgefüllt hast wird die fertige Heimabend-Idee dem Team hinter dem Inspirator zur Verfügung gestellt, das die einzelnen Felder kurz sprachlich, aber auch grob inhaltlich korrektur liest (sich bei Rückfragen ggf. noch einmal bei dir meldet) und in der Regel direkt die Heimabend-Idee freischaltet, sodass sie für alle Besucher der Website sichtbar ist.',
      },
      {
        question: 'Wie kann ich das Team unterstützen?',
        answer: 'Wir freuen uns besonders über wunderbare Heimabend-Ideen von vielen verschiedenen Menschen und über Werbung für das Projekt. Wenn du eigene Ideen oder Verbesserungsvorschläge hast oder sogar selbst Teil des Teams werden möchtest, wende dich gerne über das Kontaktformular ans Team, das sich direkt mit dir in Verbindung setzt.'
          + '<br><br>Die größte Freude haben wir, wenn du selbst das Beste aus den verschiedenen Ideen für deinen Heimabend nutzt und ihr als Gruppe eine schöne Zeit dabei erlebt.',
      },
      {
        question: 'Kann ich Tags selbst hinzufügen oder ändern?',
        answer: 'Du kannst uns gerne über das Nachrichtenformular (indem du auf das grüne Plus klickst und danach auf das orangene Symbol) eine kurze Nachricht mit deinem Vorschlag oder deiner Änderungsbitte schicken und wir setzen uns mit dir in Verbindung.',
      },
      {
        question: 'An wen kann ich mich bei Nachfragen oder Ergänzungs-/Änderungs- vorschlägen zu einer Heimabend-Idee wenden?',
        answer: 'Schicke uns gerne über das Nachrichtenformular mit deinem detaillierten Anliegen zu einer Heimabend-Idee eine Nachricht und wir setzen uns mit der Person in Verbindung, die die entsprechende Idee hinzugefügt habt. Kleine Änderungen oder Ergänzungen können wir aber auch direkt berücksichtigen.',
      },
      {
        question: 'Wie kann ich meine Heimabend-Idee nach dem Abschicken noch einmal ergänzen oder nachträglich verändern (auch wenn sie bereits veröffentlicht wurde)? ',
        answer: 'Schick uns gerne über das Kontaktformular (indem du auf das grüne Plus klickst und danach auf das orangene Symbol) eine kurze Nachricht mit deinem genauen Anliegen und wir können deine Änderungsvorschläge direkt einbringen. ',
      },
      {
        question: 'Was kann ich machen, wenn ich einen Verbesserungsvorschlag für eure Seite oder einen Fehler gefunden habe?',
        answer: 'Wir freuen uns besonders über konstruktive Kritik! Schick uns gerne über das Kontaktformular (indem du auf das grüne Plus klickst und danach auf das orangene Symbol) eine kurze Nachricht mit deinem Vorschlag/gefundenen Fehler und wir befassen uns damit - schließlich befindet sich diese Seite im stetigen Wandel und wird immer wieder (technisch und inhaltlich) verbessert und aktualisiert.',
      },
      {
        question: 'Ich habe eine nicht ganz ausgearbeitete Heimabend-Idee. Kann ich sie trotzdem einreichen?',
        answer: 'Wir freuen uns über neue Ideen! Schick uns gerne über das Nachrichtenformular einen kurzen Hinweis darauf, dass du gerne eine noch nicht vollständig ausgearbeitete Idee hochladen möchtest. Im Anschluss daran kannst du direkt deine Heimabend-Idee auf dem normalen Weg hinzufügen und wir ergänzen in unserem Team die restlichen Stellen. Bei Rückfragen dazu setzen wir uns mit dir in Verbindung.',
      },
      {
        question: 'Wer steckt hinter dem Projekt?',
        answer: 'Hinter dem Heimabend-Inspirator steckt ein kleines Team von Pfadfinderinnen und Pfadfindern aus dem DPBM (Deutscher Pfadfinderbund Mosaik), das sich zum Ziel gesetzt hat den Erfahrungsschatz aus dem Bund zu sammeln und öffentlich zur Verfügung zu stellen, damit viele Gruppenführungen davon in ihren Heimabenden profitieren können.',
      },
      {
        question: 'Wer entscheidet, ob eine Heimabend-Idee veröffentlicht wird und anhand welcher Kriterien?',
        answer: 'Das Team hinter dem Heimabend-Inspirator liest die einzeln eingebrachten Heimabend-Ideen sprachlich und inhaltlich Korrektur und veröffentlicht sie letztendlich. <br> <br>'
          + 'Dabei werden keine Heimabend-Ideen veröffentlicht, die bereits auf der Website veröffentlicht wurden, deren Durchführung gefährlich ist oder sich in rechtlichen Grauzonen bis hin zur Illegalität verhält. Außerdem veröffentlichen wir nur Beiträge mit sachlichem Bezug zum Inspirator, die in Art und Umfang der Konzeption des Projekts nicht widersprechen. Es werden nur Fotos und Beiträge veröffentlicht, an denen der Beitragende auch die Urheberrechte besitzt.',
      },
    ],
  }),

  computed: {
  },

  methods: {
    getFaqs() {
      const path = `${this.API_URL}basic/faq/?&timestamp=${new Date().getTime()}`;
      axios.get(path)
        .then((res) => {
          this.faqs = res.data;
        })
        .catch(() => {
        });
    },
  },

  created() {
    // this.getFaqs();
    this.$store.commit('setHeaderString', 'Fragen + Antworten');
  },
};
</script>

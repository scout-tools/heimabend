<template>
<v-container fluid>
  <v-row justify="center">
    <v-flex
      ma-3
      lg7
    >
      <div class="display-1 ma-10 text-uppercase" >
          Unsere Idee
      </div>
      <v-divider/>
      <v-sheet class="ma-4 pa-4">
        <div class="pa-3 display-1">
            Warum?
        </div>

        <div class="ma-3 subtitle-1 text-left">
            Wer von euch hat es nicht selbst schon erlebt?

          <li class="ma-3">
            Der Heimabend steht bevor und die Ideen gehen langsam aus, was
            du mit deinen Kindern oder ihr in eurer Gruppe machen
            möchtet - euch fehlt die Abwechslung.
          </li>

          <li class="ma-3">
            Ihr macht eure Quartalsplanung und braucht einfach kreativen Input, um an den
            Heimabenden mit eurer Gruppe spannendes zu erleben und zusammen zu
            wachsen.
          </li>

          <li class="ma-3">
            Ihr wollt stolz eure beste Heimabend-Idee mit den verschieden anderen Gruppen
            aus dem Bund teilen und auch selbst etwas ganz Neues ausprobieren.
          </li>
        </div>

      </v-sheet>

      <v-sheet class="ma-4 pa-4">
        <div class="pa-3 display-1">
            Die Idee
        </div>
        <div class="ma-5 subtitle-1 text-left">
          Wir haben diese Plattform geschaffen, um die kostbaren Erfahrungsschätze aus unserem
          Bund miteinander zu <b>teilen</b> und gemeinsam davon zu profitieren - damit die wenigen
          Alltags Stunden jedes jungen Pfadfinders am Heim für die ganze Gruppe zu einem noch
          <b>größeren Abenteuer</b> werden.
        </div>

        <div class="ma-5 subtitle-1 text-left">
          Auf dieser Seite sammeln wir verschiedene kreative <b>Heimabend-Programm-Ideen</b> - für
          alle Altersstufen, egal ob drinnen oder draußen, mit oder ohne Vorbereitung, aufwändig
          oder ohne Kosten, Lückenfüller oder Großprojekt. Nutzt dafür gerne eigene Ideen, aber
          auch analoge Quellen wie bspw. ein Ideenbuch aus eurem Stamm oder die Früchte der
          eigenen Erfahrung.
        </div>

        <div class="ma-5 subtitle-1 text-left">
          Es geht uns <b>nicht</b> darum, <b>fertig geplante Heimabend-Konzepte und Protokolle</b>
          auszutauschen und in der Gruppe nachzumachen. Vielmehr soll euch die Seite als
          Ideenquelle dienen, um Input für eure eigenen Heimabende zu haben, an euren
          Gruppenstunden-Konzepten zu basteln, mit der Gruppe neue Erfahrungen zu machen und
          euch selbst kreativ zu verwirklichen.
        </div>

      </v-sheet>

      <v-sheet class="ma-4 pa-4">
        <div class="pa-3 display-1">
          Kann ich mitmachen?
        </div>

        <div class="ma-5 subtitle-1 text-left">
          Wir laden euch hiermit herzlich ein, einen ganz persönlichen Stein zu diesem Mosaik an
          Programmideen hinzuzufügen, euch von dem Gesamtkunstwerk inspirieren zu lassen und
          das für eure Gruppe Beste mitzunehmen. Herzlich Gut Pfad und viel Freude bei euren
          Heimabenden!
        </div>

        <div class="ma-5 subtitle-1 text-left">
          Euer Team hinter dem Heimabend-Inspirator
        </div>
      </v-sheet>

      <v-sheet class="ma-4 pa-4">
        <div class="pa-3 display-1">
          <u>
            Kontakt
          </u>
        </div>

        <div class="ma-3 subtitle-1 text-left">
            Du möchtest uns eine <b>Nachricht</b> schicken? Gerne!

          <li class="ma-5">
            Wir freuen uns natürlich über alle Arten von Heimabend-Ideen. Gerne kannst du
            sie direkt mit dem &quot;grünen Plus&quot; (unten rechts) eintragen
            oder uns einfach per E-Mail senden.
          </li>

          <li class="ma-5">
            Wenn du einen Fehler findest freuen wir uns riesig, wenn du uns ihn mitteilen
            würdest, damit wir ihn so schnell wie möglich für alle beheben können.
          </li>

          <li class="ma-5">
            Wenn du einen Verbesserungsvorschlag oder eine geniale Idee hast, um den
            “Heimabend Inspirator” zu verbessern und daran mitzuwirken, sind wir dir natürlich
            auch sehr dankbar.
          </li>

            Zögere nicht uns zu schreiben, wir <b>freuen uns auf deine Nachricht</b> an:
        </div>
        <div>
          <img
            class="mr-2"
            :src="require('@/assets/inspiratorMailAdresse.jpg')" height="50"
          />
          <br>
          <i>Aus Spam-Schutz ist diese E-Mail-Adresse nicht zum Anklicken.</i>
        </div>

      </v-sheet>

      <v-sheet class="ma-4 pa-4">
        <div class="pa-3 display-1">
          <u>
            Open Source
          </u>
        </div>

        <div class="ma-3 subtitle-1 text-left">
            Alles was wir aufbauen ist für jeden frei verwendbar,
            der seinen Inhalt ebenfalls frei verwendbar macht.

          <li class="ma-5">
            Unsere Heimabende dürfen für Open-Source Projekte kopiert werden
          </li>

          <li class="ma-5">
            Unser Quellcode ist hier veröffentlicht:
            <a href="https://github.com/RobertBagdahn/heimabend">Github</a>
          </li>

          <li class="ma-5">
            Wenn du Fragen hast, dann kannst du uns gerne kontaktieren.
          </li>
        </div>
      </v-sheet>
    </v-flex>
  </v-row>
</v-container>
</template>

<script>
export default {
  created() {
    this.$store.commit('setHeaderString', 'Unsere Idee');
  },
};
</script>

<template>
  <v-row
    justify="center">
          <div class="ma-12">
          <h2 class="py-5">
          Angaben gemäß § 5 TMG
          </h2>

          <p class="font-weight-medium">
          Robert Bagdahn <br>
          Goebenstr. 31 <br>
          53113 Bonn <br>
          </p>

          <h2 class="py-5">
          Kontakt:
          </h2>

          <p class="font-weight-medium">
          E-Mail: robertbagdahn@gmail.com <br>
          </p>

          <h2 class="py-5">
          Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV
          </h2>

          <p class="font-weight-medium">
          Robert Bagdahn <br>
          Goebenstr. 31 <br>
          53113 Bonn <br>
          </p>

          <h2 class="py-5">
          Haftung für Inhalte
          </h2>

          <p class="font-weight-medium">
          Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte
          auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.
          Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet,
          übermittelte oder gespeicherte fremde Informationen zu überwachen
          oder nach Umständen zu
          forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
          Verpflichtungen zur Entfernung oder Sperrung der Nutzung von
          Informationen nach den allgemeinen
          Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist
          jedoch erst ab dem Zeitpunkt
          der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden
          von entsprechenden Rechtsverletzungen
          werden wir diese Inhalte umgehend entfernen.
          </p>

          <h2 class="py-5">
          Haftung für Links
          </h2>

          <p class="font-weight-medium">
          Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte
          wir keinen Einfluss haben. Deshalb
          können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die
          Inhalte der verlinkten Seiten ist stets
          der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten
          Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft.
          Rechtswidrige Inhalte waren zum
          Zeitpunkt der Verlinkung nicht erkennbar.
          Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne
          konkrete Anhaltspunkte einer Rechtsverletzung
          nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige
          Links umgehend entfernen.
          </p>

          <h2 class="py-5">
            Urheberrecht
          </h2>

          <p class="font-weight-medium">
          Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten
          unterliegen dem deutschen Urheberrecht. Die
          Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb
          der Grenzen des Urheberrechtes bedürfen der
          schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und
          Kopien dieser Seite sind nur für den privaten,
          nicht kommerziellen Gebrauch gestattet.
          Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die
          Urheberrechte Dritter beachtet. Insbesondere
          werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf
          eine Urheberrechtsverletzung aufmerksam werden,
          bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen
          werden wir derartige
          Inhalte umgehend entfernen
          </p>
          </div>
  </v-row>
</template>

<script>
export default {
  props: [],

  data: () => ({
    dialog: false,
    data: [],
  }),

  methods: {
    show() {
      this.dialog = true;
    },
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
  },
};
</script>

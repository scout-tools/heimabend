<template>
<v-container>
  <v-row justify="center">
    <v-flex ma-3 lg7>
      <div class="display-3">
        Impressum / Datenschutz
      </div>

      <v-card class="ma-10 pa-10">
        <div>
          <div class="ma-12">
            <h2 class="py-5">
              Angaben gemäß § 5 TMG
            </h2>

          <p class="font-weight-medium">
            David Miron <br>
            Deutscher Pfadfinderbund Mosaik <br>
            Neue Maastrichter Str. 5-7 <br>
            50672 Köln <br>
          </p>

          <h2 class="py-5">
          Kontakt:
          </h2>

          <p class="font-weight-medium">
          <a href="https://dpbm.de/impressum/">Kontakt zum Bundesamt hier </a>
          <br>
          <v-btn class="ma-10" @click="onClickHeimabendItem">
            Kontaktforumalar an das Team
          </v-btn>
          <br>
          <img
            class="mr-2"
            :src="require('@/assets/inspiratorMailAdresse.jpg')" height="50"
          />
          <br>
          </p>

          <h2 class="py-5">
          Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV
          </h2>

          <p class="font-weight-medium">
            David Miron <br>
            Deutscher Pfadfinderbund Mosaik <br>
            Neue Maastrichter Str. 5-7 <br>
            50672 Köln <br>
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
          werden wir derartige Inhalte umgehend entfernen
          </p>
          <a
            rel="license"
            href="http://creativecommons.org/licenses/by-nc/4.0/">
            <img
              alt="Creative Commons Lizenzvertrag"
              style="border-width:0"
              src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"/>
          </a>
          <br />
            Dieses Werk ist lizenziert unter einer
          <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
            Creative Commons Namensnennung-Nicht kommerziell 4.0 International Lizenz
          </a>.
          </div>
        </div>
      </v-card>
      <v-card class="ma-10 pa-10">
          <h2 class="py-5">
            Cookies widerrufen
          </h2>
          <p class="font-weight-medium">
            Sie haben die Möglichkeit zu verhindern, dass von Ihnen hier getätigte
            Aktionen analysiert und verknüpft werden. Dies wird Ihre Privatsphäre
            schützen, aber wird auch den Besitzer daran hindern, aus Ihren Aktionen
            zu lernen und die Bedienbarkeit für Sie und andere Benutzer zu verbessern.
          </p>

          <v-switch v-model="isAgree" :label="getLabel"></v-switch>
          <p class="font-weight-medium">

          </p>
          <p class="font-weight-medium">

          </p>

      </v-card>
    </v-flex>
  </v-row>
</v-container>
</template>

<script>
export default {
  props: [],

  data: () => ({
    dialog: false,
    data: [],
    isAgree: true,
  }),

  mounted() {
    const me = this;
    setTimeout(() => { me.getAgreeMent(); }, 300);
  },

  methods: {
    getAgreeMent() {
      const me = this;
      // eslint-disable-next-line no-undef
      _paq.push([function () {
        me.isAgree = !this.isUserOptedOut();
      }]);
    },
    show() {
      this.dialog = true;
    },
    cancel() {
      this.dialog = false;
      this.$emit('dialogClose');
    },
    onClickHeimabendItem() {
      this.$router.push({ name: 'message' });
    },
  },
  computed: {
    getLabel() {
      if (this.isAgree) {
        return 'Dein Besuch dieser Webseite wird aktuell erfasst. Diesen Schalter abwählen wenn dein Nutzerverhalten nicht mehr aufgezeichnet werden soll.';
      }
      return 'Dein Besuch dieser Webseite wird aktuell nicht erfasst. Diesen Schalter aktivieren wenn du uns erlauben willst dein Nutzerverhalten zu erfassen';
    },
  },
  watch: {
    isAgree(value) {
      if (value) {
        // eslint-disable-next-line no-undef
        _paq.push(['forgetUserOptOut']);
      } else {
        // eslint-disable-next-line no-undef
        _paq.push(['optUserOut']);
      }
    },
  },
};
</script>

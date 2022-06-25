<template>
  <v-container fluid>
    <v-row justify="center">
      <v-flex class="ma-3 lg7">
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">Angaben gemäß § 5 TMG</h2>

              <p class="font-weight-medium">
                Deutscher Pfadfinderbund Mosaik <br />
                Robert-Perthel-Str. 79<br />
                50739 Köln <br />
              </p>

              <p>
                Der Deutsche Pfadfinderbund Mosaik hat die Rechtsform eines
                nicht eingetragenen Vereins. Vorstand im Sinne des § 26 BGB sind
                je zwei Mitglieder der Bundesführung gemeinschaftlich.
                Bundesführer (Vorsitzender): David Miron, Römerstr. 440c, 50321
                Brühl Stellvertretende Bundesführer_innen (Stellvertretende
                Vorsitzende): Laurenz Sterk, Theresa Schuhmann, Tobias Michaely,
                Verena Schmidt
              </p>

              <p>
                Rechtsträger aller Bundesstellen, Bundeseinrichtungen und
                Bundesunternehmungen ist: Pfadfinder-Bundesamt Köln e.V.,
                Robert-Perthel-Str. 79, 50739 Köln VR 8654, Amtsgericht Köln
              </p>
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">Kontakt:</h2>

              <p class="font-weight-medium">
                <a href="https://dpbm.de/impressum/"
                  >Kontakt zum Bundesamt hier
                </a>
                <br />
                <v-btn class="ma-10" @click="onClickHeimabendItem">
                  Kontaktforumalar an das Team
                </v-btn>
                <br />
                <img
                  class="mr-2"
                  :src="require('@/assets/inspiratorMailAdresse.jpg')"
                  height="50"
                />
                <br />
              </p>
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">
                Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV
              </h2>

              <p class="font-weight-medium">
                David Miron<br />
                <br />
                Deutscher Pfadfinderbund Mosaik<br />
                Robert-Perthel-Str. 79<br />
                50739 Köln<br />
              </p>
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">Haftung für Inhalte</h2>

              <p class="font-weight-medium">
                Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene
                Inhalte auf diesen Seiten nach den allgemeinen Gesetzen
                verantwortlich. Nach §§ 8 bis 10 TMG sind wir als
                Diensteanbieter jedoch nicht verpflichtet, übermittelte oder
                gespeicherte fremde Informationen zu überwachen oder nach
                Umständen zu forschen, die auf eine rechtswidrige Tätigkeit
                hinweisen. Verpflichtungen zur Entfernung oder Sperrung der
                Nutzung von Informationen nach den allgemeinen Gesetzen bleiben
                hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst
                ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung
                möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen
                werden wir diese Inhalte umgehend entfernen.
              </p>
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">Haftung für Links</h2>

              <p class="font-weight-medium">
                Unser Angebot enthält Links zu externen Websites Dritter, auf
                deren Inhalte wir keinen Einfluss haben. Deshalb können wir für
                diese fremden Inhalte auch keine Gewähr übernehmen. Für die
                Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter
                oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten
                wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße
                überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der
                Verlinkung nicht erkennbar. Eine permanente inhaltliche
                Kontrolle der verlinkten Seiten ist jedoch ohne konkrete
                Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei
                Bekanntwerden von Rechtsverletzungen werden wir derartige Links
                umgehend entfernen.
              </p>
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <div>
            <div class="ma-12">
              <h2 class="py-5">Urheberrecht</h2>

              <p class="font-weight-medium">
                Die durch die Seitenbetreiber erstellten Inhalte und Werke auf
                diesen Seiten unterliegen dem deutschen Urheberrecht. Die
                Vervielfältigung, Bearbeitung, Verbreitung und jede Art der
                Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der
                schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
                Downloads und Kopien dieser Seite sind nur für den privaten,
                nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf
                dieser Seite nicht vom Betreiber erstellt wurden, werden die
                Urheberrechte Dritter beachtet. Insbesondere werden Inhalte
                Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine
                Urheberrechtsverletzung aufmerksam werden, bitten wir um einen
                entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen
                werden wir derartige Inhalte umgehend entfernen
              </p>
              <a
                rel="license"
                href="https://creativecommons.org/licenses/by-nc/4.0/deed.de"
              >
                <img
                  alt="Creative Commons Lizenzvertrag"
                  style="border-width: 0"
                  src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"
                />
              </a>
              <br />
              Dieses Werk ist lizenziert unter einer
              <a
                rel="license"
                href="https://creativecommons.org/licenses/by-nc/4.0/deed.de"
              >
                Creative Commons Namensnennung-Nicht kommerziell 4.0
                International Lizenz </a
              >.
            </div>
          </div>
        </v-sheet>
        <v-sheet class="ma-4 pa-4">
          <h2 class="py-5">Cookies widerrufen</h2>
          <p class="font-weight-medium">
            Sie haben die Möglichkeit zu verhindern, dass von Ihnen hier
            getätigte Aktionen analysiert und verknüpft werden. Dies wird Ihre
            Privatsphäre schützen, aber wird auch den Besitzer daran hindern,
            aus Ihren Aktionen zu lernen und die Bedienbarkeit für Sie und
            andere Benutzer zu verbessern.
          </p>

          <v-switch v-model="isAgree" :label="getLabel"></v-switch>
          <p class="font-weight-medium"></p>
          <p class="font-weight-medium"></p>
        </v-sheet>
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


  created() {
    this.$store.commit('setHeaderString', 'Impressum + Datenschutz');
  },

  methods: {
    onClickHeimabendItem() {
      this.$router.push({ name: 'message' });
    },
  },
};
</script>

import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import '@mdi/font/css/materialdesignicons.css';

import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: {
    themes: {
      light: {
        primary: '#1a4b7e',
        secondary: '#FFA300',
        accent: '#fefefe',
        backgroundGrey: '#fefefe',
        lightPrimary: colors.blue.lighten4,
      },
    },
  },
});

import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import '@mdi/font/css/materialdesignicons.css';

import colors from 'vuetify/lib/util/colors';
import InspiIcon from '@/components/icon/Inspi.vue';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
    myIcon: {
      component: InspiIcon,
      props: {
        name: 'inspi',
      },
    },
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

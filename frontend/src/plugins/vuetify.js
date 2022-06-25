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
        primary: '#4171A4',
        secondary: '#FFA300',
        accent: '#fefefe',
        backgroundGrey: '#fefefe',
        lightPrimary: colors.blue.lighten4,
        inspiBlue: '#4171A4',
        inspiGray: '#3d3d3d',
        inspiOrange: '#E9B12B',
        inspiRed: '#CD6162',
      },
    },
  },
});

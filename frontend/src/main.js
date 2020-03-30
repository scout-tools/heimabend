import Vue from 'vue';
import VueLodash from 'vue-lodash';
import lodash from 'lodash';
// import VueMeta from 'vue-meta';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faAt } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faWhatsapp, faTelegram, faPinterest, faFacebook,
} from '@fortawesome/free-brands-svg-icons';
import App from './App.vue';
import router from './router';
import auth from './auth';
import store from './store';
import vuetify from './plugins/vuetify';


const SocialSharing = require('vue-social-sharing');

library.add(faWhatsapp);
library.add(faTelegram);
library.add(faPinterest);
library.add(faFacebook);
library.add(faAt);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.config.productionTip = false;

auth.interceptorsSetup(store, router);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');

Vue.use(SocialSharing);
Vue.use(VueLodash,
  {
    name: 'custom',
    lodash,
  });

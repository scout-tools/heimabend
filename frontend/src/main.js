import Vue from 'vue';
import VueAnalytics from 'vue-analytics';
import VueLodash from 'vue-lodash';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import auth from './auth';

Vue.config.productionTip = false;

auth.interceptorsSetup(store);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');

Vue.use(VueAnalytics, {
  id: 'UA-154886286-2',
  autoTracking: {
    screenview: true,
  },
  router,
});

const options = { name: 'lodash' }; // customize the way you want to call it

Vue.use(VueLodash, options); // options is optional

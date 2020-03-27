import Vue from 'vue';
import VueLodash from 'vue-lodash';
import App from './App.vue';
import router from './router';
import auth from './auth';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

auth.interceptorsSetup(store, router);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');


const options = { name: 'lodash' }; // customize the way you want to call it

Vue.use(VueLodash, options); // options is optional

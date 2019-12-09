import Vue from 'vue';
// import Axios from 'axios';
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

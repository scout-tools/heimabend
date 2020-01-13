import Vue from 'vue';
import VueRouter from 'vue-router';
import Heimabend from '../views/heimabend/Main.vue';
import AboutProject from '../views/aboutProject/Main.vue';
import Impressum from '../views/impressum/Main.vue';
import Tags from '../views/tags/Main.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'overview',
    component: Heimabend,
  },
  {
    path: '/about',
    name: 'aboutProject',
    component: AboutProject,
  },
  {
    path: '/impressum',
    name: 'impressum',
    component: Impressum,
  },
  {
    path: '/tags',
    name: 'tags',
    component: Tags,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

import Vue from 'vue';
import VueRouter from 'vue-router';
import Heimabend from '../views/heimabend/Main.vue';
import AboutProject from '../views/aboutProject/Main.vue';
import Impressum from '../views/impressum/Main.vue';
import Tags from '../views/tags/Main.vue';
import HeimabendCreate from '../views/heimabend/create/Main.vue';

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
  {
    path: '/heimabend/create/',
    name: 'heimabendCreate',
    component: HeimabendCreate,
  },
  {
    path: '/heimabend/update/:id',
    name: 'heimabendUpdate',
    component: HeimabendCreate,
    props: true,
  },
];

const router = new VueRouter({
  // mode: 'history', // add fallback route to prod server
  base: process.env.BASE_URL,
  routes,
});

export default router;

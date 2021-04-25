import Vue from 'vue';
import VueRouter from 'vue-router';
import Inspirations from '@/views/inspi/inspirations/Main.vue';

import Message from '@/views/footer/message/Main.vue';
import Heimabend from '@/views/heimabend/Main.vue';
import AboutProject from '@/views/footer/aboutProject/Main.vue';
import Faq from '@/views/footer/aboutProject/Faq.vue';
import Impressum from '@/views/footer/impressum/Main.vue';
import HeimabendCreate from '@/views/heimabend/create/Main.vue';
import HeimabendDetails from '@/views/heimabend/details/Main.vue';
import RankingOverview from '@/views/inspi/ranking/Main.vue';
import ScoringStart from '@/views/inspi/scoring/Main.vue';
import ScoringTest from '@/views/inspi/scoring/Test.vue';
import EasterEgg from '@/views/inspi/easterEgg/Main.vue';
import Admin from '@/views/admin/Main.vue';

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
    path: '/faq',
    name: 'faq',
    component: Faq,
  },
  {
    path: '/impressum',
    name: 'impressum',
    component: Impressum,
  },
  {
    path: '/datenschutz',
    name: 'datenschutz',
    component: Impressum,
  },
  {
    path: '/message',
    name: 'message',
    component: Message,
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
  },
  {
    path: '/heimabend/:id',
    name: 'heimabendDetails',
    component: HeimabendDetails,
    props: true,
  },
  {
    path: '/ranking',
    name: 'ranking-overview',
    component: RankingOverview,
  },
  {
    path: '/scoring/start',
    name: 'scoring-start',
    component: ScoringStart,
  },
  {
    path: '/scoring/test/:id',
    name: 'scoring-test',
    component: ScoringTest,
  },
  {
    path: '/inspi/easter-egg',
    name: 'inspi-easter-egg',
    component: EasterEgg,
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin,
  },
  {
    path: '/inspirations',
    name: 'inspirations',
    component: Inspirations,
  },
];

const router = new VueRouter({
  mode: 'history', // add fallback route to prod server
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

export default router;

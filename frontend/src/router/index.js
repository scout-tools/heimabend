import Vue from 'vue';
import VueRouter from 'vue-router';
import Inspirations from '@/views/inspi/inspirations/Main.vue';

import Message from '@/views/footer/message/Main.vue';
import MessageFinale from '@/views/footer/message/FinalMessagePage.vue';
import Heimabend from '@/views/heimabend/Main.vue';
import AboutProject from '@/views/footer/aboutProject/Main.vue';
import Faq from '@/views/footer/aboutProject/Faq.vue';
import Impressum from '@/views/footer/impressum/Main.vue';
import HeimabendCreate from '@/views/heimabend/create/Main.vue';
import HeimabendCreateFinal from '@/views/heimabend/create/FinalEventPage.vue';
import HeimabendDetails from '@/views/heimabend/details/Main.vue';
import RankingOverview from '@/views/inspi/ranking/Main.vue';
import ScoringStart from '@/views/inspi/scoring/Landing.vue';
import ScoringTest from '@/views/inspi/scoring/Test.vue';
import ScoringSetup from '@/views/inspi/scoring/Setup.vue';
import ScoringFinal from '@/views/inspi/scoring/FinalScoringPage.vue';
import EasterEgg from '@/views/inspi/easterEgg/Main.vue';
import Admin from '@/views/admin/Main.vue';
import AdminOverview from '@/views/admin/overview/Main.vue';
import AdminHeimabend from '@/views/admin/heimabend/Main.vue';
// eslint-disable-next-line import/no-unresolved
import AdminTag from '@/views/admin/tag/Main.vue';
import AdminMessage from '@/views/admin/message/Main.vue';
import AdminScore from '@/views/admin/score/Main.vue';
import AdminMaterial from '@/views/admin/material/Main.vue';

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
    path: '/message/final',
    name: 'message-final',
    component: MessageFinale,
  },
  {
    path: '/heimabend/create/',
    name: 'heimabendCreate',
    component: HeimabendCreate,
  },
  {
    path: '/heimabend/create/final',
    name: 'heimabendCreateFinale',
    component: HeimabendCreateFinal,
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
    path: '/scoring/setup',
    name: 'scoring-setup',
    component: ScoringSetup,
  },
  {
    path: '/scoring/test/:id',
    name: 'scoring-test',
    component: ScoringTest,
  },
  {
    path: '/scoring/final/:id',
    name: 'scoring-final',
    component: ScoringFinal,
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
    children: [
      {
        path: 'overview',
        name: 'admin-overview',
        component: AdminOverview,
      },
      {
        path: 'heimabend',
        name: 'admin-heimabend',
        component: AdminHeimabend,
      },
      {
        path: 'tag',
        component: AdminTag,
      },
      {
        path: 'message',
        component: AdminMessage,
      },
      {
        path: 'material',
        component: AdminMaterial,
      },
      {
        path: 'score',
        component: AdminScore,
      },
    ],
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

import Vue from 'vue';
import VueRouter from 'vue-router';
import Message from '../views/message/Main.vue';
import Heimabend from '../views/heimabend/Main.vue';
import AboutProject from '../views/aboutProject/Main.vue';
import Faq from '../views/aboutProject/Faq.vue';
import Impressum from '../views/impressum/Main.vue';
import Tags from '../views/tags/Main.vue';
import TagCategory from '../views/tags/tagCategory/Main.vue';
import HeimabendCreate from '../views/heimabend/create/Main.vue';
import MessageOverview from '../views/message/Overview.vue';
import HeimabendDetails from '../views/heimabend/details/Main.vue';
import RankingOverview from '../views/ranking/Main.vue';
import ScoringStart from '../views/scoring/Main.vue';
import ScoringTest from '../views/scoring/Test.vue';

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
    path: '/message',
    name: 'message',
    component: Message,
  },
  {
    path: '/meassage/overview',
    name: 'messageOverview',
    component: MessageOverview,
  },
  {
    path: '/tags',
    name: 'tags',
    component: Tags,
  },
  {
    path: '/tagCategory',
    name: 'tagCategory',
    component: TagCategory,
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
];

const router = new VueRouter({
  mode: 'history', // add fallback route to prod server
  base: process.env.BASE_URL,
  routes,
});

export default router;

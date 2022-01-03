import axios from 'axios';

function getEvents() {
  return new Promise((resolve) => {
    axios.get('http://localhost:8000/basic/admin-sitemap')
      .then((response) => {
        resolve(response.data);
      });
  });
}

export const routes = [   // eslint-disable-line
  {
    path: '/',
    name: 'overview',
    component: () => import(/* webpackChunkName: "overview" */ './src/views/heimabend/Main.vue'), // eslint-disable-line
  },
  {
    path: '/about',
    name: 'aboutProject',
    component: () =>
      import(/* webpackChunkName: "aboutProject" */ './src/views/footer/aboutProject/Main.vue'), // eslint-disable-line
  },
  {
    path: '/faq',
    name: 'faq',
    component: () =>
      import(/* webpackChunkName: "faq" */ './src/views/footer/aboutProject/Faq.vue'), // eslint-disable-line
  },
  {
    path: '/impressum',
    name: 'impressum',
    component: () =>
      import(/* webpackChunkName: "impressum" */ './views/footer/impressum/Main.vue'), // eslint-disable-line
  },
  {
    path: '/datenschutz',
    name: 'datenschutz',
    component: () =>
      import(/* webpackChunkName: "datenschutz" */ './src/views/footer/aboutProject/Main.vue'), // eslint-disable-line
  },
  {
    path: '/message',
    name: 'message',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "message" */ './src/views/footer/message/Main.vue'), // eslint-disable-line
  },
  {
    path: '/message/final',
    name: 'message-final',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "messageFinal" */ './src/views/footer/message/FinalMessagePage.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/create/',
    name: 'heimabendCreate',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendCreate" */ './src/views/heimabend/create/Main.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/create/final',
    name: 'heimabendCreateFinale',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendCreateFinale" */ './src/views/heimabend/create/FinalEventPage.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/update/:id',
    name: 'heimabendUpdate',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendUpdate" */ './src/views/footer/aboutProject/Main.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/:id',
    name: 'heimabendDetails',
    meta: {
      sitemap: {
        slugs: async () => await getEvents(), //eslint-disable-line
      },
    },
    component: () =>
      import(/* webpackChunkName: "heimabendDetails" */ './src/views/heimabend/details/Main.vue'), // eslint-disable-line
  },
  {
    path: '/ranking',
    name: 'ranking-overview',
    component: () =>
      import(/* webpackChunkName: "rankingOverview" */ './src/views/inspi/ranking/Main.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/start',
    name: 'scoring-start',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringStart" */ './src/views/inspi/scoring/Landing.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/setup',
    name: 'scoring-setup',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringSetup" */ './src/views/inspi/scoring/Setup.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/test/:id',
    name: 'scoring-test',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringTest" */ './src/views/inspi/scoring/Test.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/final/:id',
    name: 'scoring-final',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import( /* webpackChunkName: "scoringFinal" */ './src/views/inspi/scoring/FinalScoringPage.vue'), // eslint-disable-line
  },
  {
    path: '/inspi/easter-egg',
    name: 'inspi-easter-egg',
    meta: { sitemap: { ignoreRoute: true } },

    component: () =>
      import(/* webpackChunkName: "inspiEasterEgg" */ './src/views/inspi/easterEgg/Main.vue'), // eslint-disable-line
  },
  {
    path: '/admin',
    name: 'admin',
    meta: { sitemap: { ignoreRoute: true } },
    component: () => import(/* webpackChunkName: "admin" */ './src/views/admin/Main.vue'), // eslint-disable-line
    children: [
      {
        path: 'overview',
        name: 'admin-overview',
        component: () =>
          import(/* webpackChunkName: "adminOverview" */ './src/views/admin/overview/Main.vue'), // eslint-disable-line
      },
      {
        path: 'heimabend',
        name: 'admin-heimabend',
        component: () =>
          import(/* webpackChunkName: "adminHeimabend" */ './src/views/admin/heimabend/Main.vue'), // eslint-disable-line
      },
      {
        path: 'event-of-the-week-create',
        name: 'admin-heimabend-event-of-the-week-create',
        component: () => import(/* webpackChunkName: "AdminEventOfWeek" */ './src/views/admin/heimabend/eventOfTheWeek/CreateForm.vue'), // eslint-disable-line
      },
      {
        path: 'tag',
        component: () =>
          import(/* webpackChunkName: "adminTag" */ './src/views/admin/tag/Main.vue'), // eslint-disable-line
      },
      {
        path: 'message',
        component: () =>
          import(/* webpackChunkName: "adminMessage" */ './src/views/admin/message/Main.vue'), // eslint-disable-line
      },
      {
        path: 'material',
        component: () =>
          import(/* webpackChunkName: "adminMaterial" */ './src/views/admin/material/Main.vue'), // eslint-disable-line
      },
      {
        path: 'score',
        component: () =>
          import(/* webpackChunkName: "adminScore" */ './src/views/admin/score/Main.vue'), // eslint-disable-line
      },
    ],
  },
  {
    path: '/inspirations',
    name: 'inspirations',
    component: () =>
      import(/* webpackChunkName: "inspirations" */ './src/views/inspi/inspirations/Main.vue'), // eslint-disable-line
  },
];

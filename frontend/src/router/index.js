// import axios from 'axios';

// function getEvents() {
//   return new Promise((resolve) => {
//     axios.get('http://localhost:8000/basic/admin-sitemap').then((response) => {
//       resolve(response.data);
//     });
//   });
// }

const routes = [   // eslint-disable-line
  {
    path: '/',
    name: 'overview',
    component: () => import(/* webpackChunkName: "overview" */ './../views/heimabend/Main.vue'), // eslint-disable-line
  },
  {
    path: '/about',
    name: 'aboutProject',
    component: () =>
      import(/* webpackChunkName: "aboutProject" */ './../views/footer/aboutProject/Main.vue'), // eslint-disable-line
  },
  {
    path: '/faq',
    name: 'faq',
    component: () =>
      import(/* webpackChunkName: "faq" */ './../views/footer/aboutProject/Faq.vue'), // eslint-disable-line
  },
  {
    path: '/impressum',
    name: 'impressum',
    component: () =>
      import(/* webpackChunkName: "impressum" */ './../views/footer/impressum/Main.vue'), // eslint-disable-line
  },
  {
    path: '/datenschutz',
    name: 'datenschutz',
    component: () =>
      import(/* webpackChunkName: "datenschutz" */ './../views/footer/aboutProject/Main.vue'), // eslint-disable-line
  },
  {
    path: '/message',
    name: 'message',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "message" */ './../views/footer/message/Main.vue'), // eslint-disable-line
  },
  {
    path: '/message/final',
    name: 'message-final',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "messageFinal" */ './../views/footer/message/FinalMessagePage.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/create/',
    name: 'heimabendCreate',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendCreate" */ './../views/heimabend/create/Main.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/create/final',
    name: 'heimabendCreateFinale',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendCreateFinale" */ './../views/heimabend/create/FinalEventPage.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/update/:id',
    name: 'heimabendUpdate',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "heimabendUpdate" */ './../views/heimabend/create/Main.vue'), // eslint-disable-line
  },
  {
    path: '/heimabend/:id',
    name: 'heimabendDetails',
    meta: { sitemap: { ignoreRoute: true } },
    // meta: {
    //   sitemap: {
    //     slugs: async () => await getEvents(), //eslint-disable-line
    //   },
    // },
    component: () =>
      import(/* webpackChunkName: "heimabendDetails" */ './../views/heimabend/details/Main.vue'), // eslint-disable-line
  },
  {
    path: '/ranking',
    name: 'ranking-overview',
    component: () =>
      import(/* webpackChunkName: "rankingOverview" */ './../views/inspi/ranking/Main.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/start',
    name: 'scoring-start',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringStart" */ './../views/inspi/scoring/Landing.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/setup',
    name: 'scoring-setup',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringSetup" */ './../views/inspi/scoring/Setup.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/test/:id',
    name: 'scoring-test',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import(/* webpackChunkName: "scoringTest" */ './../views/inspi/scoring/Test.vue'), // eslint-disable-line
  },
  {
    path: '/scoring/final/:id',
    name: 'scoring-final',
    meta: { sitemap: { ignoreRoute: true } },
    component: () =>
      import( /* webpackChunkName: "scoringFinal" */ './../views/inspi/scoring/FinalScoringPage.vue'), // eslint-disable-line
  },
  {
    path: '/inspi/easter-egg',
    name: 'inspi-easter-egg',
    meta: { sitemap: { ignoreRoute: true } },

    component: () =>
      import(/* webpackChunkName: "inspiEasterEgg" */ './../views/inspi/easterEgg/Main.vue'), // eslint-disable-line
  },
  {
    path: '/admin',
    name: 'admin',
    meta: { sitemap: { ignoreRoute: true } },
    component: () => import(/* webpackChunkName: "admin" */ './../views/admin/Main.vue'), // eslint-disable-line
    children: [
      {
        path: 'overview',
        name: 'admin-overview',
        component: () =>
          import(/* webpackChunkName: "adminOverview" */ './../views/admin/overview/Main.vue'), // eslint-disable-line
      },
      {
        path: 'heimabend',
        name: 'admin-heimabend',
        component: () =>
          import(/* webpackChunkName: "adminHeimabend" */ './../views/admin/heimabend/Main.vue'), // eslint-disable-line
      },
      {
        path: 'event-of-the-week-create',
        name: 'admin-heimabend-event-of-the-week-create',
        component: () => import(/* webpackChunkName: "AdminEventOfWeek" */ './../views/admin/heimabend/eventOfTheWeek/CreateForm.vue'), // eslint-disable-line
      },
      {
        path: 'tag',
        component: () =>
          import(/* webpackChunkName: "adminTag" */ './../views/admin/tag/Main.vue'), // eslint-disable-line
      },
      {
        path: 'message',
        component: () =>
          import(/* webpackChunkName: "adminMessage" */ './../views/admin/message/Main.vue'), // eslint-disable-line
      },
      {
        path: 'material',
        component: () =>
          import(/* webpackChunkName: "adminMaterial" */ './../views/admin/material/Main.vue'), // eslint-disable-line
      },
      {
        path: 'score',
        component: () =>
          import(/* webpackChunkName: "adminScore" */ './../views/admin/score/Main.vue'), // eslint-disable-line
      },
    ],
  },
  {
    path: '/inspirations',
    name: 'inspirations',
    component: () =>
      import(/* webpackChunkName: "inspirations" */ './../views/inspi/inspirations/Main.vue'), // eslint-disable-line
  },
];

export default routes;

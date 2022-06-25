require = require("esm")(module); // eslint-disable-line
// const { routes } = require('./src/router/index.js'); // eslint-disable-line

module.exports = {
  transpileDependencies: ['vuetify'],
  configureWebpack: {
    devServer: {
      clientLogLevel: 'info',
      watchOptions: {
        poll: true,
      },
    },
  },
  // pluginOptions: {
  //   sitemap: {
  //     baseURL: 'https://inspirator.dpbm.de',
  //     routes,
  //     pretty: true,
  //     outputDir: 'public/',
  //   },
  // },
};

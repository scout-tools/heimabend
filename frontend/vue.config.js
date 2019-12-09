module.exports = {
  transpileDependencies: [
    'vuetify',
  ],
  configureWebpack: {
    devServer: {
      clientLogLevel: 'info',
      watchOptions: {
        poll: true,
      },
    },
  },
};

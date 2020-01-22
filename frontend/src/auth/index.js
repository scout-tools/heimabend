import axios from 'axios';

export default {
  user: {
    authenticated: false,
  },

  interceptorsSetup(store, router) {
    axios.interceptors.request.use((config) => {
      const { accessToken } = store.state;
      if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`; // eslint-disable-line no-param-reassign
      }
      return config;
    }, err => Promise.reject(err));

    axios.interceptors.response.use((response) => {
      store.commit('apiIsDown', false);
      return response;
    }, (error) => {
      if (error.response === undefined) {
        debugger;
        store.commit('apiIsDown', true);
      }

      if (error.response.status === 401) {
        store.commit('clearTokens');
        router.push({ name: 'overview' });
      }
      return Promise.reject(error);
    });
  },
};

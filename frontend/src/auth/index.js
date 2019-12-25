import axios from 'axios';

export default {
  user: {
    authenticated: false,
  },

  interceptorsSetup(store) {
    axios.interceptors.request.use((config) => {
      const { accessToken } = store.state;
      if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`; // eslint-disable-line no-param-reassign
      }
      return config;
    }, err => Promise.reject(err));
    axios.interceptors.response.use(response => response.data, (error) => {
      // Do something with response error
      if (error.response.status === 401) {
        store.commit('clearTokens');
        this.$router.push({ name: 'main' });
      }
      console.log(error.response);
      return Promise.reject(error);
    });
  },
};

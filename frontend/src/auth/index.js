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
      console.log(error.response);
      return Promise.reject(error);
    });
  },
};

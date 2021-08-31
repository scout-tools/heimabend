import axios from 'axios';

export const serviceMixin = { // eslint-disable-line
  methods: {
    async postExperimentItem(event, experiment, score) {
      const path = `${process.env.VUE_APP_API}basic/experiment-item/`;
      return axios.post(path, {
        event,
        experiment,
        score,
      });
    },
    async getTopViews() {
      const path = `${process.env.VUE_APP_API}basic/top-views/`;
      return axios.get(path);
    },
    async getEventOfTheWeekHistory(params = []) {
      const path = `${process.env.VUE_APP_API}basic/event-of-the-week/?&timestamp=${new Date().getTime()}`;
      return axios.get(path, { params });
    },
    async getNextEvents(eventId) {
      const path = `${process.env.VUE_APP_API}basic/next-best-heimabend/?event=${eventId}`;
      return axios.get(path);
    },
    async getService(messageType) {
      const path = `${process.env.VUE_APP_API}basic/${messageType}/?&timestamp=${new Date().getTime()}`;
      return axios.get(path);
    },
    async getService2(messageType, params = []) {
      const path = `${process.env.VUE_APP_API}basic/${messageType}/?&timestamp=${new Date().getTime()}`;
      return axios.get(path, { params });
    },
    getItems(messageType) {
      this.getService(messageType)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {});
    },
    refreshStoreItems(serviceName, setter) {
      this.getService(serviceName)
        .then((res) => {
          this.$store.commit(setter, res.data);
        });
    },
  },
};

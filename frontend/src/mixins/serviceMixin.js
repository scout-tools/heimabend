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
    async getNextEvents(eventId) {
      const path = `${process.env.VUE_APP_API}basic/next-best-heimabend/?event=${eventId}`;
      return axios.get(path);
    },
    async getService(messageType) {
      const path = `${process.env.VUE_APP_API}basic/${messageType}/`;
      return axios.get(path);
    },
    getItems(messageType) {
      this.getService(messageType)
        .then((res) => {
          this.items = res.data;
        })
        .catch(() => {});
    },
  },
};

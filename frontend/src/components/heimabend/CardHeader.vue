<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on, attrs }">
      <v-card-title v-bind="attrs" v-on="on" class="pa-0">
        <v-list-item
          two-line
          class="whiteText justify-center text-center"
          :class="titleClass(item)"
        >
          <v-list-item-content>
            <v-list-item-title class="whiteText justify-center text-center">
              {{ item.title }}
            </v-list-item-title>
            <v-list-item-subtitle class="whiteText justify-center text-center">
              {{ getType(item) }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card-title>
    </template>
    <span>{{ getToolTipTextClass(item.tags) }}</span>
  </v-tooltip>
</template>


<script>
import store from '@/store'; // eslint-disable-line
import { mapGetters } from 'vuex';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

export default {
  mixins: [serviceMixin],
  props: {
    item: Object,
  },
  data() {
    return {
      dataReady: false,
      delay: '0.1s',
      API_URL: process.env.VUE_APP_API,
      showError: false,
      showSuccess: false,
      showErrorLiked: false,
      timeout: 3000,
      showSuccessLiked: false,
      alreadyVotedSnackbar: false,
      emptyMaterialText: 'Juhu, kein Material nötig ^^',
      data: [],
      count: 0,
      show: false,
      rating: 3,
      addRating: 0,
    };
  },
  computed: {
    ...mapGetters(['tags', 'liked', 'isAuthenticated', 'isScoringMode']),
  },
  methods: {
    titleClass(item) {
      let styleClass = '';
      styleClass = this.$vuetify.breakpoint.mdAndUp
        ? 'headline font-weight-medium'
        : 'title';
      styleClass = `${styleClass} ${this.getHeaderColorClass(item.tags)}`;
      return styleClass;
    },
    getHeaderColorClass(tags) {
      let colorclass = 'color-scout';
      const hasWo = tags.includes(50);
      const hasScout = tags.includes(51);
      const hasRover = tags.includes(52);
      if (hasWo && hasScout) {
        colorclass = 'color-wo-scout';
      } else if (hasWo) {
        colorclass = 'color-wo';
      } else if (hasScout && hasRover) {
        colorclass = 'color-scout-rover';
      } else if (hasScout) {
        colorclass = 'color-scout';
      } else if (hasRover) {
        colorclass = 'color-rover';
      }
      return colorclass;
    },
    getToolTipTextClass(tags) {
      let text = 'Für Pfadfinder_innen geeignet';

      const hasWo = tags.includes(50);
      const hasScout = tags.includes(51);
      const hasRover = tags.includes(52);

      if (hasWo && hasScout) {
        text = 'Für Wölflinge und Pfadis geeignet';
      } else if (hasWo) {
        text = 'Für Wölflinge geeignet';
      } else if (hasScout && hasRover) {
        text = 'Für Pfadis und Ältere geeignet';
      } else if (hasScout) {
        text = 'Für Pfadis geeignet';
      } else if (hasRover) {
        text = 'Für Ältere geeignet';
      }
      return text;
    },
    getType(event) {
      const tagsObject = this.tags.filter(item => event.tags.includes(item.id)); // eslint-disable-line
      const containsCategoryId = tagsObject.filter(
        ( // eslint-disable-line
          tag // eslint-disable-line
        ) => [4].includes(tag.category) // eslint-disable-line
      ); // eslint-disable-line
      if (containsCategoryId.length) {
        return containsCategoryId[0].name;
      }
      return 'kein Typ';
    },
  },
};
</script>

<style scoped>
.color-wo-scout {
  background: linear-gradient(
    190deg,
    rgba(26, 75, 126, 1) 0%,
    rgba(26, 75, 126, 1) 30%,
    rgba(230, 154, 23) 70%,
    rgba(230, 154, 23) 100%
  );
}
.color-scout-rover {
  background: linear-gradient(
    10deg,
    rgba(26, 75, 126, 1) 0%,
    rgba(26, 75, 126, 1) 30%,
    rgba(148, 47, 34) 70%,
    rgba(148, 47, 34) 100%
  );
}
.color-scout {
  background: rgba(26, 75, 126, 1) 30%;
}
.color-wo {
  background: rgb(230, 154, 23);
}
.color-rover {
  background: rgb(148, 47, 34);
}
.v-card__title{
  padding: 0 !important;
}
</style>

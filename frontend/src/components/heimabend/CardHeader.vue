<template>
  <v-tooltip bottom :disabled="preview">
    <template v-slot:activator="{ on, attrs }">
      <v-card-title v-bind="attrs" v-on="on" class="pa-0">
        <v-list-item
          two-line
          class="justify-center text-truncate"
          :class="getHeaderColorClass(item.tags)"
        >
          <v-list-item-content>
            <v-list-item-title class="whiteText justify-center text-center text-truncate"
              :class="titleClass()">
              {{ item.title }}
            </v-list-item-title>
            <v-list-item-subtitle class="whiteText justify-center text-center"
              :class="subTitleClass()">
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
import { mapGetters } from 'vuex';

// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';

export default {
  mixins: [serviceMixin],
  props: {
    item: Object,
    preview: {
      type: Boolean,
      default: false,
    },
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
    titleClass() {
      let styleClass = '';
      styleClass = this.$vuetify.breakpoint.mdAndUp && !this.preview
        ? 'text-h5 font-weight-medium'
        : 'text-subtitle-1';
      return styleClass;
    },
    subTitleClass() {
      let styleClass = '';
      styleClass = this.$vuetify.breakpoint.mdAndUp && !this.preview
        ? 'text-body-1 font-weight-regular'
        : 'text-body-2 font-weight-regular';
      return styleClass;
    },
    getHeaderColorClass(tags) {
      let colorclass = 'inspiBlue';
      if (!tags) {
        return colorclass;
      }
      const hasWo = tags.includes(50);
      const hasScout = tags.includes(51);
      const hasRover = tags.includes(52);
      if (hasWo && hasScout) {
        colorclass = 'inspiBlue';
      } else if (hasWo) {
        colorclass = 'inspiOrange';
      } else if (hasScout && hasRover) {
        colorclass = 'inspiBlue';
      } else if (hasScout) {
        colorclass = 'inspiBlue';
      } else if (hasRover) {
        colorclass = 'inspiRed';
      }
      return colorclass;
    },
    getToolTipTextClass(tags) {
      let text = 'Für Pfadfinder_innen geeignet';

      if (!tags) {
        return text;
      }

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
      if (!event.tags) {
        return 'laden...';
      }
      let returnString = 'kein Typ';
      const tagsObject = this.tags.filter(item => event.tags.includes(item.id)); // eslint-disable-line
      const containsCategoryId = tagsObject.filter(
        ( // eslint-disable-line
          tag // eslint-disable-line
        ) => [4].includes(tag.category) // eslint-disable-line
      ); // eslint-disable-line
      if (containsCategoryId.length) {
        returnString = '';
        containsCategoryId.forEach((item, index) => {
          returnString = `${returnString} ${index ? '&' : ''} ${item.name}`;
        });
      }
      return returnString;
    },
  },
};
</script>

<style scoped>
.color-scout {
  background: rgba(26, 75, 126, 1) 30%;
}
.color-wo {
  background: rgb(230, 126, 0);
}
.color-rover {
  background: rgb(148, 47, 34);
}
.v-card__title{
  padding: 0 !important;
}
</style>

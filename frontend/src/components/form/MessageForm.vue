<template>
  <v-form v-model="valid">
    <v-container fluid>
      <v-text-field
        v-model="data.createdBy"
        :error-messages="createdByErrors"
        prepend-icon="mdi-campfire"
        label="Dein Fahrtenname (freiwillig)"
        required
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{ 'Gib hier deinen Pfadfindernamen ein.' }}
            </span>
          </v-tooltip>
        </template>
      </v-text-field>
      <v-text-field
        v-model="data.createdByEmail"
        :error-messages="createdByEmailErrors"
        label="Deine E-Mail Adresse (freiwillig)"
        prepend-icon="mdi-at"
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{
                'Gib hier die E-Mail Adresse ein auf die wir Antworten können.'
              }}
            </span>
          </v-tooltip>
        </template></v-text-field
      >
      <v-select
        v-model="data.messageType"
        v-if="showType"
        :items="filteredMessageType"
        item-value="id"
        item-text="name"
        :error-messages="messageTypeErrors"
        prepend-icon="mdi-message"
        label="Art der Nachricht"
        required
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{ 'Wähle aus wie wir deine Nachricht einsortieren können.' }}
            </span>
          </v-tooltip>
        </template>
      </v-select
      >
      <v-textarea
        v-model="data.messageBody"
        label="Dein Text"
        required
        filled
        auto-grow
        prepend-icon="mdi-text"
        :error-messages="messageBodyErrors"
        hint="Hier deine Nachricht eintippen."
        v-on:keyup="onKeyPress"
      >
        <template slot="append">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="success" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>
              {{ 'Gib hier den Namen der Schlafstätte ein.' }}
            </span>
          </v-tooltip>
        </template>
      </v-textarea>

      <!-- <v-btn class="mr-4" color="primary" @click="submit"> Absenden </v-btn> -->
    </v-container>
  </v-form>
</template>


<script>
import { mapGetters } from 'vuex';
// eslint-disable-next-line
import { validationMixin } from 'vuelidate';
// eslint-disable-next-line
import { serviceMixin } from '@/mixins/serviceMixin.js';
import {
  required,
  minLength,
  maxLength,
  email,
} from 'vuelidate/lib/validators';

export default {
  mixins: [validationMixin, serviceMixin],
  props: {
    showEmail: {
      type: Boolean,
      default: true,
    },
    showName: {
      type: Boolean,
      default: true,
    },
    showType: {
      type: Boolean,
      default: true,
    },
    allowedMessageTypes: {
      type: String,
      default: 'all',
    },
  },
  data: () => ({
    data: {
      createdBy: '',
      createdByEmail: '',
      messageType: null,
      messageBody: '',
    },
    showError: false,
    API_URL: process.env.VUE_APP_API,
    showSuccess: false,
    valid: false,
    checkbox: false,
  }),
  validations: {
    data: {
      createdBy: {
        minLength: minLength(3),
        maxLength: maxLength(20),
      },
      createdByEmail: {
        email,
      },
      messageType: { required },
      messageBody: {
        required,
        minLength: minLength(5),
        maxLength: maxLength(5000),
      },
    },
  },
  watch: {
    filteredMessageType() {
      this.data.messageType = this.filteredMessageType[0].id; // eslint-disable-line
    },
  },
  computed: {
    ...mapGetters(['messageType']),
    filteredMessageType() {
      if (this.allowedMessageTypes === 'comment') {
        return this.messageType.filter(item => item.isComment === true);
      }
      if (this.allowedMessageTypes === 'question') {
        return this.messageType.filter(item => item.id === 5);
      }

      return this.messageType;
    },

    createdByErrors() {
      const errors = [];
      if (!this.$v.data.createdBy.$dirty) return errors;
      !this.$v.data.createdBy.minLength && errors.push('Der Name ist zu kurz'); // eslint-disable-line
      !this.$v.data.createdBy.maxLength && errors.push('Der Name ist zu lang'); // eslint-disable-line
      return errors;
    },
    createdByEmailErrors() {
      const errors = [];
      if (!this.$v.data.createdByEmail.$dirty) return errors;
      !this.$v.data.createdByEmail.email && // eslint-disable-line
        errors.push('Bitte prüfe die Adresse nochmal'); // eslint-disable-line
      return errors;
    },
    messageTypeErrors() {
      const errors = [];
      if (!this.$v.data.messageType.$dirty) return errors;
      !this.$v.data.messageType.required && // eslint-disable-line
        errors.push('Wir müssen wissen welcher Art dein Anliegen ist.'); // eslint-disable-line
      return errors;
    },
    messageBodyErrors() {
      const errors = [];
      if (!this.$v.data.messageBody.$dirty) return errors;
      !this.$v.data.messageBody.minLength && errors.push('Nachricht ist zu kurz'); // eslint-disable-line
      !this.$v.data.messageBody.maxLength && errors.push('Nachricht ist zu lang'); // eslint-disable-line
      !this.$v.data.messageBody.required && errors.push('Die Nachricht ist nötig.'); // eslint-disable-line
      return errors;
    },
  },

  methods: {
    onKeyPress() {
      this.validate();
      if (this.valid) {
        this.$emit('input', this.data);
      }
    },
    validate() {
      this.$v.$touch();
      this.valid = !this.$v.$anyError;
    },
  },
  created() {
    this.refreshStoreItems('message-type', 'setMessageType');
  },
};
</script>

<template>
  <v-container fluid>
    <v-row>
      <router-link :to="{ name: 'overview' }" class="no-underline mt-4 ml-4">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              fab
              small
              outlined
              color="primary"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </template>
          <span>Zurück zum Inspirator</span>
        </v-tooltip>
      </router-link>
    </v-row>
  </v-container>
</template>

<script>
export default {

};
</script>

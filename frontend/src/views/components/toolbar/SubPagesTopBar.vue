<template>
<div>
  <v-toolbar
    flat
    dense
    fixed>
    <router-link
      :to="{ name: 'overview'}"
      class="no-underline"
    >
      <v-btn text large icon>
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </router-link>
    <v-toolbar-title>
    </v-toolbar-title>
    <v-spacer></v-spacer>
  </v-toolbar>
    <v-divider/>
</div>
</template>

<script>
export default {

};
</script>

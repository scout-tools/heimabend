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
        <v-icon>mdi-arrow-left</v-icon>
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

<style scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
    opacity: 0.4;
    color: rgb(192, 214, 192)
}
.v-btn--active:before {
    opacity: 0.4;
    color: rgb(149, 201, 240)
}

.theme--light.v-btn--active:hover::before,
.theme--light.v-btn--active::before {
  opacity: 0.3;
}
</style>

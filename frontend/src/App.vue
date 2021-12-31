<template>
  <v-app>
  <div id="app">
    <main-comp/>
  </div>
  </v-app>
</template>

<script>
import MainComp from './views/Main.vue';

export default {
  components: {
    MainComp,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #4171A4;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #4171A4;
}
</style>

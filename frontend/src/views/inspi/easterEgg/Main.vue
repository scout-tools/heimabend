<template>
  <v-container class="wrap" fluid>
    <v-img class="wrap2" :src="require('@/assets/inspi/inspi_flying.png')" max-width="200" />
    <div class="cloud0"></div>
    <div class="cloud00"></div>
    <div class="cloud1"></div>
    <div class="cloud2"></div>
    <div class="cloud3"></div>
    <div class="cloud4"></div>
    <div class="cloud5"></div>
    <div class="cloud6"></div>

    <div class="debri1"></div>
    <div class="debri2"></div>
    <div class="debri3"></div>
    <div class="debri4"></div>
    <div class="debri5"></div>
    <div class="debri6"></div>
  </v-container>
</template>

<script>
export default {};
</script>

<style scoped>
.wrap {
  position: relative;
  background-color: rgb(8, 125, 241) !important;
  margin: 0px !important;
  height: 100vh !important;
}
/* THE BEE   THE BEE   THE BEE   THE BEE    */
@keyframes dodging1 {
  0% {
    top: 0;
  }
  50% {
    top: 75px;
  }
  100% {
    top: 0;
  }
}
.wrap2 {
  z-index: 1;
  position: absolute;
  left: 20%;
  margin-top: 100px;
  animation: dodging1 1s ease-in-out infinite;
}
/* EYES EYES EYES EYES  */
/* DEBRIS DEBRIS DEBRIS DEBRIS  */
@keyframes debri {
  0% {
    left: -150px;
  }
  100% {
    left: 125%;
  }
}
$debri-duration: random(1) - 0.4 + s;
$debri-delay: 0.5s;
.debri1 {
  position: absolute;
  width: 100px;
  height: 1px;
  background-color: #000;
  top: 300px;
  left: -150px;
  animation: debri $debri-duration $debri-delay ease-out infinite;
}
.debri2 {
  position: absolute;
  width: 75px;
  height: 2px;
  background-color: #000;
  top: 170px;
  left: -150px;
  animation: debri $debri-duration $debri-delay + -0.1 ease-out infinite;
}
.debri3 {
  position: absolute;
  width: 60px;
  height: 2px;
  background-color: #000;
  top: 275px;
  left: -150px;
  z-index: -1;
  animation: debri $debri-duration $debri-delay + 0.95 ease-out infinite;
}
.debri4 {
  position: absolute;
  width: 80px;
  height: 1px;
  background-color: #000;
  top: 400px;
  left: -150px;
  animation: debri $debri-duration $debri-delay + -0.2 ease-out infinite;
}
.debri5 {
  position: absolute;
  width: 90px;
  height: 2px;
  background-color: #000;
  top: 315px;
  left: -150px;
  animation: debri $debri-duration $debri-delay + 0.3 ease-out infinite;
}
.debri6 {
  position: absolute;
  width: 100px;
  height: 2px;
  background-color: #000;
  top: 265px;
  left: -150px;
  z-index: -1;
  animation: debri $debri-duration $debri-delay + 0.2 ease-out infinite;
}
/* DEBRIS DEBRIS DEBRIS DEBRIS  */
/* CLOUDS CLOUDS CLOUDS CLOUDS  */
@keyframes cloud {
  0% {
    left: -150px;
  }
  100% {
    left: 125%;
  }
}
@keyframes cloud2 {
  0% {
    left: -150px;
  }
  100% {
    left: 175%;
  }
}
.cloud0 {
  position: absolute;
  height: 20px;
  width: 20px;
  top: 30px;
  left: -150px;
  border-radius: 100%;
  box-shadow: 37px 40px 1px rgba(255, 255, 255, 1),
    20px 45px 1px rgba(255, 255, 255, 1),
    6px 40px 1px rgba(255, 255, 255, 1),
    20px 35px 1px rgba(255, 255, 255, 1),
    35px 35px 1px rgba(255, 255, 255, 1);
  animation: cloud 12s linear infinite;
  z-index: 0;
}
.cloud00 {
  position: absolute;
  height: 20px;
  width: 20px;
  top: 220px;
  left: -350px;
  border-radius: 100%;
  box-shadow: 37px 40px 1px rgba(255, 255, 255, 1),
    20px 45px 1px rgba(255, 255, 255, 1),
    8px 40px 1px rgba(255, 255, 255, 1),
    23px 35px 1px rgba(255, 255, 255, 1),
    30px 35px 1px rgba(255, 255, 255, 1);
  animation: cloud 14s linear infinite;
  z-index: 0;
}
.cloud1 {
  position: absolute;
  height: 30px;
  width: 30px;
  top: 100px;
  left: -150px;
  border-radius: 100%;
  box-shadow: 50px 50px 2px rgba(255, 255, 255, 0.95),
    30px 55px 1px rgba(255, 255, 255, 0.95),
    10px 50px 1px rgba(255, 255, 255, 0.95),
    20px 35px 1px rgba(255, 255, 255, 0.95),
    40px 35px 1px rgba(255, 255, 255, 0.95);
  animation: cloud 10s linear infinite;
  z-index: 0;
}
.cloud2 {
  position: absolute;
  height: 60px;
  width: 60px;
  top: 0px;
  left: -950px;
  border-radius: 100%;
  box-shadow: 100px 200px 2px rgba(255, 255, 255, 0.95),
    50px 205px 1px rgba(255, 255, 255, 0.95),
    10px 200px 1px rgba(255, 255, 255, 0.95),
    35px 170px 1px rgba(255, 255, 255, 0.95),
    70px 170px 1px rgba(255, 255, 255, 0.95);
  animation: cloud 5s 2s linear infinite;
  z-index: 0;
}
.cloud3 {
  position: absolute;
  height: 100px;
  width: 100px;
  top: 200px;
  left: -950px;
  border-radius: 100%;
  box-shadow: 150px 200px 2px rgba(255, 255, 255, 0.95),
    75px 205px 1px rgba(255, 255, 255, 0.95),
    10px 200px 1px rgba(255, 255, 255, 0.95),
    45px 150px 1px rgba(255, 255, 255, 0.95),
    120px 150px 1px rgba(255, 255, 255, 0.95);
  animation: cloud2 2.8s 1s linear infinite;
  z-index: 1;
}

.cloud4 {
  position: absolute;
  height: 100px;
  width: 100px;
  top: 300px;
  left: -1000px;
  border-radius: 100%;
  box-shadow: 150px 200px 2px rgba(255, 255, 255, 0.95),
    75px 205px 1px rgba(255, 255, 255, 0.95),
    10px 200px 1px rgba(255, 255, 255, 0.95),
    45px 150px 1px rgba(255, 255, 255, 0.95),
    120px 150px 1px rgba(255, 255, 255, 0.95);
  animation: cloud2 4s 1s linear infinite;
  z-index: 1;
}

.cloud5 {
  position: absolute;
  height: 100px;
  width: 100px;
  top: 50px;
  left: -700px;
  border-radius: 100%;
  box-shadow: 150px 200px 2px rgba(255, 255, 255, 0.95),
    75px 205px 1px rgba(255, 255, 255, 0.95),
    10px 200px 1px rgba(255, 255, 255, 0.95),
    45px 150px 1px rgba(255, 255, 255, 0.95),
    120px 150px 1px rgba(255, 255, 255, 0.95);
  animation: cloud2 5s 1s linear infinite;
  z-index: 1;
}
.cloud6 {
  position: absolute;
  height: 100px;
  width: 100px;
  top: 50px;
  left: -950px;
  border-radius: 100%;
  box-shadow: 150px 200px 2px rgba(255, 255, 255, 0.95),
    75px 205px 1px rgba(255, 255, 255, 0.95),
    10px 200px 1px rgba(255, 255, 255, 0.95),
    45px 150px 1px rgba(255, 255, 255, 0.95),
    120px 150px 1px rgba(255, 255, 255, 0.95);
  animation: cloud2 7s 1s linear infinite;
  z-index: 1;
}

/* CLOUDS CLOUDS CLOUDS CLOUDS  */
</style>

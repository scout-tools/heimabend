<template>
<v-container class="fullscreen fluid pa-0">
  <div class="wrap">
      <v-img class="wrap2" :src="require('@/assets/inspi.png')" max-width="200" />
    <div class="cloud1"></div>
    <div class="cloud2"></div>
    <div class="cloud3"></div>

    <div class="debri1"></div>
    <div class="debri2"></div>
    <div class="debri3"></div>
    <div class="debri4"></div>
    <div class="debri5"></div>
    <div class="debri6"></div>
  </div>
</v-container>
</template>

<script>
export default {};
</script>

<style scoped>
.fullscreen {
  height: 105vh !important;
  width: 105vh !important;
  background-color: rgb(8, 125, 241) !important;
}
.wrap {
  position: relative;
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
/* THE BEE   THE BEE   THE BEE   THE BEE    */
/* BODY BODY BODY BODY  */
.body {
  position: absolute;
  top: 250px;
  left: 250px;
  height: 85px;
  width: 75px;
  border-radius: 100%;
  background-color: #ffb733;
  box-shadow: 20px 0 0 #000, 40px -3px 0 #ffb733, 60px -7px 0 #000,
    80px -11px 0 #ffb733;
}
/* BODY BODY BODY BODY  */
/* WINGS WINGS WINGS WINGS */
@keyframes flutter2 {
  0% {
    transform: rotate(80deg);
  }
  50% {
    transform: rotate(100deg);
  }
}
@keyframes flutter1 {
  0% {
    transform: rotate(20deg);
  }
  50% {
    transform: rotate(40deg);
  }
}
.wing1 {
  position: absolute;
  height: 55px;
  width: 55px;
  top: 210px;
  left: 280px;
  transform: rotate(20deg);
  transform-origin: bottom right;
  border-top-right-radius: 100%;
  border-bottom-left-radius: 100%;
  border-top-left-radius: 10px;
  background-color: #ddd;
  z-index: -1;
  filter: blur(1px);
  animation: flutter1 0.01s linear reverse infinite;
}
.wing2 {
  position: absolute;
  height: 55px;
  width: 55px;
  top: 205px;
  left: 290px;
  transform: rotate(80deg);
  transform-origin: bottom right;
  border-top-right-radius: 100%;
  border-bottom-left-radius: 100%;
  border-top-left-radius: 10px;
  background-color: #ddd;
  z-index: 1;
  filter: blur(1px);
  animation: flutter2 0.01s linear infinite;
}
/* WINGS WINGS WINGS WINGS */
/* STINGER STINGER STINGER STINGER  */

.stinger {
  position: absolute;
  height: 55px;
  width: 55px;
  top: 255px;
  left: 355px;
  transform: rotate(320deg);
  border-top-right-radius: 50%;
  border-bottom-left-radius: 100%;
  border-top-left-radius: 10px;
  background-color: #000;
  z-index: -1;
}

/* STINGER STINGER STINGER STINGER  */
/* EYES EYES EYES EYES  */
.eyes {
  position: absolute;
  height: 25px;
  width: 25px;
  top: 260px;
  left: 250px;
  background-color: #eee;
  box-shadow: 20px 0 0 #eee;
  border-radius: 100%;
  .pupil {
    position: absolute;
    height: 4px;
    width: 4px;
    top: 13px;
    left: 2px;
    background-color: #000;
    border-radius: 100%;
    box-shadow: 20px 0 0 #000;
  }
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

/* CLOUDS CLOUDS CLOUDS CLOUDS  */
</style>

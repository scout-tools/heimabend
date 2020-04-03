<template>
  <div>
    <full-page ref="fullpage" :options="options" id="fullpage">
      <why-step class="section"/>
      <div class="section">Second section ...</div>
    </full-page>
  </div>
</template>

<script>
import WhyStep from './step/Why.vue';

export default {

  components: {
    WhyStep,
  },
  data: () => ({

  }),
};
</script>

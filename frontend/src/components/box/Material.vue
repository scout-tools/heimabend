<template>
<div>
  <v-card flat color="#F6F6F6">
    <v-card-title align="center" justify="center" class="headline">
      Materialliste
    </v-card-title>
    <v-card-text>
    <div v-if="materialList.length" class="text-left font-italic ml-10">
      <ul>
        <li v-for="(item, index4) in materialList" :key="index4">
          {{
            item.quantity +
            ' ' +
            item.materialUnitStr +
            ' ' +
            item.materialNameStr
          }}
        </li>
      </ul>
    </div>
    <div v-else class="text-left">
      <ul>
        <li>
          {{ 'Kein Material nötig' }}
        </li>
      </ul>
    </div>
    </v-card-text>
  </v-card>
</div>
</template>

<script>
export default {
  props: {
    materialList: Array,
    isDetailsView: Boolean,
  },
};
</script>

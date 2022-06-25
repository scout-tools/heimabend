<template>
  <v-card flat align="center" justify="center" color="#F6F6F6">
    <v-card-text>
      <v-container v-if="materialList.length">
        <v-row align="center" justify="center"></v-row>
        <h2> Materialliste </h2>
        <v-row class="mt-3">
          <v-col
            align="start"
            justify="start"
            cols="6"
            class="ma-0"
            v-for="(item, index4) in materialList"
            :key="index4"
          >
            <h4 class="ma-0">
              {{
                '- ' +
                item.quantity +
                ' ' +
                item.materialUnitStr +
                ' ' +
                item.materialNameStr
              }}
            </h4>
          </v-col>
        </v-row>
      </v-container>
      <div v-else class="text-left">
        <ul>
          <li>
            {{ 'Kein Material nötig' }}
          </li>
        </ul>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    materialList: Array,
    isDetailsView: Boolean,
  },
};
</script>

<template>
  <v-row justify="space-around">
    <v-menu offset-y>
      <template v-slot:activator="{ attrs, on }">
        <v-btn
          class="mx-2"
          icon
          small
          dark
          color="black"
          v-bind="attrs"
          v-on="on"
        >
          <v-icon dark> mdi-dots-vertical </v-icon>
        </v-btn>
      </template>

      <v-list>
        <v-list-item link @click="onPublishClick(data)">
          <v-list-item-avatar>
            <v-icon color="green lighten-1" big> mdi-eye-outline </v-icon>
          </v-list-item-avatar>
          <v-list-item-title>
            {{ getPublishString(data.isActive) }}
          </v-list-item-title>
        </v-list-item>
        <v-list-item link @click="openViewNewTab(data.id)">
          <v-list-item-avatar>
            <v-icon color="blue lighten-1" big> mdi-book-open </v-icon>
          </v-list-item-avatar>
          <v-list-item-title> Öffnen</v-list-item-title>
        </v-list-item>
        <v-list-item link @click="openEditNewTab(data.id)">
          <v-list-item-avatar>
            <v-icon color="orange lighten-1" big> mdi-pencil </v-icon>
          </v-list-item-avatar>
          <v-list-item-title>Editieren</v-list-item-title>
        </v-list-item>
        <v-list-item link @click="onDeleteClick(data)">
          <v-list-item-avatar>
            <v-icon color="red lighten-1" big>mdi-delete-outline</v-icon>
          </v-list-item-avatar>
          <v-list-item-title>Löschen</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

<script>
export default {
  props: {
    data: Object,
  },
  data: () => ({}),
  methods: {
    getPublishString(isActive) {
      return isActive ? 'Zurück nehmen' : 'Veröffentlichen';
    },
    openViewNewTab(id) {
      const routeData = this.$router.resolve({
        name: 'heimabendDetails',
        params: { id },
      });
      window.open(routeData.href, '_blank').focus();
    },
    openEditNewTab(id) {
      const routeData = this.$router.resolve({
        name: 'heimabendUpdate',
        params: { id },
      });
      window.open(routeData.href, '_blank').focus();
    },
    onDeleteClick(item) {
      this.$emit('onDeleteClick', item);
    },
    onPublishClick(item) {
      this.$emit('onPublishClick', item);
    },
  },
};
</script>

<template>
  <v-app>
    <iframe id="my_iframe" style="display: none"></iframe>
    <!-- APP BAR -->
    <v-app-bar dark app flat>
      <v-toolbar-title style="width: 250px">Dev Challenge</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat @click="$router.push('/')">Home</v-btn>
        <v-btn flat @click="$router.push('/employee')">Employees</v-btn>
        <v-btn flat @click="$router.push('/product')">Products</v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <!-- CONTENT -->
    <v-main>
      <v-container fluid style="height: 100%">
        <nuxt />
      </v-container>
    </v-main>

    <!-- FOOTER -->
    <v-footer app>
      <span class="my-1">
        <v-row> &copy; {{ new Date().getFullYear() }} </v-row>
      </span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {}
  },
  created() {},
  computed: {},
}
</script>

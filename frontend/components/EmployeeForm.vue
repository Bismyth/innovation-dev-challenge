<template>
  <v-card>
    <v-card-title> Add Employee </v-card-title>
    <v-card-text>
      <v-text-field v-model="employee.first_name" label="First Name" />
      <v-text-field v-model="employee.last_name" label="Last Name" />
      <v-text-field v-model="employee.email" label="Email" />
      <v-text-field v-model="employee.role" label="Role" />
    </v-card-text>
    <v-card-actions>
      <v-btn :disabled="lock" @click="addEmployee()" color="primary">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['employee_id'],
  data() {
    return {
      employee: {},
      lock: false,
    }
  },
  methods: {
    async addEmployee() {
      this.lock = true
      await this.$axios.$post('/employee/employee', this.employee)
      this.lock = false
      this.employee = {}
      this.$emit('save')
    },
  },
}
</script>

<style></style>

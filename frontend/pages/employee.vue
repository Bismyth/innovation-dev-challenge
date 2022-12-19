<template>
  <v-card>
    <v-card-title>
      Employee List <v-btn icon @click="dialog = true"><v-icon>mdi-plus</v-icon></v-btn></v-card-title
    >
    <v-data-table :headers="headers" :items="employees">
      <template v-slot:item.active="{ item }">
        <v-btn icon @click="deleteEmployee(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog">
      <employee-form
        @save="
          dialog = false
          getEmployees()
        "
      />
    </v-dialog>
  </v-card>
</template>

<script>
import EmployeeForm from '../components/EmployeeForm.vue'
export default {
  components: { EmployeeForm },
  created() {
    this.getEmployees()
  },

  data() {
    return {
      dialog: false,
      employees: [],
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Email', value: 'email' },
        { text: 'Role', value: 'role' },
        { text: 'Currently Employed', value: 'active' },
      ],
    }
  },

  methods: {
    async getEmployees() {
      this.employees = await this.$axios.$get('/employee/employees')
    },
    async deleteEmployee(id) {
      await this.$axios.$delete('/employee/employee', { params: { id } })
      this.getEmployees()
    },
  },
}
</script>

<style></style>

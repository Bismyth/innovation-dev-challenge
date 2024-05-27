<template>
  <v-card>
    <v-card-title>
      Product List <v-btn icon @click="newProduct()"><v-icon>mdi-plus</v-icon></v-btn></v-card-title
    >
    <v-data-table :headers="headers" :items="employees">
      <template v-slot:item.edit="{ item }">
        <v-btn icon @click="editProduct(item.id)"><v-icon>mdi-pencil</v-icon></v-btn>
      </template>

      <template v-slot:item.price="{ item }">
        <span>{{ renderPrice(item.price) }}</span>
      </template>

      <template v-slot:item.active="{ item }">
        <v-btn icon @click="deleteProduct(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
      </template>

      <template v-slot:footer>
        <td :colspan="headers.length">
          <strong>Total Price: {{ totalPrice }}</strong>
        </td>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog">
      <product-form
        :product-id="currentId"
        @save="
          dialog = false
          getProducts()
        "
      />
    </v-dialog>
  </v-card>
</template>

<script>
import ProductForm from '../components/ProductForm.vue'
export default {
  components: { ProductForm },
  created() {
    this.getProducts()
    this.currentId = undefined
    this.totalPrice = ''
  },

  data() {
    return {
      dialog: false,
      employees: [],
      currentId: undefined,
      headers: [
        { text: 'Edit', value: 'edit' },
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
        { text: 'Price', value: 'price' },
        { text: 'Category', value: 'category' },
        { text: 'Delete', value: 'active' },
      ],
    }
  },

  methods: {
    async getProducts() {
      this.employees = await this.$axios.$get('/product/products')
      this.totalPrice = this.renderPrice(this.employees.reduce((acc, v) => acc + v.price, 0))
    },
    async deleteProduct(id) {
      await this.$axios.$delete('/product/product', { params: { id } })
      this.getProducts()
    },
    renderPrice(price) {
      const AUDollar = new Intl.NumberFormat('en-AU', {
        style: 'currency',
        currency: 'AUD',
      })
      return AUDollar.format(price / 100)
    },
    editProduct(id) {
      this.currentId = id
      this.dialog = true
    },
    newProduct() {
      this.currentId = undefined
      this.dialog = true
    },
  },
}
</script>

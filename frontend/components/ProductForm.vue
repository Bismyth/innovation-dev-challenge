<template>
  <v-card>
    <v-card-title> {{ edit ? 'Edit' : 'Add' }} Product </v-card-title>
    <v-card-text>
      <v-text-field v-model="product.name" label="Name" />
      <v-text-field v-model="product.description" label="Description" />
      <v-text-field v-model="product.price" label="Price" type="number" min="0.00" max="1000.00" step="0.01" />
      <v-text-field v-model="product.category" label="Category" />
    </v-card-text>
    <v-card-actions>
      <v-btn :disabled="lock" @click="addProduct()" color="primary">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['productId'],
  data() {
    return {
      product: {},
      edit: false,
      lock: false,
    }
  },
  watch: {
    productId: {
      async handler(newVal, oldVal) {
        if (newVal === undefined) {
          this.product = {}
          this.edit = false
          return
        }

        this.product = await this.$axios.$get(`/product/product?id=${newVal}`)
        this.product.price = (this.product.price / 100).toString()
        this.edit = true
      },
    },
  },
  methods: {
    async addProduct() {
      this.lock = true
      this.product.price = Math.floor(parseFloat(this.product.price) * 100)

      if (this.edit) {
        await this.$axios.$put(`/product/product?id=${this.productId}`, this.product)
      } else {
        await this.$axios.$post('/product/product', this.product)
      }

      this.lock = false
      this.product = {}
      this.$emit('save')
    },
  },
}
</script>

<style></style>

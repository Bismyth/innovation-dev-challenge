export default ({ app, store }, inject) => {
  let currencyFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  })

  inject('utils', {
    initArray(size, value = 0) {
      let array = []
      for (let ii = 0; ii < size; ii++) {
        array[ii] = value
      }

      return array
    },
    round(value, dec = 2) {
      if (value == null || value == '') return ''
      let testValue = value
      if (typeof value == 'string') {
        testValue = parseFloat(value)
      }

      if (isNaN(testValue)) return value
      value = testValue

      let strVal = value.toFixed(dec)

      let pad = 0

      if (dec == 0) {
      } else if (!strVal.includes('.')) {
        strVal += '.'
        pad = dec
      } else {
        pad = dec - strVal.split('.')[1].length
      }

      for (let ii = 0; ii < pad; ii++) {
        strVal += '0'
      }

      return strVal
    },
    formatCurrency(val) {
      return currencyFormatter.format(val)
    },
    commarize(number) {
      if (!number) {
        return number
      }
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    },
    formatDate(date) {
      if (!date) {
        return null
      }

      if (typeof date == 'string') {
        date = new Date(date)
      }

      let day = date.getDate()
      if (day < 10) day = '0' + day

      let month = date.getMonth() + 1
      if (month < 10) month = '0' + month

      let year = date.getFullYear()

      return `${day}/${month}/${year}`
    },
    formatTime(date) {
      if (!date) {
        return null
      }

      if (typeof date == 'string') {
        date = new Date(date)
      }

      let mins = date.getMinutes()
      if (mins < 10) mins = '0' + mins

      let hours = date.getHours()
      if (hours < 10) hours = '0' + hours

      return `${hours}:${mins}`
    },
    formatDateTime(date) {
      if (!date) {
        return null
      }

      return `${this.formatDate(date)} ${this.formatTime(date)}`
    },
    toISODate(value) {
      let temp = value.toLocaleDateString('en-GB').split('/')
      return `${temp[2]}-${temp[1]}-${temp[0]}`
    },
    initDate(date) {
      return date ? new Date(date) : null
    },
    // No i did not write this, and yes i got it from google :)
    adjustColor(col, amt) {
      let usePound = false

      if (col[0] == '#') {
        col = col.slice(1)
        usePound = true
      }

      let num = parseInt(col, 16)

      let r = (num >> 16) + amt

      if (r > 255) r = 255
      else if (r < 0) r = 0

      let b = ((num >> 8) & 255) + amt

      if (b > 255) b = 255
      else if (b < 0) b = 0

      let g = (num & 255) + amt

      if (g > 255) g = 255
      else if (g < 0) g = 0

      return (usePound ? '#' : '') + (g | (b << 8) | (r << 16)).toString(16)
    },
    between(start, val, end) {
      return start <= val && val <= end
    },
    thousandSeperator(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    },
  })
}

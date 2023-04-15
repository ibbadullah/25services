const url = 'https://ipapi.co/json'

const vm = new Vue({
        el: '#app',
        data: {
          results: []
        },
        mounted() {
          axios.get(url).then(response => {
            this.results = response.data
          })
       }
});
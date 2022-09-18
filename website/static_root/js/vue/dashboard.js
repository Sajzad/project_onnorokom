var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	src: '',
    is_added: false,
  },
  created(){
    
  },
  filters: {
  },
  methods: {
    addYtdVideos(){
      this.is_added = false;
      var vm = this;
      var url = '/api/v1/video/add'
      var data = {
        'src': this.src
      }
      sendRequest(url, 'post', data)
      .then(function(response){
        vm.is_added = true;
        vm.src = ''
      })
    }
    
  }
})

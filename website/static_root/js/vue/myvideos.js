var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	videos: '',
  },
  created(){
    this.getVideos();
  },
  filters: {
  },
  methods: {
    getVideos(){
      var vm = this;
      var username = window.location.href.split('/').slice(-2,-1)
      console.log(username)
      var url = '/api/v1/' + username + '/videos'
      console.log(url)
      sendRequest(url, 'get')
      .then(function(response){
        vm.videos = response.data.videos;
      })
    }
    
  }
})

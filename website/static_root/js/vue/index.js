var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	videos: [],
  },
  created(){
    this.videoDetails();
  },
  filters: {
  },
  methods: {
    videoDetails(){
      var vm = this;
      var url = '/api/v1/videos'
      sendRequest(url, 'get')
      .then(function(response){
        vm.videos = response.data.videos;
      })
    }
  }
})

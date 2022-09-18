var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	video: '',
    likes:'',
    dislikes:'',
  },
  created(){
    this.videoDetails();
  },
  filters: {
  },
  methods: {
    videoDetails(){
      var vm = this;
      var video_id = window.location.href.split('watch/').slice(-1)
      var url = '/api/v1/video/'+video_id
      console.log(url)
      sendRequest(url, 'get')
      .then(function(response){
        vm.video = response.data.video;
      })
    },
    getLikedUsers(){
      var vm = this;
      var video_id = window.location.href.split('watch/').slice(-1)
      var url = '/api/v1/video/'+video_id+'likes'
      console.log(url)
      sendRequest(url, 'get')
      .then(function(response){
        vm.likes = response.data.likes;
      })
    },
    getDislikedUsers(){
      var vm = this;
      var video_id = window.location.href.split('watch/').slice(-1)
      var url = '/api/v1/video/'+video_id+'dislikes'
      console.log(url)
      sendRequest(url, 'get')
      .then(function(response){
        vm.dislikes = response.data.dislikes;
      })
    },
    
  }
})

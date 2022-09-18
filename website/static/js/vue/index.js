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
    },
    addLike(item){
      var vm = this;
      var url = '/api/v1/video/'+item.id+'/like'
     
      sendRequest(url, 'post')
      .then(function(response){
        vm.videoDetails();
      })
    },
    addDislike(item){
      var vm = this;
      var url = '/api/v1/video/'+item.id+'/dislike'
      
      console.log(item)
      sendRequest(url, 'post')
      .then(function(response){
        vm.videoDetails();
      })
    },
    viewCount(item){
      var url = '/api/v1/video/view/'+item.id
      console.log(url)
      sendRequest(url, 'post')
      .then(function(response){
      })
    },
  }
})

from django.urls import path, include
from . import views


app_name = "api"

urlpatterns = [
    path('videos', views.VideoApiView.as_view(), name='videos'),
    path('<username>/videos', views.MyVideosApiView.as_view(), name='videos'),
    path('video/add', views.AddVideoApiView.as_view(), name='videos'),
    path('video/<video_id>/', views.VideoDetailApiView.as_view(), name='video-details'),
    path('video/view/<video_id>', views.VideoViewCountApiView.as_view(), name='video-count'),
    path('video/<video_id>/like', views.VideoLikeApiView.as_view(), name='like'),
    path('video/<video_id>/likes', views.VideoLikesApiView.as_view(), name='likes'),
    path('video/<video_id>/dislike', views.VideoDislikeApiView.as_view(), name='dislike'),
    path('video/<video_id>/dislikes', views.DislikesApiView.as_view(), name='dislike'),

]
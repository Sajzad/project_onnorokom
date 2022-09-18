from django.urls import path, include
from . import views


app_name = "base"

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('<username>/videos', views.myvideos_view, name='myvideos'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('watch/<video_id>/', views.video_watch_view, name='video-details'),

    path('api/v1/', include('base.api.urls')),

]
from django.urls import path, include
from . import views


app_name = "api"

urlpatterns = [
    path('videos', views.VideoApiView.as_view(), name='videos'),

]
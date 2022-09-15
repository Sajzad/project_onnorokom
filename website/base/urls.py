from django.urls import path, include
from . import views


app_name = "base"

urlpatterns = [
    
    path('', views.home_view, name='home'),

    path('api/v1/', include('base.api.urls')),

]
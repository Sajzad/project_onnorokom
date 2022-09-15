from django.urls import path, include
from . import views


app_name = "authentication"

urlpatterns = [
    
    path('accounts/signin/', views.ClientSigninView.as_view(), name='signin'),
    path('accounts/signup/', views.ClientSignupView.as_view(), name='signup'),

]
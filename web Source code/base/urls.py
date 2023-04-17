from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.home, name="Homepage"),
    path('login/', views.log_in, name="login"),
    path('signup/', views.sign, name="reg"),
    path('logout/', views.logout, name="logout"),
    path('dash/', views.dash, name="dash"),
    path('profile/', views.profile, name="profile"),
    path('bot/', views.bot, name="bot"),
    path('bot/predict', views.MakePredict, name='predict')
]
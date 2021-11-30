
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from accounts import views


urlpatterns = [

    path('users/', views.UsersView.as_view(), name='users'),

]

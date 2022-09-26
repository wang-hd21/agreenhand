from django.contrib import admin
from django.urls import path
 
from backend import views
 
urlpatterns = [
    path('index/',views.index),
]
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('logout',views.logout),
    path('upload',views.upload),
    path('studymaterial',views.studymaterial),
    path('profile',views.profile),
    path('delete/<int:id>',views.delete),
]

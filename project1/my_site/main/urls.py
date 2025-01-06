from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index),
    path('page', views.page),
    path('page1', views.page1),
    path('page2', views.page2),
    path('', views.index)
]
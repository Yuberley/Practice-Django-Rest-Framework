from nturl2path import url2pathname
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
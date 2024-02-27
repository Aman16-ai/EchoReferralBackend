from django.contrib import admin
from django.urls import path,include
from .views import *
from .router import router

urlpatterns = [
    path('getUserDetails/',getUserDetails),
    path('',include(router.urls)),
]

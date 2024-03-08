from django.contrib import admin
from django.urls import path, include
from .views import testApi
from .routers import router
urlpatterns = [
    path('test/',testApi),
    path('',include(router.urls)),
]

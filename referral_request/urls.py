from django.contrib import admin
from django.urls import path, include
from .routers import router
from .views import test
urlpatterns = [
    path("test/",test),
    path("",include(router.urls)),
]

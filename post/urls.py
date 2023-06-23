from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PostView


router = routers.DefaultRouter()
router.register(r'review', PostView, 'post')


urlpatterns = [
    path('', include(router.urls)),
]

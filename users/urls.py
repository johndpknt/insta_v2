from django.urls import re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import  include

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)), 
    ]

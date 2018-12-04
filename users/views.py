# Create your views here.
from django.shortcuts import render
from users.serializers import UserSerializer
from users.models import Users
#from rest_framework import generics, filters, status
from rest_framework import viewsets
from rest_framework.decorators import list_route


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

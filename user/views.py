from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from.serializer import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    

# Create your views here.

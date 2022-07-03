from django.shortcuts import render
from django.contrib.auth.models import User
from links.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
# Create your views here.

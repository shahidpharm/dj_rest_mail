from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):

    # queryset = User.objects.all().order_by('-university_batch')
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

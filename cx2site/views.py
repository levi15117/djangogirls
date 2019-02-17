# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import c2
from .serializers import c2Serializer

from django.shortcuts import render

# Create your views here.
class c2List(generics.ListCreateAPIView):

    queryset = c2.objects.all()
    serializer_class = c2Serializer

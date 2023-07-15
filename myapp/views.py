from django.shortcuts import render
from myapp.models import *
from rest_framework import viewsets, generics
from myapp.serializers import RegionSerializer, DistrictSerializer, PostSerializers
from rest_framework import serializers


class Region(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer





class District(generics.ListAPIView):
    queryset = District.objects.all()   
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return self.queryset.filter(
            region_id__pk=self.kwargs['pk']
        )





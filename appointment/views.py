from django.shortcuts import render,redirect
from django.contrib import messages,auth
import re
# from .models import 
from django.http import HttpResponse,FileResponse,Http404,HttpResponseRedirect,JsonResponse
import random
# from Appointment_Booking.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PreacherSerializer,LocationSerializer,TopicSerializer,AppointmentSerializer
from .models import Preacher,Location,Topic,Appointment
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def ping(request):  
    return HttpResponse("<h2>Hello, Welcome to Appointment Booking System!</h2>")  

class PreacherViews(APIView):
    def post(self, request):
        serializer = PreacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request,id=None):
        if id:
            queryset = Preacher.objects.filter(id=id)
            print(queryset)
            serializer = PreacherSerializer(data=queryset,many=True)
            serializer.is_valid()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = Preacher.objects.all()
        serializer = PreacherSerializer(data=queryset,many=True)
        serializer.is_valid()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def delete(self, request,id=None):
        if id:
            queryset=get_object_or_404(Preacher, id=id)
            # queryset = Preacher.objects.get(id=id)
            queryset.delete()
            return Response({"status": "success", "data": "Item Deleted"},status=status.HTTP_200_OK)
        else:
            return Response({"status": "failure", "data": "Id missing"},status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,id=None):
        if id:
            queryset = Preacher.objects.get(id=id)
            serializer = PreacherSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)



class LocationViews(APIView):
    def get(self, request,id=None):
        if id:
            queryset = Location.objects.get(id=id)
            serializer = LocationSerializer(queryset)
            serializer.is_valid()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = Location.objects.all()
        serializer = LocationSerializer(data=queryset,many=True)
        serializer.is_valid()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class TopicViews(APIView):
    def get(self, request,id=None):
        if id:
            queryset = Topic.objects.get(id=id)
            serializer = TopicSerializer(queryset)
            serializer.is_valid()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = Topic.objects.all()
        serializer = TopicSerializer(data=queryset,many=True)
        serializer.is_valid()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class AppointmentViews(APIView):
    def post(self, request):
        data=request.data
        print(data)
        scheduleId=data["ScheduleId"]
        date=data["Date"]
        month=data["Month"]
        preacherId=data["PreacherId"]
        topicId=data["TopicId"]
        locationId=data["LocationId"]
        serializer = PreacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request,id=None):
        if id:
            queryset = Preacher.objects.get(id=id)
            serializer = PreacherSerializer(queryset)
            serializer.is_valid()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = Preacher.objects.all()
        serializer = PreacherSerializer(data=queryset,many=True)
        serializer.is_valid()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

# def registerPreacher(request):
#     if request.method=='POST':
# 		email=request.POST['email']
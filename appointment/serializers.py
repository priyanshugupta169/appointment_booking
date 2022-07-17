from rest_framework import serializers
from .models import Preacher, Location, Topic, Appointment
from datetime import date

class PreacherSerializer(serializers.ModelSerializer):
    id=serializers.CharField(max_length=20,required=False)
    email=serializers.EmailField(max_length=100,required=False)
    name=serializers.CharField(max_length=100)
    availability_dates=serializers.JSONField(required=False)
    contact_info=serializers.CharField(max_length=70,required=False)
    type=serializers.JSONField(required=False)
    # type=models.CharField(max_length=70,choices=TYPE)
    creation_date = serializers.DateField(default=date.today)

    class Meta:
        model = Preacher
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
    id=serializers.CharField(max_length=20)
    name=serializers.CharField(max_length=100)
    creation_date = serializers.DateField(default=date.today)

    class Meta:
        model = Location
        fields = ('__all__')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('__all__')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')
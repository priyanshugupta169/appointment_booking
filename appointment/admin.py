from django.contrib import admin
from .models import Preacher,Location,Topic,Appointment
# Register your models here.
admin.site.register(Preacher)
admin.site.register(Location)
admin.site.register(Topic)
admin.site.register(Appointment)
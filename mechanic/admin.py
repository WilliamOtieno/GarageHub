from django.contrib import admin
from .models import Appointment

# Register your models here.


class MechanicAdmin(admin.ModelAdmin):
    list_display = ["date", "time_start", "time_end", "appointment_with"]
    list_filter = ('date', 'update_time')

admin.site.register(Appointment, MechanicAdmin)
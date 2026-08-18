from django.contrib import admin
from .models import Service, Appointment

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'appointment_date', 'appointment_time', 'service', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('customer_name', 'phone', 'email')
    ordering = ('appointment_date',)
    list_editable = ('status',) # To confirm or change booking status
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=20)
    special_request = models.TextField(null=True, blank=True)

    # Booking Status Logic
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} | {self.appointment_date} | {self.service.name}  | {self.status}"
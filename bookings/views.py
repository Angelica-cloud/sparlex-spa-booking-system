# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
from .models import Appointment
from .models import Service
from datetime import datetime
from datetime import date


def home(request):
    return render(request, 'spa/index.html')

# Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def appointment(request):

    services = Service.objects.all()

    if request.method == "POST":

        service_id = request.POST.get("service")
        customer_name = request.POST.get("customer_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        special_request = request.POST.get("special_request")

        service = Service.objects.get(id=service_id)

        # Check for duplicate booking
        existing_booking = Appointment.objects.filter(
            user=request.user,
            service=service,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()

        if existing_booking:
            messages.error(
                request,
                "You already have a booking for this service at that date and time."
            )
            return redirect("appointment")

        # Save booking
        Appointment.objects.create(
            user=request.user,
            service=service,
            customer_name=customer_name,
            phone=phone,
            email=email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            special_request=special_request,
        )

        messages.success(request, "Booking successful!")
        return redirect("home")

    return render(
        request,
        "spa/appointment.html",
        {
            "services": services
        }
    )

# Cancel Appointment
@login_required
def cancel_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        user=request.user
    )

    if request.method == "POST" and appointment.status == "Pending":
        appointment.status = "Cancelled"
        appointment.save()

    messages.success(request, "Appointment cancelled successfully.")

    return redirect("my_appointments")

def signup(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        auth_login(request, user)

        messages.success(request, "Account created successfully!")

        return redirect("home")

    return render(request, "spa/signup.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect("home")

        messages.error(request, "Invalid username or password.")
        return redirect("login")

    return render(request, "spa/login.html")


@login_required(login_url="login")
def my_appointments(request):

    appointments = Appointment.objects.filter(
        user=request.user
    ).order_by("-appointment_date", "-created_at")

    context = {
        "appointments": appointments
    }

    return render(request, "spa/my_appointments.html", context)

def contact(request):
    return render(request, 'spa/contact.html')

def about(request):
    return render(request, 'spa/about.html')

def gallery(request):
    return render(request, 'spa/gallery.html')

def open(request):
    return render(request, 'spa/open.html')

def price(request):
    return render(request, 'spa/price.html')

def service(request):
    return render(request, 'spa/service.html')

def team(request):
    return render(request, 'spa/team.html')

def testimonial(request):
    return render(request, 'spa/testimonial.html')


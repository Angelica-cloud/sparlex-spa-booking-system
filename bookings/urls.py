from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path("cancel-appointment/<int:appointment_id>/", views.cancel_appointment, name="cancel_appointment",),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]
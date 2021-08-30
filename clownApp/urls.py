from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('client/', views.client, name='dashboard-client'),
    path('appointment/', views.appointment, name='dashboard-appointment'),
    path('appointment/delete/<int:pk>/', views.appointment_delete, name='dashboard-appointment-delete'),
    path('appointment/update/<int:pk>/', views.appointment_delete, name='dashboard-appointment-update'),
    path('clown/', views.clown, name='dashboard-clown'),
]
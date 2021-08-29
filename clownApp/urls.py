from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('client/', views.client, name='dashboard-client'),
    path('appointment/', views.appointment, name='dashboard-appointment'),
    path('clown/', views.clown, name='dashboard-clown'),
]
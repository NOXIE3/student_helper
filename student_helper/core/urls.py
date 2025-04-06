from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/', views.custom_login, name='login'),
  path('home/', views.home, name='home'),
path('register/', views.register, name='register'), 
    path('create-task/', views.create_task, name='create_task'),
    path('help/', views.help_view, name='help'),
    path('calendar/', views.calendar_view, name='calendar'),
     path('wellness-checkin/', views.wellness_checkin, name='wellness_checkin'),
       path('notifications/', views.notifications, name='notifications'),
]

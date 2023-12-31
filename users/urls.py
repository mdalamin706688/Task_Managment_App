from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='login'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Define the login URL pattern
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

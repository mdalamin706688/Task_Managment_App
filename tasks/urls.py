from django.urls import path
from . import views
from users.views import edit_profile  # Import the edit_profile view




urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    # URL pattern for editing a task
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    # URL pattern for deleting a task
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/', views.custom_logout, name='logout'),


]

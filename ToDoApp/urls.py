from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     # Include tasks app's URLs as the root URL
    path('', include('users.urls')),
     path('', include('tasks.urls')),
]

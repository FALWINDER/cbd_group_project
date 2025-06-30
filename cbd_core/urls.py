from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),
    path('', include('learning_platform.urls')),
   

    # Redirect root URL to login page
    path('', lambda request: redirect('login')),  # <-- This line fixes the 404 at /
]

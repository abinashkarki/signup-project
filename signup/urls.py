from django.contrib import admin
from django.urls import path
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.register, name='register'),
    path('home/', user_views.home, name='home'),
]

from django.contrib import admin
from django.urls import path
from .views import home
from .views import daftar_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('customer/daftar/', daftar_customer, name='daftar_customer'),
]

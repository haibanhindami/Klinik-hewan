from django.contrib import admin
from django.urls import path, include
from .views import home
from .views import daftar_customer
from .models import JadwalPemeriksaan, Pemeriksaan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('customer/daftar/', daftar_customer, name='daftar_customer'),
    path('fasilitas/', include('fasilitas.urls')),
    admin.site.register(JadwalPemeriksaan),
    admin.site.register(Pemeriksaan),
]
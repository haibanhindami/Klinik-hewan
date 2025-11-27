from django.contrib import admin
from django.urls import path, include
from .views import home
from .views import daftar_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('customer/daftar/', daftar_customer, name='daftar_customer'),
    path('fasilitas/', include('fasilitas.urls')),
    path('pemeriksaan/', include('pemeriksaan.urls')),
    path('pegawai/', include('pegawai.urls')),
    path('pembayaran/', include('pembayaran.urls')),
    path('dashboard/', include('dashboard.urls')),
]

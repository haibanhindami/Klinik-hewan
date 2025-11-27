from django.contrib import admin

# Register your models here.
from .models import JadwalPemeriksaan, Pemeriksaan

admin.site.register(JadwalPemeriksaan)
admin.site.register(Pemeriksaan)
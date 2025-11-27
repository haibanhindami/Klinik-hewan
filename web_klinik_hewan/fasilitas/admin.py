from django.contrib import admin

# Register your models here.
from .models import Obat, Perawatan, Penginapan, InfoFasilitas

admin.site.register(Obat)
admin.site.register(Perawatan)
admin.site.register(Penginapan)
admin.site.register(InfoFasilitas)
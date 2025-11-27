from django.shortcuts import render

# Create your views here.
from .models import Obat, Perawatan, Penginapan, InfoFasilitas

def obat_list(request):
    obats = Obat.objects.all()
    return render(request, 'fasilitas/obat_list.html', {'obats': obats})

def perawatan_list(request):
    perawatans = Perawatan.objects.all()
    return render(request, 'fasilitas/perawatan_list.html', {'perawatans': perawatans})

def penginapan_list(request):
    penginapans = Penginapan.objects.all()
    return render(request, 'fasilitas/penginapan_list.html', {'penginapans': penginapans})

def info_list(request):
    infos = InfoFasilitas.objects.all()
    return render(request, 'fasilitas/info_list.html', {'infos': infos})
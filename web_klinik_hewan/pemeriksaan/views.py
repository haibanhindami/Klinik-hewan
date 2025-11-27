from django.http import HttpResponse

def index(request):
    return HttpResponse("Halo ini halaman pemeriksaan!")

from django.shortcuts import render, redirect
from .forms import CustomerForm

def daftar_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # setelah daftar kembali ke dashboard
    else:
        form = CustomerForm()

    return render(request, "customer/daftar.html", {"form": form})

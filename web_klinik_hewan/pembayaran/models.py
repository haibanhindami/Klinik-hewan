from django.db import models
from pemeriksaan.models import Pemeriksaan

class Pembayaran(models.Model):
    pemeriksaan = models.OneToOneField(Pemeriksaan, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    metode = models.CharField(max_length=50, default="Cash")
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pembayaran #{self.id} - {self.pemeriksaan.customer.nama}"

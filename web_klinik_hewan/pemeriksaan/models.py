from django.db import models
from customer.models import Customer
from pegawai.models import Pegawai
from fasilitas.models import Fasilitas

class Pemeriksaan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hewan = models.CharField(max_length=50)
    keluhan = models.TextField()
    diagnosa = models.TextField()
    dokter = models.ForeignKey(Pegawai, limit_choices_to={'jabatan': 'dokter'}, on_delete=models.CASCADE)
    tindakan = models.ManyToManyField(Fasilitas)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pemeriksaan {self.customer.nama} - {self.hewan}"

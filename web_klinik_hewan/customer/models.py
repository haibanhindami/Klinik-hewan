from django.db import models

class Customer(models.Model):
    nama_pemilik = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()

    # data hewan
    nama_hewan = models.CharField(max_length=100)
    jenis_hewan = models.CharField(max_length=50)
    ras_hewan = models.CharField(max_length=50, blank=True, null=True)
    umur = models.CharField(max_length=20)

    # waktu daftar
    tanggal_daftar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_pemilik} - {self.nama_hewan}"

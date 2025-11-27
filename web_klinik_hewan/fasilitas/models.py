from django.db import models

class Fasilitas(models.Model):
    KATEGORI = (
        ('obat', 'Obat'),
        ('perawatan', 'Perawatan'),
        ('penginapan', 'Rawat Inap'),
        ('info', 'Informasi'),
    )
    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=20, choices=KATEGORI)
    harga = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama

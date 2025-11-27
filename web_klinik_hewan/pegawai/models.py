from django.db import models

class Pegawai(models.Model):
    JABATAN_CHOICES = (
        ('dokter', 'Dokter'),
        ('perawat', 'Perawat'),
        ('resepsionis', 'Resepsionis'),
        ('cleaning', 'Cleaning Service'),
    )
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=15, choices=JABATAN_CHOICES)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nama} ({self.jabatan})"

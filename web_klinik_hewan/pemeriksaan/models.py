from django.db import models

# Create your models here.
class JadwalPemeriksaan(models.Model):
    nama_pasien = models.CharField(max_length=100)
    nama_dokter = models.CharField(max_length=100)
    tanggal = models.DateField()
    waktu = models.TimeField()
    keluhan = models.TextField()

    def __str__(self):
        return f"{self.nama_pasien} - {self.tanggal}"

class Pemeriksaan(models.Model):
    jadwal = models.ForeignKey(JadwalPemeriksaan, on_delete=models.CASCADE)
    diagnosa = models.TextField()
    tindakan = models.TextField()
    resep_obat = models.TextField(blank=True, null=True)
    catatan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pemeriksaan {self.jadwal.nama_pasien}"
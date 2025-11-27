from django.db import models

# Create your models here.
class Obat(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    stok = models.PositiveIntegerField(default=0)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama


class Perawatan(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    durasi = models.PositiveIntegerField(help_text="Durasi (menit)")
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama


class Penginapan(models.Model):
    nama_hewan = models.CharField(max_length=200)
    jenis_hewan = models.CharField(max_length=100)
    tanggal_masuk = models.DateField()
    tanggal_keluar = models.DateField(blank=True, null=True)
    harga_per_hari = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nama_hewan} - {self.jenis_hewan}"


class InfoFasilitas(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
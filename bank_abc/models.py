from tkinter import CASCADE
from django.db import models

# Create your models here.
class Nasabah(models.Model):
    id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=45)
    tempat_lahir = models.CharField(max_length=45)
    tanggal_lahir = models.DateField()
    GENDER = (
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan'),
    )
    jenis_kelamin = models.CharField(max_length=10, choices=GENDER, default=None)
    alamat = models.TextField()
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    
    class Meta:
        db_table = "nasabah"

    def __str__(self):
        return self.nama


class Cabangbank(models.Model):
    kode = models.IntegerField()
    kode = models.AutoField(primary_key=True)
    nama_cabang = models.CharField(max_length=50)
    alamat_cabang = models.TextField()

    class Meta:
        db_table = "cabang"

    def __str__(self):
        return self.nama_cabang

class Rekening(models.Model):
    no_rekening = models.CharField(max_length=10, primary_key=True)
    saldo = models.IntegerField()
    id_nasabah = models.ForeignKey(Nasabah, on_delete=models.CASCADE, related_name='bank_abc_rekening_bank_abc_nasabah')
    kode_cabang = models.ForeignKey(Cabangbank, on_delete=models.CASCADE, related_name='bank_abc_cabangbank')

    class Meta:
        db_table = "rekening"

    def __str__(self):
        return self.no_rekening

class Transaksi(models.Model):
    no_transaksi = models.IntegerField()
    no_transaksi = models.AutoField(primary_key=True)
    id_nasabah = models.ForeignKey(Nasabah, on_delete=models.CASCADE, related_name='bank_abc_nasabah')
    tujuan = models.IntegerField()
    no_rekening = models.ForeignKey(Rekening, on_delete=models.CASCADE, related_name='bank_abc_rekening')
    tanggal = models.DateField(auto_now_add=True)
    jumlah = models.IntegerField()
   
    class Meta:
        db_table = "transaksi"

    def __str__(self):
       return self.jenis_transaksi
from django.contrib import admin
from .models import Nasabah
from .models import Cabangbank
from .models import Rekening
from .models import Transaksi

# Register your models here.
admin.site.register(Nasabah)
admin.site.register(Cabangbank)
admin.site.register(Rekening)
admin.site.register(Transaksi)
#@admin.register(Nasabah)
#class NasabahAdmin(admin.ModelAdmin):
#    list_display = ('id', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'username', 'password')
    #list_filter = ('id', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'alamat')

#@admin.register(Cabangbank)
#class NasabahAdmin(admin.ModelAdmin):
#    list_display = ('kode_cabang', 'nama_cabang', 'alamat_cabang')
    #list_filter = ('kode_cabang', 'nama_cabang', 'alamat_cabang')

#@admin.register(Rekening)
#class NasabahAdmin(admin.ModelAdmin):
#    list_display = ('no_rekening', 'pin', 'saldo', 'id_nasabah', 'kode_cabang')
    #list_filter = ('no_rekening', 'id_nasabah', 'kode_cabang')

#@admin.register(Transaksi)
#class NasabahAdmin(admin.ModelAdmin):
#    list_display = ('no_transaksi', 'id_nasabah', 'no_rekening', 'jenis_transaksi', 'tanggal', 'jumlah')
    #list_filter = ('no_transaksi', 'jenis_transaksi', 'tanggal')
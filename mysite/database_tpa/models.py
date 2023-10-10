from django.db import models

class Jadwal(models.Model):
    hari_mengajar = models.CharField(max_length=30, blank=True, null=True)

class Guru(models.Model):
    nama_guru = models.CharField(max_length=30, blank=True, null=True)
    jadwal_mengajar = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)

class Siswa(models.Model):
    nama_lengkap = models.CharField(max_length=50, blank=True,null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)
    nama_orang_tua = models.CharField(max_length=50, blank=True,null=True)
    kontak = models.CharField(max_length=30, blank=True,null=True)
    alamat = models.TextField(blank=True, null=True)
    guru = models.ForeignKey(Guru, null=True, blank=True, on_delete=models.SET_NULL)





from django.db import models

class Siswa(models.Model):
    nama_lengkap = models.CharField(max_length=50, blank=True,null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)


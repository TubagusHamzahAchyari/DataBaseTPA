from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Jadwal(models.Model):
    jadwal = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.jadwal

    class Meta:
        verbose_name_plural = 'Jadwal'

class Guru(models.Model):
    nama_guru = models.CharField(max_length=30, blank=True, null=True)
    jadwal_mengajar = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama_guru

    class Meta:
        verbose_name_plural = 'Guru'

class SiswaPDB(models.Model):
    nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)
    nama_wali = models.CharField(max_length=50, blank=True, null=True)
    kontak = models.CharField(max_length=30, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jadwal_mengaji = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name_plural = 'Siswa PDB'


class Siswa(models.Model):
    nama_lengkap = models.CharField(max_length=50, blank=True,null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)
    nama_wali = models.CharField(max_length=50, blank=True,null=True)
    kontak = models.CharField(max_length=30, blank=True,null=True)
    alamat = models.TextField(blank=True, null=True)
    guru = models.ForeignKey(Guru, null=True, blank=True, on_delete=models.SET_NULL)
    jadwal_mengaji = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)
    siswa_pdb = models.ForeignKey(SiswaPDB, null=True, blank=True, on_delete=models.SET)


    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name_plural = 'Siswa'

@receiver(pre_save, sender=Siswa)
def sync_siswa_pdb(sender, instance, **kwargs):
    # Logika sinkronisasi
    if instance.siswa_pdb:
        instance.nama_lengkap = instance.siswa_pdb.nama_lengkap
        instance.nama_panggilan = instance.siswa_pdb.nama_panggilan
        instance.nama_wali = instance.siswa_pdb.nama_wali
        instance.kontak = instance.siswa_pdb.kontak
        instance.alamat = instance.siswa_pdb.alamat
        instance.jadwal_mengaji = instance.siswa_pdb.jadwal_mengaji

pre_save.connect(sync_siswa_pdb, sender=Siswa)

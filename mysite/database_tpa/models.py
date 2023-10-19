from django.db import models

class Jadwal(models.Model):
    jadwal = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.jadwal

    class Meta:
        verbose_name_plural = 'Jadwal'

    def siswa_count(self):
        return self.siswa_set.count()

class Keuangan(models.Model):
    status_keuangan = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.status_keuangan

    class Meta:
        verbose_name_plural = 'Keuangan'

class Guru(models.Model):
    nama_guru = models.CharField(max_length=30, blank=True, null=True)
    jadwal_mengajar = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama_guru

    class Meta:
        verbose_name_plural = 'Guru'

    def siswa_count(self):
        return self.siswa_set.count()

class SiswaPDB(models.Model):
    CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    )
    nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)
    nama_wali = models.CharField(max_length=50, blank=True, null=True)
    kontak = models.CharField(max_length=30, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES)
    jadwal_mengaji = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name_plural = 'Siswa PDB'


from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Siswa(models.Model):
    CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    )
    JILID_CHOICES = (
        ('Pra', 'Pra'),
        ('Jilid 1', 'Jilid 1'),
        ('Jilid 2', 'Jilid 2'),
        ('Jilid 3', 'Jilid 3'),
        ('Jilid 4', 'Jilid 4'),
        ('Jilid 5', 'Jilid 5'),
        ('Jilid 6', 'Jilid 6'),
        ('Al-Quran', 'Al-Quran'),
        ('Tahfidz', 'Tahfidz'),
        ('Private', 'Private'),
    )
    nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
    nama_panggilan = models.CharField(max_length=20, blank=True, null=True)
    nama_wali = models.CharField(max_length=50, blank=True, null=True)
    kontak = models.CharField(max_length=30, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    guru = models.ForeignKey(Guru, null=True, blank=True, on_delete=models.SET_NULL)
    jadwal_mengaji = models.ForeignKey(Jadwal, blank=True, null=True, on_delete=models.SET_NULL)
    spp = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=0)
    jenis_kelamin = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES)
    keuangan = models.ForeignKey(Keuangan, blank=True, null=True, on_delete=models.SET_NULL)
    jilid_umi = models.CharField(blank=True, null=True, max_length=30, choices=JILID_CHOICES)
    siswa_pdb = models.ForeignKey(SiswaPDB, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if self.jadwal_mengaji_id == 1 or self.jadwal_mengaji_id == 2:
            self.spp = 150000
        elif self.jadwal_mengaji_id == 3:
            self.spp = 300000
        elif self.jadwal_mengaji_id == 4:
            self.spp = 1000000

        super(Siswa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name_plural = 'Siswa'

@receiver(pre_save, sender=Siswa)
def sync_siswa_pdb(sender, instance, **kwargs):
    if instance.siswa_pdb:
        instance.nama_lengkap = instance.siswa_pdb.nama_lengkap
        instance.nama_panggilan = instance.siswa_pdb.nama_panggilan
        instance.nama_wali = instance.siswa_pdb.nama_wali
        instance.kontak = instance.siswa_pdb.kontak
        instance.alamat = instance.siswa_pdb.alamat
        instance.jadwal_mengaji = instance.siswa_pdb.jadwal_mengaji
        instance.jenis_kelamin = instance.siswa_pdb.jenis_kelamin

pre_save.connect(sync_siswa_pdb, sender=Siswa)


from django.contrib import admin
from .models import *

class SiswaInLineJadwal(admin.TabularInline):
    model = Siswa
    extra = 0
    # fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji',)
    fields = ('nama_lengkap', 'nama_panggilan','guru', 'jadwal_mengaji',)
    readonly_fields = fields
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('jadwal',)
    inlines = [SiswaInLineJadwal]

class SiswaInLineKeuangan(admin.TabularInline):
    model = Siswa
    extra = 0
    fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji',)
    readonly_fields = fields

class KeuanganAdmin(admin.ModelAdmin):
    list_display =  ('status_keuangan',)
    inlines = [SiswaInLineKeuangan]

class SiswaInLineGuru(admin.TabularInline):
    model = Siswa
    extra = 0
    fields = ('nama_lengkap', 'nama_panggilan','guru', 'jadwal_mengaji',)
    # fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'guru', 'jadwal_mengaji',)
    readonly_fields = fields

class GuruAdmin(admin.ModelAdmin):
    list_display = ('nama_guru','jadwal_mengajar',)
    inlines = [SiswaInLineJadwal]

class SiswaPDBAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'jadwal_mengaji',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)

class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji',)
    raw_id_fields = ('siswa_pdb',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)


admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(Keuangan, KeuanganAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(SiswaPDB, SiswaPDBAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.site_header = 'Database TPA Al-Qalam'
admin.site.site_title = 'Ahlan Wa Sahlan-Selamat Datang di Database TPA Al-Qalam'
admin.site.index_title = 'Ahlan Wa Sahlan-Selamat Datang di Dashboard Database TPA Al-Qalam'
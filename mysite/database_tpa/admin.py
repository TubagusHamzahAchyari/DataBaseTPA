from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

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
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'guru', 'jadwal_mengaji', 'keuangan')
    raw_id_fields = ('siswa_pdb',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)
    list_display = ('nama_lengkap',)

    def get_list_display(self, request):
        user_exists = request.user.username == 'gurutpa'

        if user_exists:
            self.list_display_links = None
            return ('nama_lengkap', 'nama_panggilan', 'guru', 'jadwal_mengaji')
        else:
            return ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'guru', 'jadwal_mengaji', 'keuangan')



# user_exists = request.user.username == 'gurutpa'
#
# # Mendaftarkan model Siswa dengan admin yang sesuai
# if user_exists:
#     class SiswaAdmin(admin.ModelAdmin):
#         list_display = ('nama_lengkap', 'nama_panggilan','guru', 'jadwal_mengaji')
#         search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)
#         list_display_links = None  # Tidak ada kolom yang dapat di-klik
# else:
#     class SiswaAdmin(admin.ModelAdmin):
#         list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji','keuangan')
#         raw_id_fields = ('siswa_pdb',)
#         search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)


# class SiswaAdmin(admin.ModelAdmin):
#     list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji','keuangan')
#     raw_id_fields = ('siswa_pdb',)
#     search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)

# class SiswaAdminGuru(admin.ModelAdmin):
#     list_display = ('nama_lengkap', 'nama_panggilan','guru', 'jadwal_mengaji')
#     search_fields = ('nama_lengkap', 'nama_panggilan',)


admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(Keuangan, KeuanganAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(SiswaPDB, SiswaPDBAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.site_header = 'Database TPA Al-Qalam'
admin.site.site_title = 'Ahlan Wa Sahlan-Selamat Datang di Database TPA Al-Qalam'
admin.site.index_title = 'Ahlan Wa Sahlan-Selamat Datang di Dashboard Database TPA Al-Qalam'

# from django.contrib.auth.models import User
#
# user_exists = User.objects.filter(username='gurutpa').exists()
#
# # Set variabel gurutpa berdasarkan hasil pencarian
# gurutpa = user_exists
#
# # Mendaftarkan model Siswa dengan admin yang sesuai
# if gurutpa:
#     admin.site.register(Siswa, SiswaAdminGuru)
# else:
#     admin.site.register(Siswa, SiswaAdmin)






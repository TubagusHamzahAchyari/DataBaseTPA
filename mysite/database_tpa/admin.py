
from django.contrib import admin
from .models import *
import babel.numbers

class SiswaInLineJadwal(admin.TabularInline):
    model = Siswa
    extra = 0
    # fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','guru', 'jadwal_mengaji',)
    fields = ('nama_lengkap', 'nama_panggilan','guru', 'jadwal_mengaji',)
    readonly_fields = fields
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('jadwal','siswa_count',)
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
    list_display = ('nama_guru','jadwal_mengajar','siswa_count',)
    inlines = [SiswaInLineJadwal]

class SiswaPDBAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'jadwal_mengaji',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat',)


class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak',
                    'alamat', 'guru', 'jadwal_mengaji', 'babel_spp','jenis_kelamin', 'keuangan','jilid_umi')
    raw_id_fields = ('siswa_pdb',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','keuangan__status_keuangan','jilid_umi','jenis_kelamin','jadwal_mengaji__jadwal','guru__nama_guru','spp')
    actions = ['save_all_selected','keuangan_satu','keuangan_dua','keuangan_tiga']

    def babel_spp(self, obj):
        return babel.numbers.format_currency(obj.spp, 'IDR', locale='id_ID')
    babel_spp.short_description = 'SPP'
    def save_all_selected(modeladmin, request, queryset):
        for obj in queryset:
            obj.save()

    save_all_selected.short_description = "Update Data"
    def keuangan_satu(self, request, queryset):
        queryset.update(keuangan=1)

    keuangan_satu.short_description = "Belum ditagih"
    def keuangan_dua(self, request, queryset):
        queryset.update(keuangan=2)

    keuangan_dua.short_description = "Sudah ditagih"

    def keuangan_tiga(self, request, queryset):
        queryset.update(keuangan=3)

    keuangan_tiga.short_description = "Sudah bayar"

    def get_list_display(self, request):
        user_exists = request.user.username == 'gurutpa'

        if user_exists:
            self.list_display_links = None
            return ('nama_lengkap', 'nama_panggilan', 'guru', 'jadwal_mengaji')
        else:
            return ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak',
                    'alamat', 'guru', 'jadwal_mengaji', 'babel_spp','jenis_kelamin', 'keuangan','jilid_umi')



admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(Keuangan, KeuanganAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(SiswaPDB, SiswaPDBAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.site_header = 'Database TPA Al-Qalam'
admin.site.site_title = 'Ahlan Wa Sahlan di Database TPA Al-Qalam'
admin.site.index_title = 'Ahlan Wa Sahlan di Dashboard Database TPA Al-Qalam'







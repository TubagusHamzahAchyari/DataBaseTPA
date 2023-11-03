import decimal
import textwrap
from reportlab.lib import colors
from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from .models import *
import babel.numbers
from babel.numbers import format_currency

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
    list_display =  ('status_keuangan','siswa_count')
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
    list_display = ('status_pendaftaran','nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'jadwal_mengaji')
    search_fields = ('status_pendaftaran','nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat', 'jadwal_mengaji__jadwal')
    actions = ['save_all_selected']

    def save_all_selected(modeladmin, request, queryset):
        for obj in queryset:
            obj.save()

    save_all_selected.short_description = "Update Data"

class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak',
                    'alamat', 'guru', 'jadwal_mengaji', 'babel_spp','jenis_kelamin', 'keuangan','jilid_umi')
    raw_id_fields = ('siswa_pdb',)
    search_fields = ('nama_lengkap', 'nama_panggilan', 'nama_wali', 'kontak', 'alamat','keuangan__status_keuangan','jilid_umi','jenis_kelamin','jadwal_mengaji__jadwal','guru__nama_guru','spp')
    actions = ['save_all_selected','keuangan_satu','keuangan_dua','keuangan_tiga','cetak_pdf']

    def babel_spp(self, obj):
        if obj.spp is not None:
            try:
                return babel.numbers.format_currency(obj.spp, 'IDR', locale='id_ID')
            except (ValueError, decimal.InvalidOperation):
                return 'Invalid SPP Value'
        else:
            return 'Perlu Update Data'

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

    def cetak_pdf(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="siswa.pdf"'

        # Data yang akan dicetak ke PDF
        data = []
        total_spp = 0
        for index, obj in enumerate(queryset, start=1):
            data.append([index,
                         obj.nama_lengkap,
                         obj.nama_panggilan,
                         obj.nama_wali,
                         obj.kontak,
                         obj.alamat,
                         obj.guru,
                         obj.jadwal_mengaji,
                         format_currency(obj.spp, 'IDR', locale='id_ID'),
                         obj.jenis_kelamin,
                         obj.keuangan,
                         obj.jilid_umi
                         ])
            total_spp += obj.spp

        # Buat dokumen PDF
        doc = SimpleDocTemplate(response, pagesize=landscape(letter))
        elements = []

        # Judul Data Siswa
        styles = getSampleStyleSheet()
        title = Paragraph("<b>Data Siswa</b>", styles['Title'])
        elements.append(title)

        # Tabel untuk data siswa
        table_data = [['No', 'Nama', 'Panggilan', 'Nama Wali', 'Kontak', 'Alamat','Guru', 'Jadwal', 'SPP', 'Jenis Kelamin', 'Keuangan', 'Jilid Umi']] \
                     + data
        col_widths = [20, 80, 70, 70, 70, 70, 70, 70, 50, 70, 70, 50]  # Misalnya, ini adalah lebar kolom untuk setiap kolom

        table = Table(table_data, colWidths=col_widths, repeatRows=1)

        # Tambahkan parameter wordwrap pada TableStyle
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Mengubah warna latar belakang header menjadi putih
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('TOPPADDING', (0, 0), (-1, 0), 2.5),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            # Ini mengatur ukuran font untuk sel dalam baris kedua (indeks 1) ke bawah menjadi 9.
            ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Mengubah warna latar belakang sel lainnya menjadi putih
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 7),
            # Ini mengatur ukuran font untuk sel dalam baris kedua (indeks 1) ke bawah menjadi 5.
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        # Tambahkan total di bawah tabel
        total_style = getSampleStyleSheet()
        total_style = total_style['Normal']
        total_style.alignment = 1  # Pusatkan teks
        total_paragraph = Paragraph(f"Total SPP: {format_currency(total_spp, 'IDR', locale='id_ID')}", total_style)
        elements.append(total_paragraph)

        # Bangun dokumen PDF
        doc.build(elements)
        return response

    cetak_pdf.short_description = "Cetak PDF"



admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(Keuangan, KeuanganAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(SiswaPDB, SiswaPDBAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.site_header = 'Database TPA Al-Qalam'
admin.site.site_title = 'Ahlan Wa Sahlan di Database TPA Al-Qalam'
admin.site.index_title = 'Ahlan Wa Sahlan di Dashboard Database TPA Al-Qalam'







# Generated by Django 4.2.6 on 2023-10-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_tpa', '0008_alter_siswa_jilid_umi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='jilid_umi',
            field=models.CharField(blank=True, choices=[('Pra', 'Pra'), ('Jilid 1', 'Jilid 1'), ('Jilid 2', 'Jilid 2'), ('Jilid 3', 'Jilid 3'), ('Jilid 4', 'Jilid 4'), ('Jilid 5', 'Jilid 5'), ('Jilid 6', 'Jilid 6'), ('Al-Quran', 'Al-Quran'), ('Tahfidz', 'Tahfidz'), ('Private', 'Private')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='spp',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True),
        ),
    ]

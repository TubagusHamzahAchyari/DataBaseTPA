# Generated by Django 4.2.6 on 2023-10-12 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_tpa', '0002_jadwal_alter_siswa_options_siswa_alamat_siswa_kontak_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keuangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_keuangan', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Keuangan',
            },
        ),
        migrations.AddField(
            model_name='siswapdb',
            name='keuangan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database_tpa.keuangan'),
        ),
    ]
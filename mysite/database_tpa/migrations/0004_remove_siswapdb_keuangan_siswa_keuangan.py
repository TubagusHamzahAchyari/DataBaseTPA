# Generated by Django 4.2.6 on 2023-10-12 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_tpa', '0003_keuangan_siswapdb_keuangan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siswapdb',
            name='keuangan',
        ),
        migrations.AddField(
            model_name='siswa',
            name='keuangan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database_tpa.keuangan'),
        ),
    ]
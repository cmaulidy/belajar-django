# Generated by Django 2.2.6 on 2019-12-13 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0003_kategori_kecamatan_kedinasan'),
    ]

    operations = [
        migrations.AddField(
            model_name='informasitambahanuser',
            name='kecamatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='masterdata.Kecamatan'),
        ),
        migrations.AddField(
            model_name='informasitambahanuser',
            name='kedinasan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pegawai', to='masterdata.Kedinasan'),
        ),
    ]
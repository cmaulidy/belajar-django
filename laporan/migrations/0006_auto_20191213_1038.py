# Generated by Django 2.2.6 on 2019-12-13 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0005_auto_20191213_1032'),
        ('laporan', '0005_auto_20191212_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='kecamatan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='laporan', to='masterdata.Kecamatan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laporan',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laporan', to='masterdata.Kategori'),
        ),
    ]

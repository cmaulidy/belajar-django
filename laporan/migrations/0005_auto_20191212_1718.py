# Generated by Django 2.2.6 on 2019-12-12 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0004_komentar_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan',
            name='pelapor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laporan', to=settings.AUTH_USER_MODEL),
        ),
    ]
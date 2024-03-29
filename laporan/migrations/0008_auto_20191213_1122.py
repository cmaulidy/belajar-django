# Generated by Django 2.2.6 on 2019-12-13 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laporan', '0007_remove_laporan_daerah'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='komentar',
            field=models.TextField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='komentar',
            name='laporan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='laporan.Laporan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='komentar',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='laporan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='laporan.Laporan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vote', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='vote',
            field=models.BooleanField(choices=[(1, 'Setuju'), (0, 'Tidak Setuju')], default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformasiTambahanUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(blank=True, max_length=20, null=True)),
                ('telepon', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]

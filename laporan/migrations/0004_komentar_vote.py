# Generated by Django 2.2.6 on 2019-12-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0003_auto_20191212_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

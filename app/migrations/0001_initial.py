# Generated by Django 4.1.7 on 2024-12-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('mualif', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
                ('asar', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='books/')),
            ],
        ),
        migrations.CreateModel(
            name='KopSotilganKitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('mualif', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
                ('asar', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='books/')),
            ],
        ),
        migrations.CreateModel(
            name='kun_iqtibos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
        ),
    ]

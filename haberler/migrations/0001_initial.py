# Generated by Django 4.0.5 on 2022-06-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=150)),
                ('baslik', models.CharField(max_length=120)),
                ('acıklama', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('sehir', models.CharField(max_length=50)),
                ('yayımlanma_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

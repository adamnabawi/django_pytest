# Generated by Django 4.1.13 on 2024-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gudang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_gudang', models.TextField(max_length=225)),
                ('kapasitas_gudang', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.13 on 2024-03-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0004_gudang_delete_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='produc',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='product')),
                ('product_name', models.TextField(max_length=225)),
                ('product_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transactio',
            fields=[
                ('transaction_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='transacyion')),
                ('transaction_type', models.TextField(choices=[('in', 'in'), ('out', 'out')], max_length=225)),
                ('wtransaction_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='transaction',
        ),
    ]

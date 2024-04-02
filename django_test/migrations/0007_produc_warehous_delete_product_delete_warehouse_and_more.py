# Generated by Django 4.1.13 on 2024-03-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0006_rename_produc_product_rename_transactio_transaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='produc',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='product')),
                ('product_name', models.TextField(max_length=225)),
                ('product_quantity', models.IntegerField()),
                ('product_update_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='warehous',
            fields=[
                ('warehouse_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='gudang')),
                ('warehouse_name', models.TextField(max_length=225)),
                ('warehouse_capacity', models.IntegerField()),
                ('warehouse_update_time', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='warehouse',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='transaction'),
        ),
    ]

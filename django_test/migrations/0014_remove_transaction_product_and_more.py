# Generated by Django 5.0.6 on 2024-05-18 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0013_rename_wtransaction_date_transaction_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouses', to='django_test.warehouse'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='django_test.product'),
            preserve_default=False,
        ),
    ]

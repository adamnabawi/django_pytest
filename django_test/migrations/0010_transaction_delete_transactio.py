# Generated by Django 4.1.13 on 2024-03-27 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0009_transactio_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('transaction_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='transaction')),
                ('transaction_type', models.TextField(choices=[('in', 'in'), ('out', 'out')], max_length=225)),
                ('wtransaction_date', models.DateTimeField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_test.product')),
                ('warehouse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_test.warehouse')),
            ],
        ),
        migrations.DeleteModel(
            name='transactio',
        ),
    ]

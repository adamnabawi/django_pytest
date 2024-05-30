from django.db import models

# Create your models here.
class warehouse(models.Model):
    warehouse_id = models.AutoField(verbose_name="gudang", primary_key=True, serialize=False, auto_created=True)
    warehouse_name = models.TextField(max_length=225)
    warehouse_capacity = models.IntegerField()
    warehouse_update_time = models.DateField()
    
    def __str__(self):
        return self.warehouse_name
    
class product(models.Model):
    product_id = models.AutoField(verbose_name="product", primary_key=True, serialize=False, auto_created=True)
    product_name = models.TextField(max_length=225)
    product_quantity = models.IntegerField()
    product_update_time = models.DateField()
    
    def __str__(self):
        return self.product_name
    
class transaction(models.Model):
    t_type= (
        ('in','in'),
        ('out','out')
    )
    transaction_id = models.AutoField(verbose_name="transaction", primary_key=True, serialize=False, auto_created=True)
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, related_name="warehouses")
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="products")
    transaction_type = models.TextField(max_length=225, choices=t_type)
    transaction_date = models.DateTimeField()
    
    def __str__(self):
        return str(self.transaction_id)
    
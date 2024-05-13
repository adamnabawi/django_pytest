
import pytest
from django.utils import timezone
from django.db.models import Count

#def test_example():
 #   assert 1 == 1

@pytest.mark.django_db
def test_model():
    from django_test.models import warehouse
    warehouse.objects.create(
        warehouse_name = "Gudang 1",
        warehouse_capacity =20,
        warehouse_update_time = timezone.now())
    warehouse.objects.create(
        warehouse_name = "Gudang 2",
        warehouse_capacity =20,
        warehouse_update_time = timezone.now())
    warehouse.objects.create(
        warehouse_name = "Gudang 3",
        warehouse_capacity =40,
        warehouse_update_time = timezone.now())
    warehouse.objects.create(
        warehouse_name = "Gudang 4",
        warehouse_capacity =40,
        warehouse_update_time = timezone.now())
    
    from django_test.models import product
    product.objects.create(
        product_name = "Produk 1",
        product_quantity = 50,
        product_update_time = timezone.now() 
    )
    product.objects.create(
        product_name = "Produk 2",
        product_quantity = 50,
        product_update_time = timezone.now() 
    )
    
    totalgudang = warehouse.objects.count()
    cap20 = warehouse.objects.filter(warehouse_capacity=20).count()
    cap40 = warehouse.objects.filter(warehouse_capacity=40).count()
    totalproduk = product.objects.count()

    assert totalgudang == 4
    assert cap20 == 2
    assert cap40 == 2
    assert totalproduk == 2
    

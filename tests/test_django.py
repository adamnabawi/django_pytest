
import pytest
from django.utils import timezone

#def test_example():
 #   assert 1 == 1

@pytest.mark.django_db
def test_model():
    from django_test.models import warehouse, transaction, product

    wh1 = warehouse.objects.create(
        warehouse_name = "Gudang 1",
        warehouse_capacity =20,
        warehouse_update_time = timezone.now())
    wh2 = warehouse.objects.create(
        warehouse_name = "Gudang 2",
        warehouse_capacity =20,
        warehouse_update_time = timezone.now())
    wh3 = warehouse.objects.create(
        warehouse_name = "Gudang 3",
        warehouse_capacity =40,
        warehouse_update_time = timezone.now())
    wh4 = warehouse.objects.create(
        warehouse_name = "Gudang 4",
        warehouse_capacity =40,
        warehouse_update_time = timezone.now())
    
    pd1 = product.objects.create(
        product_name = "Produk 1",
        product_quantity = 50,
        product_update_time = timezone.now())
    pd2 = product.objects.create(
        product_name = "Produk 2",
        product_quantity = 50,
        product_update_time = timezone.now())
    
    totalgudang = warehouse.objects.count()
    cap20 = warehouse.objects.filter(warehouse_capacity=20).count()
    cap40 = warehouse.objects.filter(warehouse_capacity=40).count()
    totalproduk = product.objects.count()

    assert totalgudang == 4
    assert cap20 == 2
    assert cap40 == 2
    assert totalproduk == 2

    tx1 = transaction.objects.create(
        warehouse = wh1,
        product = pd2,
        transaction_type = "in",
        transaction_date = timezone.now()
    )

   # gudang = warehouse.objects.get(
    #    warehouse_id = wh1.pk)

    #print(gudang.warehouses.all())

    gudang = warehouse.objects.get(warehouse_name = "Gudang 1")
    tc1 = gudang.warehouses.all()

    produk = product.objects.get(product_name = "Produk 2")
    tc2 = produk.products.all()


    tipe_transaksi = tx1.transaction_type
    nama_gudang = tx1.warehouse
    nama_produk = tx1.product
    jumlah_produk = tx1.product.product_quantity
    waktu_transaksi = tx1.transaction_date.strftime("%d-%m-%Y %H:%M:%S")
    

    print(tc1)
    print(tc2)
    print("")

    
    print("Tipe Transaksi :", tipe_transaksi)
    print("Gudang : ", nama_gudang)
    print("Jenis Produk : ", nama_produk)
    print("Jumlah Produk : ", jumlah_produk)
    print("Waktu Transaksi : ",waktu_transaksi)
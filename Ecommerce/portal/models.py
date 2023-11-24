from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    user_ref_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")
    role_ref_id = models.ForeignKey('RoleMst', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')
    address = models.TextField()
    contact_no = models.CharField(max_length=15)

    class Meta:
        db_table = "tbl_user_detail"

class Master(models.Model):
    master_type = models.CharField(max_length=255)
    master_value = models.CharField(max_length=255)
    master_key = models.CharField(max_length=255)

    class Meta:
        db_table = "tbl_master"

class TokenMaster(models.Model):

    user_access_token = models.CharField(max_length=255)
    user_refresh_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
    user_ref_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")

    class Meta:
        db_table = "tbl_token_master"

class CountryCurrency(models.Model):
    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=5)
    country_code = models.CharField(max_length=5)
    currency_code = models.CharField(max_length=5)
    currency_symbol = models.CharField(max_length=5)

    class Meta:
        db_table = "tbl_country_currency"

class CompanyMst(models.Model):
    company_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    ownership_status_ref_id = models.ForeignKey('Master', on_delete=models.CASCADE)
    cin_no = models.CharField(max_length=20)
    pan_no = models.CharField(max_length=20)
    tan_no = models.CharField(max_length=20)
    gst_no = models.CharField(max_length=20)

    class Meta:
        db_table = "tbl_company_mst"

class RoleMst(models.Model):
    # company_ref_id = models.ForeignKey('CompanyMst', on_delete=models.CASCADE)
    role_name = models.CharField(max_length=255)

    class Meta:
        db_table = "tb_role_mst"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_category"

class UOM(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_uom"

class ProductBrand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_product_brand"

class ProductMst(models.Model):
    product_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey('ProductBrand', on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    category_ref_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    uom_ref_id = models.ForeignKey('UOM', on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_product_mst"

class ProductDetails(models.Model):
    product_ref_id = models.ForeignKey('ProductMst', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images/')

    class Meta:
        db_table = "tbl_details_mst"

class CartMst(models.Model):
    user_ref_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")
    total_quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tbl_cart_mst"

class CartDetail(models.Model):
    cart_ref_id = models.ForeignKey('CartMst', on_delete=models.CASCADE)
    product_ref_id = models.ForeignKey('ProductMst', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tbl_cart_detail"

class Wishlist(models.Model):
    user_ref_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")
    product_ref_id = models.ForeignKey('ProductMst', on_delete=models.CASCADE)
    is_wishlist = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_wishlist"

class OrderMst(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")
    total_order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    order_status = models.ForeignKey('Master', on_delete=models.CASCADE, related_name='order_statuses')
    shipping_address = models.TextField()
    billing_address = models.TextField()
    payment_type = models.ForeignKey('Master', on_delete=models.CASCADE, related_name='payment_types')

    class Meta:
        db_table = "tbl_order_mst"
        
class OrderDetail(models.Model):
    order_ref_id = models.ForeignKey('OrderMst', on_delete=models.CASCADE)
    product_ref_id = models.ForeignKey('ProductMst', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tbl_order_detail"

class StockMst(models.Model):
    product_ref_id = models.ForeignKey(ProductMst, on_delete=models.CASCADE)

class StockDetail(models.Model):
    stock_ref_id = models.ForeignKey(StockMst, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

class MainMenu(models.Model):
    app_url = models.CharField(max_length=255)
    app_icon = models.CharField(max_length=255)
    menu_name = models.CharField(max_length=255)
    role_id = models.ForeignKey(RoleMst, on_delete=models.CASCADE)

class SubMenu(models.Model):
    main_menu_ref_id = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    app_url = models.CharField(max_length=255)
    menu_name = models.CharField(max_length=255)
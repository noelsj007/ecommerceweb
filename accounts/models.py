from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
"""
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)
"""

class UserRegister(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField() 
    user_dob = models.CharField(max_length=10)
    user_gender = models.CharField(max_length=10)
    user_phonenumber = models.IntegerField()
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_password = models.CharField(max_length=100)
    user_address = models.TextField(default=None)
    def __str__(self):
        return self.user_name



"""
class UserProfile(models.Model):  
    user = models.ForeignKey(User, unique=True)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    employer = models.ForeignKey(Employer)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
        """

class AddToCart(models.Model):
    cart_useremail = models.EmailField(default=None)
    cart_name = models.CharField(max_length=1024)
    cart_image = models.ImageField(upload_to = 'cartimages/')
    cart_price = models.PositiveIntegerField()
    cart_publisher = models.CharField(max_length=1024)
    cart_origin = models.CharField(max_length=1024)
    cart_description = models.TextField()
    cart_quantity = models.PositiveIntegerField(default=0)
    cart_total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cart_name


def return_datetime():
    now = timezone.now()
    return now + timedelta(days=20)


class Order(models.Model):
    order_useremail = models.EmailField(default=None)
    order_name = models.CharField(max_length=1024)
    order_image = models.ImageField(upload_to = 'orderimages/')
    order_price = models.PositiveIntegerField()
    order_publisher = models.CharField(max_length=1024)
    order_origin = models.CharField(max_length=1024)
    order_description = models.TextField()
    order_domain= models.CharField(max_length=100, default='null')
    order_quantity = models.PositiveIntegerField(default=1)
    order_total_price = models.PositiveIntegerField(default=0)
    order_ordered_date = models.DateTimeField(default= datetime.now())
    order_delivery_date = models.DateTimeField(default= return_datetime)
    order_address = models.TextField(default="address")
    order_phonenumber = models.IntegerField(default=9061325108)
    paymentstatus = models.CharField(max_length =100, default=False)

    def __str__(self):
        return self.order_name

class Product(models.Model):
    product_useremail = models.EmailField(default=None)
    product_price = models.PositiveIntegerField()
    product_domain= models.CharField(max_length=100)
    product_phonenumber = models.IntegerField()
    product_ordered_date = models.DateTimeField(default= datetime.now())
    product_delivery_date = models.DateTimeField(default= return_datetime)
    product_home = models.CharField(max_length=100)
    product_contact = models.CharField(max_length=100)
    product_blog = models.CharField(max_length=100)
    product_news = models.CharField(max_length=100)
    product_event = models.CharField(max_length=100)
    product_product = models.CharField(max_length=100)
    product_shop = models.CharField(max_length=100)
    product_login= models.CharField(max_length=10 )

    def __str__(self):
        return self.product_useremail

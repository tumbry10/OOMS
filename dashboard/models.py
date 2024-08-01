from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "SystAdmin"), (2, "SalesRep"), (3, "Customer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class SystAdmin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural='SystAdmin'

    def __str__(self):
        return self.admin

class SalesRep(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural='SalesRep'

    def __str__(self):
        return self.admin

class Customer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural='Customer'

    def __str__(self):
        return self.admin
    
# Django Signal so wen new user is created it will add a new row in SystAdmin, SalesRep & Customer tables
# with its id in admin_id column

@receiver (post_save, sender=CustomUser)
def create_user_profile(sender,instance, created, **kwags):
    if created:
        if instance.user_type == 1:
            SystAdmin.objects.create(admin=instance)
        if instance.user_type == 2:
            SalesRep.objects.create(admin=instance, gender="")
        if instance.user_type == 3:
            Customer.objects.create(admin=instance, gender="")

@receiver (post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwags):
    if instance.user_type == 1:
        instance.systadmin.save() 
    if instance.user_type == 2:
        instance.salesrep.save()
    if instance.user_type == 3:
        instance.customer.save() 
from django.db.models.signals import pre_delete, post_delete
from .models import Product
from django.dispatch import receiver

@receiver(pre_delete, sender=Product)
def pre_delete_profile(sender, **kwargs):
    print("You are about to delete something!")

@receiver(post_delete, sender=Product)
def delete_profile(sender, **kwargs):
    print("You have just deleted a Product!!!")
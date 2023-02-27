from django.contrib import admin

from .models import Product,User,Message

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Message)

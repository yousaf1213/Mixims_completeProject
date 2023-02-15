from rest_framework import serializers
from .models import Product,User

class CommonSerializer(serializers.ModelSerializer):
    user=User.objects.all()

    class Meta:
        model = User
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    user=CommonSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    products=ProductSerializer(source="set_user",many=True)
    class Meta:
        model = User
        fields = "__all__"





# serializers/order_detail.py
from rest_framework import serializers
from models.order_detail import OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'product_id', 'quantity']

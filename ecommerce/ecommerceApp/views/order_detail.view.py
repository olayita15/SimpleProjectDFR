# views/order_detail.py
from rest_framework import generics
from models.order_detail import OrderDetail
from serializers.order_detail import OrderDetailSerializer

class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects

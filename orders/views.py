from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def orders_page(request):
    context = {
        'orders': SalesOrder.objects.all()
    }
    return render(request, 'index.html', context)


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, 'main_app.html')


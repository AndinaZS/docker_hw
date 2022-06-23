from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = StockProduct.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        product = self.request.GET.get('product', '')
        if product:
            queryset = Stock.objects.filter(positions__product__title__icontains=product)
        else:
            queryset = Stock.objects.all()
        return queryset.order_by('id')
    def perform_update(self, serializer):
        request = self.request
        serializer.save()
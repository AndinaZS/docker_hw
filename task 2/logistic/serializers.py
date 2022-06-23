from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(product=position['product'],
                                        quantity=position['quantity'],
                                        price=position['price'],
                                        stock_id=stock.id)

        return stock

    def partial_update(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(validated_data)

        for position in positions:
            product = StockProduct.objects.all().filter(stock_id=stock.id, product=position['product'])
            if product:
                if position['quantity'] == 0:
                    product.delete()
                else:
                    product.update(quantity=position['quantity'],
                                    price=position['price'])
            else:
                StockProduct.objects.create(product=position['product'],
                                            quantity=position['quantity'],
                                            price=position['price'],
                                            stock_id=stock.id)

        return stock


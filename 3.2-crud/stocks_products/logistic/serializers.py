from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['stock', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'products']
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for i in positions:
            item = StockProduct(
                product=i.get('product'),
                quantity=i.get('quantity'),
                price=i.get('price'),
                stock=stock.id
            )
            item.save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

from django.db import transaction
from rest_framework import serializers

from commerc_net.models.base import Address, Product
from commerc_net.models.retail_network import RetailNetwork
from commerc_net.serializers.base import AddressPartSerializer, ProductPartSerializer


class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(max_digits=19, decimal_places=2, required=False)
    address = AddressPartSerializer(read_only=True)
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ("id", "created")

    def is_valid(self, *, raise_exception=False):
        """валидация адреcа или продукта"""
        self._address = self.initial_data.pop('address')
        self._product = self.initial_data.pop('product')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """переопределение метода создания продукта и адреса"""
        with transaction.atomic():
            retail_network = RetailNetwork.objects.create(**validated_data)
            address, _ = Address.objects.get_or_create(**self._address)
            product, _ = Product.objects.get_or_create(**self._product)
            retail_network.address = address
            retail_network.product.add(product)
            retail_network.save()

        return retail_network


class RetailNetworkListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('__all__',)


class RetailNetworkUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    address = AddressPartSerializer(
        read_only=True,
        required=False
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')

    def is_valid(self, *, raise_exception=False):
        """валидация адреcа или продукта"""
        if 'address' in self.initial_data:
            self._address = self.initial_data.pop('address')
        else:
            self._address = None
        if 'product' in self.initial_data:
            self._product = self.initial_data.pop('product')
        else:
            self._product = None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        """переопределение метода сохранения продукта и адреса"""
        retail_network = super().save()

        with transaction.atomic():
            if self._address:
                if retail_network.address is None:
                    address, _ = Address.objects.get_or_create(**self._address)
                else:
                    address, _ = Address.objects.update_or_create(id=retail_network.address.pk, defaults=self._address)
                retail_network.address = address
            if self._product:
                if retail_network.address is None:
                    product, _ = Product.objects.get_or_create(**self._address)
                else:
                    product, _ = Product.objects.update_or_create(self._product.pk, **self._product)
                retail_network.product.add(product)

            retail_network.save()

        return retail_network

from django.db import transaction
from rest_framework import serializers

from commerc_net.models.base import Address, Product
from commerc_net.models.individual_entrepreneur import IndividualEntrepreneur
from commerc_net.serializers.base import AddressPartSerializer, ProductPartSerializer


class IndividualEntrepreneurCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(max_digits=19, decimal_places=2, required=False)
    address = AddressPartSerializer(read_only=True)
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
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
            individual_entrepreneur = IndividualEntrepreneur.objects.create(**validated_data)
            address, _ = Address.objects.get_or_create(**self._address)
            product, _ = Product.objects.get_or_create(**self._product)
            individual_entrepreneur.address = address
            individual_entrepreneur.product.add(product)
            individual_entrepreneur.save()

        return individual_entrepreneur


class IndividualEntrepreneurListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ('__all__',)


class IndividualEntrepreneurUpdateSerializer(serializers.ModelSerializer):
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
        model = IndividualEntrepreneur
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
        """переопределение метода сохранения проодукта и адреса"""
        individual_entrepreneur = super().save()

        with transaction.atomic():
            if self._address:
                if individual_entrepreneur.address is None:
                    address, _ = Address.objects.get_or_create(**self._address)
                else:
                    address, _ = Address.objects.update_or_create(id=individual_entrepreneur.address.pk, defaults=self._address)
                individual_entrepreneur.address = address
            if self._product:
                if individual_entrepreneur.address is None:
                    product, _ = Product.objects.get_or_create(**self._address)
                else:
                    product, _ = Product.objects.update_or_create(self._product.pk, **self._product)
                individual_entrepreneur.product.add(product)

            individual_entrepreneur.save()

        return individual_entrepreneur

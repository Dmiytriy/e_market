from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from commerc_net.models.factory import Factory
from commerc_net.serializers.factory import FactoryCreateSerializer, FactoryListSerializer, FactoryUpdateSerializer


class FactoryCreateView(CreateAPIView):
    model = Factory
    serializer_class = FactoryCreateSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]


class FactoryListView(ListAPIView):
    model = Factory
    serializer_class = FactoryListSerializer
    queryset = Factory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class FactoryRetrieveView(RetrieveUpdateDestroyAPIView):
    model = Factory
    serializer_class = FactoryUpdateSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]
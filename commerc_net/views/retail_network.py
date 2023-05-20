from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from commerc_net.models.retail_network import RetailNetwork
from commerc_net.serializers.retail_network import RetailNetworkCreateSerializer, RetailNetworkListSerializer, \
    RetailNetworkUpdateSerializer


class RetailNetworkCreateView(CreateAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkCreateSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class RetailNetworkListView(ListAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkListSerializer
    queryset = RetailNetwork.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class RetailNetworkRetrieveView(RetrieveUpdateDestroyAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkUpdateSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]
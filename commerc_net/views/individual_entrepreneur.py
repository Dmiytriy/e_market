from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from commerc_net.models.individual_entrepreneur import IndividualEntrepreneur
from commerc_net.serializers.individual_entrepreneur import IndividualEntrepreneurCreateSerializer, \
    IndividualEntrepreneurListSerializer, IndividualEntrepreneurUpdateSerializer


class IndividualEntrepreneurCreateView(CreateAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurCreateSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated]


class IndividualEntrepreneurListView(ListAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurListSerializer
    queryset = IndividualEntrepreneur.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class IndividualEntrepreneurRetrieveView(RetrieveUpdateDestroyAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurUpdateSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated]
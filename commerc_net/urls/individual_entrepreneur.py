from django.urls import path

from commerc_net.views.individual_entrepreneur import IndividualEntrepreneurCreateView, \
    IndividualEntrepreneurListView, IndividualEntrepreneurRetrieveView

urlpatterns = [
    path('create/', IndividualEntrepreneurCreateView.as_view(), name='individual_entrepreneur_create'),
    path('list/', IndividualEntrepreneurListView.as_view(), name='individual_entrepreneur_list'),
    path('<int:pk>/', IndividualEntrepreneurRetrieveView.as_view(), name='individual_entrepreneur_RUD'),
]
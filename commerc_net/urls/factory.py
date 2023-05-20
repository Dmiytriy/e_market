from django.urls import path

from commerc_net.views.factory import FactoryCreateView, FactoryListView, FactoryRetrieveView

urlpatterns = [
    path('create/', FactoryCreateView.as_view(), name='factory_create'),
    path('list/', FactoryListView.as_view(), name='factory_list'),
    path('<int:pk>/', FactoryRetrieveView.as_view(), name='factory_RUD'),
]
from django.urls import path

from commerc_net.views.retail_network import RetailNetworkCreateView, RetailNetworkListView, RetailNetworkRetrieveView

urlpatterns = [
    path('create/', RetailNetworkCreateView.as_view(), name='commerc_net_create'),
    path('list/', RetailNetworkListView.as_view(), name='commerc_net_list'),
    path('<int:pk>/', RetailNetworkRetrieveView.as_view(), name='commerc_net_RUD'),
]
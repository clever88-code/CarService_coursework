from django.urls import path

from .views import OrderFormView, add_orders

app_name = "orders"


urlpatterns = [
    path('', OrderFormView.as_view(), name="orders"),
    path('add_orders', add_orders, name="add_orders"),
]
from django.urls import path
from customers.views import (
	customer_create_view, 
	customer_detail_view, 
	customer_delete_view, 
	customer_list_view,
	customer_update_view,
)

app_name = 'customers'
urlpatterns = [
    path('create/', customer_create_view),
    path('<int:my_id>/', customer_detail_view, name='customer-detail'),
    path('<int:my_id>/update', customer_update_view, name='customer-update'),
    path('<int:my_id>/delete', customer_delete_view, name='customer-delete'),
    path('', customer_list_view, name='customer-list'),
]
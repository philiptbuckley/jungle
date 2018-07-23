"""jungle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from customers.views import customer_detail_view, customer_create_view, customer_delete_view, customer_list_view
from pages.views import home_view, contact_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('customer/<int:my_id>', customer_detail_view, name='customer'),
    path('customer/<int:my_id>/delete', customer_delete_view, name='customer-delete'),
    path('customer/create/', customer_create_view),
    path('customer/list/', customer_list_view),
    path('admin/', admin.site.urls),
]

from django.urls import path
from django.contrib import admin
from Purchase import views

urlpatterns = [
      path('',views.purchaseDetail, name='purchase-details'),
      path('purchase-add/',views.purchaseAdd, name='purchase-add'),
      path('stock/<int:id>/', views.stockMaster, name='stock_master'),
      path('stock_add/<int:id>/', views.stockAdd, name='stock_add'),
    ]

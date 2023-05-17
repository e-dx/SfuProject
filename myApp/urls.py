from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('warehouse/', views.warehouse),
    path('products/', views.products),
    path('press/', views.press),
    path('vendors/', views.vendors)
]
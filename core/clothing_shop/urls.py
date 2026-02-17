from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.cloth_list, name='cloth_list'),
    path('cloth/<int:pk>/', views.cloth_detail, name='cloth_detail'),
    
    
    path('cloth/add/', views.ClothCreateView.as_view(), name='cloth_create'),
    path('cloth/<int:pk>/edit/', views.ClothUpdateView.as_view(), name='cloth_update'),
    path('cloth/<int:pk>/delete/', views.ClothDeleteView.as_view(), name='cloth_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Пустая строка означает "главная"
]
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cloth
from django.shortcuts import render, get_object_or_404


class ClothListView(ListView):
    model = Cloth
    template_name = 'index.html'
    context_object_name = 'clothes' 

class ClothCreateView(CreateView):
    model = Cloth
    template_name = 'cloth_form.html'
    fields = ['title', 'cloth_color', 'size', 'price', 'stock_quantity', 'brand']
    success_url = reverse_lazy('cloth_list') 


class ClothUpdateView(UpdateView):
    model = Cloth
    template_name = 'cloth_form.html' 
    fields = ['title', 'cloth_color', 'size', 'price', 'stock_quantity', 'brand']
    success_url = reverse_lazy('cloth_list')


class ClothDeleteView(DeleteView):
    model = Cloth
    template_name = 'cloth_confirm_delete.html'
    success_url = reverse_lazy('cloth_list')
    
# 1. ФУНКЦІЯ ДЛЯ СПИСКУ (Головна)
def cloth_list(request):
    items = Cloth.objects.all()
    query = request.GET.get('q')
    if query:
        items = items.filter(title__icontains=query)
    
    # Переконайся, що тут 'index.html'
    return render(request, 'index.html', {'items': items})

# 2. ФУНКЦІЯ ДЛЯ ДЕТАЛЕЙ
def cloth_detail(request, pk):
    item = get_object_or_404(Cloth, pk=pk)
    return render(request, 'cloth_detail.html', {'item': item})
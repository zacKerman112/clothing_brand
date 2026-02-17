from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic  
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.forms import UserCreationForm 
from .models import Cloth

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


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def cloth_list(request):
    items = Cloth.objects.all()
    query = request.GET.get('q')
    if query:
        items = items.filter(title__icontains=query)
        
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        items = items.order_by('price')
    elif sort == 'price_desc':
        items = items.order_by('-price')
        
    return render(request, 'index.html', {'items': items})    
    
    
    return render(request, 'index.html', {'items': items})


def cloth_detail(request, pk):
    item = get_object_or_404(Cloth, pk=pk)
    return render(request, 'cloth_detail.html', {'item': item})
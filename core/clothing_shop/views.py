from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cloth
from .forms import RegistrtionForm

class ClothListView(ListView):
    model = Cloth
    template_name = 'index.html'
    context_object_name = 'clothes' 


class ClothDetailView(DetailView):
    model = Cloth
    template_name = 'cloth_detail.html'


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



def register(request):
    if request.method == 'POST':
        form = RegistrtionForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrtionForm()    
        
    return render(request, 'registration/register.html', {'form': form})    
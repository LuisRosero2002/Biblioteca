from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from libros.models import Nacionalidad, Genero, Autor, Libro

# Create your views here.
class AutoresListView(ListView):
    model = Autor

class AutorDetailView(DetailView):
    model = Autor

##############################################

class LibroListView(ListView):
    model = Libro

class LibroDetailView(DetailView):
    model = Libro


####################################################
class AutorCreate(CreateView):
    model = Autor
    fields = '__all__'

class AutoresUpdate(UpdateView):
    model = Autor
    fields = '__all__' 
    template_name = ' '


class AutoresDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autores-list')

####################################################

class LibroCreate(CreateView):
    model = Libro
    fields = '__all__'

class LibroUpdate(UpdateView):
    model = Libro
    fields = '__all__' 


class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro-list')  
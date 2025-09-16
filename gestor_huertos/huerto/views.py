from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import Cultivo

class CultivoListView(ListView):
    model = Cultivo
    template_name = "cultivo_lista.html"
    context_object_name = "cultivos"
class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "cultivo_form.html"
    success_url = reverse_lazy("cultivos:lista")
class CultivoUpdateView(UpdateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "cultivo_form.html"
    success_url = reverse_lazy("cultivos:lista")
class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = "cultivo_confirmar_eliminar.html"
    success_url = reverse_lazy("cultivos:lista")
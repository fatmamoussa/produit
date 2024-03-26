from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView,ListView
from produit.models import produit
from produit.forms import produitForm
from django.urls import reverse_lazy

class CreateproduitView(CreateView):
    template_name = 'produit/ajouter.html'
    model = produit
    form_class = produitForm
    success_url = reverse_lazy('list-produit')
    success_message = ("%(name)s was created successfully")

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form)
  
class ListproduitView(ListView):
    template_name = "produit/list.html"
    model = produit

    #paginate_by = 10        
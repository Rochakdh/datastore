from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,DeleteView,TemplateView,UpdateView
from .forms import PersonalDetailsForm
from django.urls import reverse,reverse_lazy
from .models import PersonalDetails
# Create your views here.

class Index(TemplateView):
    template_name = 'crud/index.html'


class ProfileCreate(CreateView):
    template_name = 'crud/index.html'
    form_class = PersonalDetailsForm
    success_url = reverse_lazy('crud:table')


class ProfileDelete(DeleteView):
    model = PersonalDetails
    success_url = reverse_lazy('crud:table')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class ProfileUpdate(UpdateView):
    template_name = 'crud/update.html'
    form_class = PersonalDetailsForm
    model = PersonalDetails
    success_url = reverse_lazy('crud:table')
    queryset = PersonalDetails.objects.all()

class TableView(ListView):
    template_name = 'crud/detail.html'
    form_class = PersonalDetailsForm
    queryset = PersonalDetails.objects.all()


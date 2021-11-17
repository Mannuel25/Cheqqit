from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Tasks

class HomePageView(TemplateView):
    template_name = 'home.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class WebappPageView(ListView):
    template_name = 'webapp.html'

class TasksList(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        

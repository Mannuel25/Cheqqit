from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTasks

class HomePageView(TemplateView):
    template_name = 'home.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class WebappPageView(TemplateView):
    template_name = 'webapp.html'

class InboxView(LoginRequiredMixin, ListView):
    model = UserTasks
    context_object_name = 'tasks'
    template_name = 'inbox.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('Context_1:', context)
        # context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = context['tasks'].filter(complete=False).count()
        # print('Context_2:', context)

        search_input = self.request.GET.get('search-area') or ''
        print('SEARCH INPUT:', search_input)
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context  

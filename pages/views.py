from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTasks
from .forms import TaskDetails

class HomePageView(TemplateView):
    template_name = 'home.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class WebappPageView(TemplateView):
    template_name = 'webapp.html'

class InboxView(LoginRequiredMixin, ListView):
    model = UserTasks
    template_name = 'inbox.html'
    login_url = 'login'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('CONTEXT DATA 1:', context)
        all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
        print('ALL USER TASKS 2:', all_tasks)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed_task=False).count()
        print('CONTEXT 2:', context)
        all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
        print('\n\nall incomplete tasks:', all_incomplete)
        # print(all_incomplete[0])

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context

class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TaskDetails
    template_name = 'create_task.html'
    success_url = reverse_lazy('inbox')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class TaskDetailView(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'task_detail.html'
#     login_url = 'login'

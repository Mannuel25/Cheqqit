from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import UserTasks
from .forms import TaskDetailsForm, ViewTaskDetailsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

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
    success_url = reverse_lazy('inbox')

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
        print('-'*29)
        print(f'\n\nCURENT USER: {self.request.user}')

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context

class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TaskDetailsForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('inbox')
    login_url = 'login'
   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required(login_url='login')
def UpdateTask(request, slug):
        user_task = get_object_or_404(UserTasks, slug=slug)
        form = TaskDetailsForm(instance=user_task)
        if request.method == 'POST':
            form = TaskDetailsForm(request.POST, instance=user_task)
            if form.is_valid():
                form.save()
                return redirect('inbox')
        context = {'form':form, 'slug':slug}
        return render(request, 'update_task.html', context)

@login_required(login_url='login')
def TaskDetail(request, slug):
    user_task = get_object_or_404(UserTasks, slug=slug)
    form = ViewTaskDetailsForm(instance=user_task)
    context = {'form':form, 'slug':slug}
    return render(request, 'task_detail.html', context)

@login_required(login_url='login')
def DeleteTask(request, slug):
    user_tasks = UserTasks.objects.get(slug=slug)
    user_tasks.delete()
    return redirect('inbox')

def page_not_found(request, exception):
    return render(request, '404.html')
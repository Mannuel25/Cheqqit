from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import UserTasks
from .forms import TaskDetailsForm, ViewTaskDetailsForm, AllTasksForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime 

class HomePageView(TemplateView):
    template_name = 'home.html'
class FeaturesPageView(TemplateView):
    template_name = 'features.html'

done_tasks, lst_undone_task = [], []
today_date = datetime.today().strftime('%a %b %d, %Y')
tasks_due_dates, today_tasks = [], []
remove_none, selected_task = [], []
all_completed_tasks = []
selected_task = ''

class InboxView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'inbox.html'
    login_url = 'login'
    context_object_name = 'tasks'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        if self.request.method == 'POST':
            form =  AllTasksForm(self.request.POST or None)
            list_ = self.request.POST.getlist('checkbox')
            for i in list_:
                done_tasks.append(i)
                messages.success(self.request, f'{i} completed') 
            return redirect('inbox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        
        try: 
            join_done_task = ''.join(i for i in done_tasks[-1])
        except: 
            pass
        else: 
            join_done_task = ''.join(i for i in done_tasks[-1])
            context['tasks'].filter(title=join_done_task).delete()
            context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
            for i in context['object_list']:
                if str(i) == join_done_task:
                    all_completed_tasks.append(i)
            for i in today_tasks:
                if join_done_task == str(i):
                    today_tasks.remove(i)
        lst_undone_task.append(context['no_of_undone_tasks'])
        context['all_completed_tasks'] = set(all_completed_tasks)     
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

class TodayView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'today.html'
    success_url = reverse_lazy('today') 
    context_object_name = 'tasks'
    login_url = 'login'

    def form_valid(self, form):
        if self.request.method == 'POST':
            form =  AllTasksForm(self.request.POST or None)
            list_ = self.request.POST.getlist('checkbox')
            for i in list_:
                selected_task.append(i)
                messages.success(self.request, f'{i} completed')
            return redirect('today')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        context['today_date'] = today_date
        format_today_date = datetime.today().strftime('%Y-%m-%d')
        
        try: 
            join_done_task = ''.join(i for i in selected_task[-1])
        except: 
            pass
        else: 
            join_done_task = ''.join(i for i in selected_task[-1])

            for i in context['object_list']:
                if str(i) == join_done_task:
                    all_completed_tasks.append(i)
            context['tasks'].filter(title=join_done_task).delete()
            context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
            for i in today_tasks:
                if join_done_task == str(i):
                    today_tasks.remove(i)
        for i in context['tasks']:
            if i.task_due_date != None:
                tasks_due_dates.append(str(i.task_due_date))
        
        your_today_tasks = []
        context['all_completed_tasks'] = set(all_completed_tasks)     

        for i in context['tasks']:
            for j in tasks_due_dates:
                if str(i.task_due_date) == j and j == format_today_date:
                    your_today_tasks.append(i)

        context['your_today_tasks'] = set(your_today_tasks)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['your_today_tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

class CreateTaskView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = TaskDetailsForm
    template_name = 'create_task.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('inbox')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        
        try: 
            join_done_task = ''.join(i for i in done_tasks[-1])
        except: 
            pass
        else: 
            join_done_task = ''.join(i for i in done_tasks[-1])
            context['tasks'].filter(title=join_done_task).delete()
            context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()

        context['all_completed_tasks'] = set(all_completed_tasks)     

        search_input = self.request.GET.get('search-box') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

class CompletedTasksView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'completed_tasks.html'
    success_url = reverse_lazy('completed_tasks') 
    context_object_name = 'tasks'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        context['all_completed_tasks'] = set(all_completed_tasks)     
        # try: 
        #     join_done_task = ''.join(i for i in selected_task[-1])
        # except: 
        #     pass
        # else: 
        #     join_done_task = ''.join(i for i in selected_task[-1])
        #     context['tasks'].filter(title=join_done_task).delete()
        #     context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        #     print('all tasks:', context['tasks'])
        search_input = self.request.GET.get('search-box') or ''
        if search_input:
            context['all_completed_tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

class LabelsView(LoginRequiredMixin, TemplateView):
    template_name = 'labels.html'
    login_url = 'login'

@login_required(login_url='login')
def UpdateTask(request, slug):
    user_task = get_object_or_404(UserTasks, slug=slug)
    form = TaskDetailsForm(instance=user_task)
    if request.method == 'POST':
        form = TaskDetailsForm(request.POST, instance=user_task)
        if form.is_valid():
            form.save()
            return redirect('inbox')
    context = {'form':form, 'slug':slug, 'no_of_undone_tasks':lst_undone_task[-1]}
    return render(request, 'update_task.html', context)

@login_required(login_url='login')
def TaskDetail(request, slug):
    user_task = get_object_or_404(UserTasks, slug=slug)
    task_title = UserTasks.objects.get(slug=slug)
    form = ViewTaskDetailsForm(instance=user_task)
    context = {'form':form, 'slug':slug, 
        'task_title':task_title,  'no_of_undone_tasks':lst_undone_task[-1]}
    return render(request, 'task_detail.html', context)

@login_required(login_url='login')
def DeleteTask(request, slug):
    user_tasks = UserTasks.objects.get(slug=slug)
    user_tasks.delete()
    return redirect('inbox')

def page_not_found(request, exception):
    return render(request, '404.html')

def server_error(request, exception=None):
    return render(request, '500.html')
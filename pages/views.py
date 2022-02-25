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

class HomePageView(TemplateView):
    template_name = 'home.html'
class FeaturesPageView(TemplateView):
    template_name = 'features.html'
class WebappPageView(TemplateView):
    template_name = 'webapp.html'

done_tasks, lst_undone_task = [], []

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
                print('done tasks:', done_tasks)
                messages.success(self.request, f'{i} completed')
            if form.is_valid():
                form.save() 
                return redirect('inbox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        # all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
        try: 
            # print(F' \n\n\nUNDOnE TASK: {done_tasks[-1]}')
            # print(F' \n\n\nALL UNDONE TASK: {done_tasks}')
            join_done_task = ''.join(i for i in done_tasks[-1])
        except: 
            # print('error occured')
            # print('LENGTH OF UNDONE TASKS IS:',len(done_tasks))
            pass
        else: 
            # print('NO ERROR!!')
            # print(F' n\n\nALL UNDOE TASKS: {done_taskn           s[-1]}')
            join_done_task = ''.join(i for i in done_tasks[-1])
            # print('UNDONE TASKS:',join_done_task)
            
            # print('USERTASKS:',UserTasks.objects.all())
            UserTasks.objects.filter(title=join_done_task).delete()
            context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()

        done_tasks.clear()
        lst_undone_task.append(context['no_of_undone_tasks'])
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context    

class CreateTaskView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = TaskDetailsForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('inbox') 
    context_object_name = 'tasks'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
        # all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
        try: 
            # print(F' \n\n\nUNDOnE TASK: {done_tasks[-1]}')
            # print(F' \n\n\nALL UNDONE TASK: {done_tasks}')
            join_done_task = ''.join(i for i in done_tasks[-1])
        except: 
            # print('error occured')
            # print('LENGTH OF UNDONE TASKS IS:',len(done_tasks))
            pass
        else: 
            # print('NO ERROR!!')
            # print(F' n\n\nALL UNDOE TASKS: {done_tasks[-1]}')
            join_done_task = ''.join(i for i in done_tasks[-1])
            # print('UNDONE TASKS:',join_done_task)
            
            # print('USERTASKS:',UserTasks.objects.all())
            UserTasks.objects.filter(title=join_done_task).delete()
            context['no_of_undone_tasks'] = context['tasks'].filter(completed_task=False).count()
            # lst_done_task.append(i for i i)
        done_tasks.clear()
        # print('undone tasks length:', len(done_tasks))
        # print('\n\nall incomplete tasks:', all_incomplete)
    
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

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

print('\n\n++++lst:',lst_undone_task)

@login_required(login_url='login')
def DeleteTask(request, slug):
    user_tasks = UserTasks.objects.get(slug=slug)
    user_tasks.delete()
    return redirect('inbox')


def page_not_found(request, exception):
    return render(request, '404.html')

def server_error(request, exception=None):
    return render(request, '500.html')
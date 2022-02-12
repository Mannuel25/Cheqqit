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

class HomePageView(TemplateView):
    template_name = 'home.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class WebappPageView(TemplateView):
    template_name = 'webapp.html'

# class InboxView(LoginRequiredMixin, ListView):
#     model = UserTasks
#     template_name = 'inbox.html'
#     login_url = 'login'
#     context_object_name = 'tasks'
#     success_url = reverse_lazy('tasks')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print('CONTEXT DATA 1:', context)
#         all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
#         print('ALL USER TASKS 2:', all_tasks)
#         context['tasks'] = context['tasks'].filter(user=self.request.user)
#         context['count'] = context['tasks'].filter(completed_task=False).count()
#         print('CONTEXT 2:', context)
#         all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
#         print('\n\nall incomplete tasks:', all_incomplete)
        
#         print('-'*29)
#         print(f'\n\nCURENT USER: {self.request.user}')

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['tasks'] = context['tasks'].filter(
#                 title__contains=search_input)

#         context['search_input'] = search_input
#         context['all_incomplete'] = all_incomplete
        
#         return context

undone_tasks = []
class InboxView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'inbox.html'
    login_url = 'login'
    context_object_name = 'tasks'
    # success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # form.instance.user = self.request.user
        # return super().form_valid(form)

        if self.request.method == 'POST':
            form =  AllTasksForm(self.request.POST or None)
            list_ = self.request.POST.getlist('checkbox')
            for i in list_:
                undone_tasks.append(i)
            if form.is_valid():
                form.save() 
                print(F'FORM: {form}')
                # print('LIST:', list_)
                # return redirect('tasks')
                return redirect('inbox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('\n\n--CONTEXT DATA 1:', context)
        all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
        # print('ALL USER TASKS 2:', all_tasks)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed_task=False).count()
        all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
        print('CONTEXT 2:', context)
        try: 
            print(F' \n\n\nUNDOnE TASK: {undone_tasks[-1]}')
            print(F' \n\n\nALL UNDONE TASK: {undone_tasks}')
            join_undone_tasks = ''.join(i for i in undone_tasks[-1])
        except: 
            print('error occured')
            print('LENGTH OF UNDONE TASKS IS:',len(undone_tasks))
        else: 
            just_completed_task = []
            print('NO ERROR!!')
            print(F' n\n\nALL UNDOE TASKS: {undone_tasks[-1]}')
            join_undone_task = ''.join(i for i in undone_tasks[-1])
            print('UNDONE TASKS:',join_undone_task)
            just_completed_task.append(join_undone_task)
            print('USERTASKS:',UserTasks.objects.all())
            UserTasks.objects.filter(title=join_undone_task).delete()
            context['no_of_incomplete_tasks'] = len(undone_tasks)
            UserTasks.objects.filter(title=join_undone_tasks).completed_task = True
        undone_tasks.clear()
        print('undone tasks length:', len(undone_tasks))
        print('\n\nall incomplete tasks:', all_incomplete)
        
        print(f'\n\nCURENT USER: {self.request.user}')
        context['done'] = len(undone_tasks)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context

class AllTasksView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'tasks.html'
    login_url = 'login'
    context_object_name = 'tasks'
    # success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        # form.instance.user = self.request.user
        # return super().form_valid(form)

        if self.request.method == 'POST':
            form =  AllTasksForm(self.request.POST or None)
            list_ = self.request.POST.getlist('checkbox')
            for i in list_:
                undone_tasks.append(i)
            if form.is_valid():
                form.save() 
                print(F'FORM: {form}')
                # print('LIST:', list_)
                return redirect('inbox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('\n\n--CONTEXT DATA 1:', context)
        all_tasks = [i for i in context['tasks'].filter(user = self.request.user)]
        # print('ALL USER TASKS 2:', all_tasks)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = len(undone_tasks)
        context['count'] = len(undone_tasks)
        # context['count'] = context['tasks'].filter(completed_task=False).count()
        all_incomplete = [i for i in context['tasks'].filter(user=self.request.user, completed_task=False)]
        print('CONTEXT 2:', context)
        try: 
            print(F' \n\n\nUNDOnE TASK: {undone_tasks[-1]}')
            print(F' \n\n\nALL UNDONE TASK: {undone_tasks}')
            join_undone_tasks = ''.join(i for i in undone_tasks[-1])
        except: 
            print('error occured')
            print('LENGTH OF UNDONE TASKS IS:',len(undone_tasks))
        else: 
            just_completed_task = []
            print('NO ERROR!!')
            print(F' n\n\nALL UNDOE TASKS: {undone_tasks[-1]}')
            join_undone_task = ''.join(i for i in undone_tasks[-1])
            print('UNDONE TASKS:',join_undone_task)
            just_completed_task.append(join_undone_task)
            print('USERTASKS:',UserTasks.objects.all())
            UserTasks.objects.filter(title=join_undone_task).delete()
            context['no_of_incomplete_tasks'] = len(undone_tasks)
            # UserTasks.objects.filter(title=join_undone_tasks).completed_task = True
        undone_tasks.clear()
        print('undone tasks length:', len(undone_tasks))
        print('\n\nall incomplete tasks:', all_incomplete)
        
        print(f'\n\nCURENT USER: {self.request.user}')
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)
        context['search_input'] = search_input
        return context


# class CreateTaskView(LoginRequiredMixin, CreateView):
#     form_class = TaskDetailsForm
#     template_name = 'create_task.html'
#     success_url = reverse_lazy('inbox')
#     login_url = 'login'
   
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# @login_required(login_url='login')
# def UpdateTask(request, slug):
#         user_task = get_object_or_404(UserTasks, slug=slug)
#         form = TaskDetailsForm(instance=user_task)
#         if request.method == 'POST':
#             form = TaskDetailsForm(request.POST, instance=user_task)
#             if form.is_valid():
#                 form.save()
#                 return redirect('inbox')
#         context = {'form':form, 'slug':slug}
#         return render(request, 'update_task.html', context)

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
                return redirect('tasks')
        context = {'form':form, 'slug':slug}
        return render(request, 'update_task.html', context)


@login_required(login_url='login')
def TaskDetail(request, slug):
    user_task = get_object_or_404(UserTasks, slug=slug)
    task_title = UserTasks.objects.get(slug=slug)
    form = ViewTaskDetailsForm(instance=user_task)
    context = {'form':form, 'slug':slug, 'task_title':task_title}
    return render(request, 'task_detail.html', context)

@login_required(login_url='login')
def DeleteTask(request, slug):
    user_tasks = UserTasks.objects.get(slug=slug)
    user_tasks.delete()
    # return redirect('inbox')
    return redirect('tasks')


def page_not_found(request, exception):
    return render(request, '404.html')


class AllTasksView(LoginRequiredMixin, CreateView, ListView):
    model = UserTasks
    form_class = AllTasksForm
    template_name = 'tasks.html'
    login_url = 'login'
    context_object_name = 'tasks'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        # form.instance.user = self.request.user
        # return super().form_valid(form)

        if self.request.method == 'POST':
            form =  AllTasksForm(self.request.POST or None)
            if form.is_valid():
                form.save() 
                return redirect('inbox')

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

            
        value="{{task}}"

                       
                       
                       
                       
                       
                       
                       
                       
                       
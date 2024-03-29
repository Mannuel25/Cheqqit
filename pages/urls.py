from django.urls import path
from .views import HomePageView, InboxView, CreateTaskView, UpdateTask, TaskDetail, DeleteTask,TodayView, CompletedTasksView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('add_task/', CreateTaskView.as_view(), name='create_task'),
    path('completed_tasks/', CompletedTasksView.as_view(), name='completed_tasks'),
    path('update_task/<slug:slug>/', UpdateTask, name='update_task'),
    path('task_detail/<slug:slug>/', TaskDetail, name='task_detail'),
    path('delete_task/<slug:slug>/', DeleteTask, name='delete_task'),
    path('today/', TodayView.as_view(), name='today'),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
from django.urls import path
from .views import HomePageView
from .views import FeaturesPageView
from .views import WebappPageView
from .views import InboxView
from .views import CreateTaskView, UpdateTask, TaskDetail, DeleteTask,TodayView, CompletedTasksView, LabelsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('features/', FeaturesPageView.as_view(), name='features'),
    path('webapp/', WebappPageView.as_view(), name='webapp'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('add_task/', CreateTaskView.as_view(), name='create_task'),
    path('labels/', LabelsView.as_view(), name='labels'),
    path('completed_tasks/', CompletedTasksView.as_view(), name='completed_tasks'),
    path('update_task/<slug:slug>/', UpdateTask, name='update_task'),
    path('task_detail/<slug:slug>/', TaskDetail, name='task_detail'),
    path('delete_task/<slug:slug>/', DeleteTask, name='delete_task'),
    path('today/', TodayView.as_view(), name='today'),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
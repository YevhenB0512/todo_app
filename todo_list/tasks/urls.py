from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='tasklist'),
    path('task/<int:pk>', views.task_detail, name='task'),
    path('task-create/', views.task_create, name='create'),
    path('task-edit/<int:task_id>', views.task_update, name='task_edit'),
    path('task-delete/<int:task_id>', views.task_delete, name='task_delete'),
]
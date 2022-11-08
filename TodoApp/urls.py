from django.urls import path
from .views  import *


app_name="TodoApp"
urlpatterns = [
    path("create/", TaskCreateView.as_view(), name='task-create'),
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailViews.as_view(), name='task-details'),
    path('update/<int:pk>/', TaskUpdateViews.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteViews.as_view(), name='task-delete')
]
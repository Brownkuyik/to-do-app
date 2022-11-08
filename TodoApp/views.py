#this part of the views explains only the generic views of django which is more useful if u dont have enough time to complete or to work with main views
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView #this is the view to be used while working on it first
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
# Create your views here.
# today we want to talk about generic views and how it can be used.
#if u inherit a function based view you still need to used function to declare it.


class TaskCreateView(CreateView):
    form_class = TaskForm #this is the form class we create for the task creation
    template_name = 'TodoApp/task_create.html' #here you call the template u want to used while creating the page for the project
    success_url = reverse_lazy("TodoApp:task-list")


class TaskListView(ListView): #look up for where the listview comes from before coding further
    #a generic views for ListViews, you need quaryset, tempalte name and context_object_name which wil be what you call at the template.
    queryset = Task.objects.all()
    template_name = 'TodoApp/task_list.html'
    context_object_name = 'tasks'

#to show the details of the task you created, you import detailsview from django genetic details.
from django.views.generic.detail import DetailView
# then declare or call it class
class TaskDetailViews(DetailView):
    model = Task
    template_name = 'TodoApp/task_list.html'

# for an update views, you need to import for edit in generic
from django.views.generic.edit import UpdateView, DeleteView

class TaskUpdateViews(UpdateView):
    model = Task
    template_name = 'TodoApp/task_update.html'
    fields = "__all__"
    success_url = reverse_lazy("TodoApp:task-list")

# in line 32, deleteview was already imported
class TaskDeleteViews(DeleteView):
    model = Task
    template_name = 'TodoApp/task_confirm_delete.html'
    success_url = reverse_lazy("TodoApp:task-list")
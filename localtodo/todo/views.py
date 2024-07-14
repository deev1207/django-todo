from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import ToDoItem
from todo.forms import ToDoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
class ToDoListView(LoginRequiredMixin, generic.ListView):
    model = ToDoItem
    context_object_name = 'todoitem_list'
    template_name = 'todo/todoitem_list.html'
    def get_queryset(self):
        return self.request.user.todos.all()

@login_required
def CreateToDoView(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo-list')

    else:
        form = ToDoForm()

    return render(request, 'todo/create.html', {'form': form})

def Update(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo-list')

    else:
        form = ToDoForm(instance=item)

    return render(request, 'todo/create.html', {'form': form})

def Delete(request,pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('todo-list')
    return render(request, 'todo/todoitem_confirm_delete.html')


class ToDoUpdate(UpdateView):
    model = ToDoItem
    form_class = ToDoForm
    # Not recommended (potential security issue if more fields added)
    success_url = reverse_lazy('todo-list')

class ToDoDelete(DeleteView):
    model = ToDoItem
    # Not recommended (potential security issue if more fields added)
    success_url = reverse_lazy('todo-list')

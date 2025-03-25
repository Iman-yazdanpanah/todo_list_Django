
# In myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib.auth import login
from .forms import SignUpForm, TodoForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    
    return render(request, 'myapp/todo_list.html', {
        'todos': todos, 
        'form': form
    })

@login_required
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.complete = not todo.complete
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')
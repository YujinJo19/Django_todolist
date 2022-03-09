from django.shortcuts import render, redirect
from .models import Todo



def index(request):

    todo = Todo.objects.all()

    context = {
        'todo': todo,
    }
    return render(request, 'todo_lists/index.html', context)


def new(request):
    return render(request, 'todo_lists/new.html')



def create(requset):
    
    content = requset.POST.get('content')
    todo = Todo(content=content)
    todo.save()

    return redirect('todo_lists:index')


def delete(request, pk):

    todo = Todo.objects.get(pk=pk)
    todo.delete()
    
    return redirect('todo_lists:index')
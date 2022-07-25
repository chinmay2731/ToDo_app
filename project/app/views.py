from django.shortcuts import render,redirect
from.models import todo
from.forms import TodoForm

# Create your views here.

def index(request):
    todo_list = todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    index = {'todoapp':todo_list, 'form':form}
    return render(request,'todo_list.html', index)

def update_data(request,pk):
    list = todo.objects.get(id=pk)
    form = TodoForm(instance=list)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=list)
        if form.is_valid():
            form.save()
            return redirect('/')
    update = {'form':form}
    return render(request,'todo_update.html', update)

def delete_data(request,pk):
    todo_delete = todo.objects.get(id=pk)
    if request.method == 'POST':
        todo_delete.delete()
        return redirect('/')
    delete = {'todo_delete':todo_delete}
    return render(request,'todo_delete.html',delete)


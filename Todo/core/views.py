from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import now


# Create your views here.


def index(request):
    return render(request, 'index.html')

def addtodo(request):
    form = TodoForm(request.POST or None, request.FILES or None)
    context = {
        'form':form,
    }
    if request.method == 'GET':
        todos = Todo.objects.all().order_by('-created_date')

        page = request.GET.get('page',1)
        paginator = Paginator(todos, 5)

        try:
            todos = paginator.page(page)
        except PageNotAnInteger:
            todos = paginator.page(1)
        except EmptyPage:
            todos = paginator.page(paginator.num_pages)


        context['todos'] = todos
        return render(request, 'addtodo.html', context)


    elif request.method == 'POST':

        if form.is_valid():
            form.save()
            todos = Todo.objects.all().order_by('-created_date')
            context['todos'] = todos

        return redirect('core:addtodo')

def complete(request,id):

    todo = Todo.objects.get(id = id)
    if todo.status:
        todo.status = False
        todo.completed_date = None
    else:
        todo.status = True
        todo.completed_date = now()
    todo.save()
    return redirect('core:addtodo')


def edit(request, id):

    todo = Todo.objects.get(id = id)

    form = TodoForm(request.POST or None, request.FILES or None, instance=todo)

    if request.method == 'GET':

        context = dict()
        context['form'] = form


        return render(request, 'addtodo.html', context)
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:addtodo')


    return redirect('core:addtodo')

def delete(request, id):

    todo = Todo.objects.get(id = id)
    todo.delete()

    return redirect('core:addtodo')


def mytodos (request):
    
    todos = Todo.objects.all().order_by('-status', 'created_date')
    page = request.GET.get('page',1)
    paginator = Paginator(todos, 5)

    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)


    context = {}
    context['todos'] = todos

    return render(request, 'mytodos.html',context)
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
def todopage(request):
    todo_items = Todo.objects.all().order_by("added_date")
    
    return render(request, 'polls/index.html', {
        "todo_items":todo_items,
    })

def add_todo(request):
    current_date = timezone.now()
    if request.POST["content"]:
        content = request.POST["content"]
        Todo.objects.create(added_date=current_date, text = content)
        length_of_todos = Todo.objects.all().count()
    
        return HttpResponseRedirect("/")
    else:
        messages.error(request, "Your input field is empty!")
        return HttpResponseRedirect("/")
        

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

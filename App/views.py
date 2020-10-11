from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from App.models import Todo, complete
from django.http import HttpResponseRedirect

# Create your views here.
def base(request):
    todo_item = Todo.objects.all().order_by("-added_date")
    complete_item = complete.objects.all().order_by("-complete_date")
    return render(request, 'App/index.html', { "todo_item": todo_item , "complete_item": complete_item})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date , text=content)
    print(created_obj)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    print(Todo.objects.all())
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

@csrf_exempt
def complete_todo(request, todo_id):
    current_date = timezone.now()
    complete_id = Todo.objects.get(id=todo_id)
    complete_content = complete_id.text
    print(complete_content)
    complete_obj = complete.objects.create(complete_date=current_date , text=complete_content)
    print(complete.objects.all())
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_complete(request, complete_id):
    complete.objects.get(id=complete_id).delete()
    return HttpResponseRedirect("/")

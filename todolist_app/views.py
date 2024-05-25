from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {
        'welcome_text':"Welcome from Jinja2."
        }
    return render(request, 'todolist.html', context)
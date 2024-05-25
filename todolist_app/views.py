from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {
        'welcome_text':"Welcome todo list page."
        }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'contact_text':"Welcome to the contact page."
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome to the about page."
        }
    return render(request, 'about.html', context)

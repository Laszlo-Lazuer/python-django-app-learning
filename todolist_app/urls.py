from django.urls import path
from todolist_app import views

urlpatterns = [
    path("", views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about-us', views.about, name='about')
]

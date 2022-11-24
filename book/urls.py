from django.urls import path, reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book 

app_name = 'book'
urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
    path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse_lazy('book:list')), name='delete')
]

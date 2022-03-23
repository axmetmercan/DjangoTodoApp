from distutils.command.upload import upload
from unicodedata import name
from django import views
from django.utils.timezone import now

from django.urls import path, include
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/todo/', views.addtodo, name='addtodo' ),
    path('myoldtodos/', views.mytodos, name='mytodos'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('complete/<int:id>', views.complete, name='complete'),

]

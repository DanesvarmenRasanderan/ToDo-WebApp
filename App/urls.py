from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
    path('complete_todo/<int:todo_id>/', views.complete_todo),
    path('delete_complete/<int:complete_id>/', views.delete_complete),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name="tasks"),
    path('edit_tasks/<str:pk>/', views.editTask, name="edit_task"),
    path('notes/', views.notes, name="notes"),
    path('accounts/', views.accounts, name="accounts"),
]
from django.urls import path
from tasks.views import TaskList

urlpatterns = [
    path('', view=TaskList.as_view(), name='task-list'),
]

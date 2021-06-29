from django.urls import path
from tasks.views import TaskAPIView

urlpatterns = [
    path('tasks/', view=TaskAPIView.as_view(), name='tasks'),
    path('tasks/<str:pk>/', view=TaskAPIView.as_view(), name='tasks'),
]

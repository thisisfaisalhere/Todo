from django.urls import path
from tasks.views import TaskAPIView

urlpatterns = [
    path('', view=TaskAPIView.as_view(), name='tasks'),
    path('<str:pk>/', view=TaskAPIView.as_view(), name='tasks'),
]

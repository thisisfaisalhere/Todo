from datetime import datetime
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import UserTaskSerializer
from .models import UserTask

class TaskList(generics.ListAPIView):
  serializer_class = UserTaskSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    query = UserTask.objects.filter(user=self.request.user, date=datetime.now().date())
    return query
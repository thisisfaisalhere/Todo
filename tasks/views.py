from django.http import Http404
from rest_framework import status, permissions, views
from rest_framework.response import Response
from .serializers import UserTaskSerializer
from .models import UserTask

class TaskAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return UserTask.objects.get(pk=pk, user=user)
        except UserTask.DoesNotExist:
            raise Http404

    def add_user_to_data(self, data, user):
      data['user'] = user.id
      return data

    def get(self, request, format=None):
        tasks = UserTask.objects.filter(user=request.user)
        serializer = UserTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = self.add_user_to_data(data=request.data, user=request.user)
        serializer = UserTaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        tasks = self.get_object(pk=pk, user=request.user)
        data = self.add_user_to_data(data=request.data, user=request.user)
        serializer = UserTaskSerializer(tasks, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk=pk, user=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
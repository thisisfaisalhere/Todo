from django.db import models
from django.db.models import fields
from rest_framework import serializers
from tasks.models import UserTask

class UserTaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTask
    fields = '__all__'
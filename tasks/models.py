from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
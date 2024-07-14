from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ToDoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def get_absolute_url(self):
        return reverse('edit', args=[str(self.id)])

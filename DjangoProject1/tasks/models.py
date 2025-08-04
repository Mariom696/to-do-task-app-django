from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Skipped', 'Skipped'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='task_images/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    # assigned_to = models.ForeignKey( on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

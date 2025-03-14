from django.db import models

from django.contrib.auth.models import User

class TaskModel(models.Model):

    task_name=models.CharField(max_length=50,null=True)

    created_date=models.DateField(auto_now_add=True,null=True)

    is_completed=models.BooleanField(default=False,null=True)

    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    priority=[
        ('high','high'),

        ('medium','medium'),

        ('low','low')
    ]

    priority_level=models.CharField(max_length=100,choices=priority,null=True)

    due_date=models.DateField(null=True)

    





from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    #status option
    class TaskStatus(models.TextChoices):
        TODO = 'todo', _('Todo')
        IN_PROGRESS = 'in_progress', _('In Progress')
        CLOSED = 'closed', _('Closed')

    #define clomn
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #define table name
        db_table = 'tasks'
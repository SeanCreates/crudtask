from django.db import models

class Task(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    DueDate = models.DateField()
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title

# Create your models here.

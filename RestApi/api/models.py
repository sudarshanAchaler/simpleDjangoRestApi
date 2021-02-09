from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        temp= str(self.user) + '-' + str(self.title)
        return temp
    
from django.db import models

# Create your models here.
# Add the Finch class & list and view function below the imports

class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
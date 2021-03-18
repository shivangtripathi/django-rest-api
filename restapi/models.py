from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(("task"), max_length=50)
    status = models.BooleanField(("completed"),default=False,blank=True,null=True)

    def __str__(self):
        return self.title


    
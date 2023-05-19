from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.TextField()
    
    def __str__(self):
        return self.name
    
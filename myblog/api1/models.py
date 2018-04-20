from django.db import models


class Blog (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
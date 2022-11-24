from django.db import models

# Create your models here.   
class AiModel(models.Model):
    ai_file = models.FileField(blank=True)
    version = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.version
    

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    isCorrect = models.BooleanField(default=True)
    version = models.CharField(max_length=10)

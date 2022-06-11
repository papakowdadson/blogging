from email.policy import default
from sqlite3 import Date
from django.db import models
from django.forms import SlugField

# Create your models here.
class Articles(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField()
    Slug=models.SlugField()
    Date=models.DateTimeField(auto_now_add='True')
    Thumb = models.ImageField(default='default.png',blank=True)
    #others would be added later
    def __str__(self):
     return self.Title

    def BodySnipet(self):
        return self.Body[:70]+"..."
      

    



from email.policy import default
from sqlite3 import Date
from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField()
    Slug=models.SlugField()
    Date=models.DateTimeField(auto_now_add='True')
    Thumb = models.ImageField(default='default.png',blank=True)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    #others would be added later
    def __str__(self):
     return self.Title

    def BodySnipet(self):
        return self.Body[:70]+"..."
      

    



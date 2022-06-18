from django.db import models


from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    author = models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('date published')# Create your models here.

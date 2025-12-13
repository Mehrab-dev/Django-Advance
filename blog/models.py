from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# create model class 
class Post(models.Model) :
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Category(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
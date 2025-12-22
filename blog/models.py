from django.db import models
# from django.contrib.auth import get_user_model
from django.urls import reverse

# user = get_user_model()

# create model class 
class Post(models.Model) :
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self) :
        return self.content[0:3]
    
    def get_absolute_api_url(self) :
        return reverse('blog:api_v1:post_detail',kwargs={'pk':self.pk})
    
class Category(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
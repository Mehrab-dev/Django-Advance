from django.contrib import admin
from blog.models import Post , Category


class PostAdmin(admin.ModelAdmin) :
    list_display = ['title','author','status','created_date','published_date']


admin.site.register(Category)
admin.site.register(Post,PostAdmin)
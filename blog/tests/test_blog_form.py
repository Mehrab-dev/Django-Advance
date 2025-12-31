from django.test import TestCase
from blog.forms import PostForm
from accounts.models import User
from blog.models import Category
from datetime import datetime

class TestPostForm(TestCase) :

    def test_post_form_with_valid_data(self) :
        author_obj = User.objects.create(email='test@gmail.com')
        category_obj = Category.objects.create(name='one')
        form = PostForm(data={
            'author':author_obj.id,
            'title':'test',
            'content':'description',
            'status':True,
            'category':category_obj.id,
            'published_date':datetime.now()
        })

        self.assertTrue(form.is_valid())


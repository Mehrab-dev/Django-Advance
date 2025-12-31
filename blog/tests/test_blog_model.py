from django.test import TestCase
from blog.models import Post , Category
from accounts.models import User , Profile
from datetime import datetime

class TestPostModel(TestCase) :
    def setUp(self) :
        self.user = User.objects.create(email='test@gmail.com',password='Mm20399990')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'mehrab',
            last_name = 'khan',
            description = 'testtt'
        )


    def test_post_model_with_valid_data(self) :
        
        post = Post.objects.create(
            title = 'test',
            content = 'description',
            status = True,
            category = None ,
            author = self.profile ,
            published_date = datetime.now()
        )

        self.assertTrue(Post.objects.filter(pk=post.id).exists())
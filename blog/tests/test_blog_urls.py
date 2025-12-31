from django.test import TestCase
from django.urls import resolve , reverse
from ..views import IndexView , PostListView , PostDetail

# Create your tests here.


class TestUrl(TestCase) :

    def test_blog_index_url_resolve(self) :
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class,IndexView)

    def test_blog_pos_list_url_resolve(self) :
        url = reverse('blog:list_posts')
        self.assertEqual(resolve(url).func.view_class,PostListView)

    def test_blog_post_detail_url_resolve(self) :
        url = reverse('blog:detail_post',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,PostDetail)

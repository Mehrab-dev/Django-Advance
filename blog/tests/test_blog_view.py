# from django.test import TestCase , Client
# from django.urls import reverse

# class TestBlogViews(TestCase) :
#     def setUp(self):
#         self.client = Client()

#     def test_blog_index_url_respone_200(self) :
#         url = reverse('blog:index')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code,200)
#         self.assertTrue(str(response.content).find('index'))
#         self.assertTemplateUsed(response,template_name='index.html')

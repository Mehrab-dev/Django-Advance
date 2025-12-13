from django.shortcuts import render
from blog.models import Post
from django.views.generic.base import TemplateView , RedirectView
from django.views.generic import ListView , DetailView

# create the class base views
class IndexView(TemplateView) :
    template_name = 'index.html'

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'mehrab'
        context["post"] = Post.objects.all()
        return context

class RedirectView(RedirectView) :
    url = 'https://maktabkhooneh.org/'



class PostListView(ListView) :
    # model = Post
    # queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = ['-created_date']

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts 


class PostDetail(DetailView) :
    model = Post
    context_object_name = 'post'
    
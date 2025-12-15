from django.urls import path , include
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('redirect/',views.RedirectView.as_view(),name='redirect'),
    path('posts/',views.PostListView.as_view(),name='list_posts'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='detail_post'),
    path('create_post/',views.CreatePost.as_view(),name='create_post'),
    path('update/post/<int:pk>/',views.UpdatePostView.as_view(),name='update_post'),
    path('delete/post/<int:pk>/',views.DeletePostView.as_view(),name='delete_post'),

    path('api/v1/',include('blog.api.v1.urls'),name='post_api')
]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('redirect/',views.RedirectView.as_view(),name='redirect'),
    path('posts/',views.PostListView.as_view(),name='list_posts'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='detail_post')
]
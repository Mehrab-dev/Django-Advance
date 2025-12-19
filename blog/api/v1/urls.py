from django.urls import path
from . import views

app_name = 'api_v1'

urlpatterns = [
    # path('post/',views.api_post_list,name='post_api'),
    # path('post/<int:pk>/',views.api_postdetail,name='api_post_detail'),
    # path('post/',views.PostList.as_view(),name='post_list'),
    # path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail')

    # path('post/',views.PostViewSet.as_view({'get':'list'}),name='post-list'),
    # path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve'}),name='post-detail')

    path('post/',views.PostModelViewSet.as_view({'get':'list','post':'create'}),name='post_view_model_set'),
    path('post/<int:pk>/',views.PostModelViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),

    path('category/',views.CategoryModelViewSet.as_view({'get':'list','post':'create'}),name='category_models_view_set'),
    path('category/<int:pk>/',views.CategoryModelViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))

]
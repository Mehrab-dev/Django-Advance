from django.urls import path
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('post/',views.api_post_list,name='post_api'),
    path('post/<int:pk>/',views.api_postdetail,name='api_post_detail')

]
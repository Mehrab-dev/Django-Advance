from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from accounts.models import User
from datetime import datetime
from blog.models import Category


@pytest.fixture
def common_user() :
    user = User.objects.create_user(
        email = 'test@gmail.com',
        password='Mm20399990'
    )
    return user

@pytest.fixture
def cat(db) :
    category = Category.objects.create(name='meeting')
    return category

@pytest.fixture
def api_client() :
    client = APIClient()
    return client



@pytest.mark.django_db
class TestPostApi :

    # def test_get_post_response_200(self) :
    #     user = User.objects.create_user(
    #         email ='test@gmail.com',
    #         password = 'Mm20399990'
    #     )
    #     client = APIClient()
    #     client.force_authenticate(user=user)
    #     url = reverse('blog:api_v1:post_view_model_set')
    #     response = client.get(url)
    #     assert response.status_code == 200

    def test_create_post_response_201(self,api_client,common_user,cat) :
        url = reverse('blog:api_v1:post_view_model_set')
        data = {
            'title' : 'test',
            'content' :'decription' ,
            'status' : True ,
            'category' : cat.name ,
            'published_date' : datetime.now()
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201 
    
    def test_create_post_response_401(self,api_client,cat) :
        url = reverse('blog:api_v1:post_view_model_set')
        data = {
            'title' : 'test',
            'content' :'decription' ,
            'status' : True ,
            'category' : cat.name ,
            'published_date' : datetime.now()
        }
        
        response = api_client.post(url,data)
        assert response.status_code == 401

    def test_create_post_invalid_data_response_400(self,api_client,common_user) :
        url = reverse('blog:api_v1:post_view_model_set')
        data = {
            'title' : 'test',
            'content' : 'yes'
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        return response.status_code == 400
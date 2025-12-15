from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def api_post_list(request) :
    posts = Post.objects.all()
    serializer = PostSerializers(posts,many=True)
    return Response(serializer.data)

@api_view()
def api_postdetail(request,pk) :
    # post = get_object_or_404(Post,pk=pk)
    # serializer = PostSerializers(post)
    # return Response(serializer.data)

    try :
        post = Post.objects.get(pk=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)
    except Post.DoesNotExist :
        return Response({"detail":"post does not exists"},status=404)
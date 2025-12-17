from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
def api_post_list(request) :
    if request.method == 'GET' :
        posts = Post.objects.all()
        serializer = PostSerializers(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.errors)



@api_view(["GET","PUT","DELETE"])
def api_postdetail(request,pk) :
    # post = get_object_or_404(Post,pk=pk)
    # serializer = PostSerializers(post)
    # return Response(serializer.data)


    try :
        if request.method == 'GET' :
            post = Post.objects.get(pk=pk)
            serializer = PostSerializers(post)
            return Response(serializer.data)
        elif request.method == 'PUT' :
            post = Post.objects.get(pk=pk)
            serializer = PostSerializers(post,data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response(serializer.errors)
        elif request.method == "DELETE" :
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist :
        return Response({"detail":"post does not exists"},status=404)
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404

# import for classbaseviews
from rest_framework.views import APIView


"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
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
"""

class PostList(APIView) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    def get(self,request) :
        posts = Post.objects.filter(status=True)
        serializer = PostSerializers(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request) :
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.errors)

"""
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
"""

class PostDetail(APIView) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers

    def get(self,request,pk) :
        try :
            post = Post.objects.get(pk=pk)
            serializer = self.serializer_class(post)
            return Response(serializer.data)
        except Post.DoesNotExist :
            return Response({"detail":"post does not exists"},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk) :
        try :
            post = Post.objects.get(pk=pk)
            serializer = self.serializer_class(post,data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response(serializer.errors)
        except Post.DoesNotExist:
            return Response({"detail":"post does not exists"})
    
    def delete(self,request,pk) :
        try :
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist :
            return Response({"detail":"post does not exists"})

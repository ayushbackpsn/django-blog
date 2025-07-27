from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BogPost
from .serializer import BogPostSerializer
from django.shortcuts import render


@api_view(['GET', 'POST'])
def blog_list_create(request):
    if request.method == 'GET':
        posts = BogPost.objects.all()
        serializer = BogPostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    try:
        post = BogPost.objects.get(pk=pk)
    except BogPost.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BogPostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BogPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

def index_view(request):
    return render(request, 'blogupload/index.html')






# Create your views here.

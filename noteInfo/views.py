from django.shortcuts import render
from noteInfo.models import Blog
from noteInfo.Serializers import Blogserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def blog(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = Blogserializers(blog, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = Blogserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def blog_details(request,slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = Blogserializers(blog)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = Blogserializers(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# search on the database for a specific word
@api_view(['GET'])
def search_blog(request):
    query = request.query_params.get("search")
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
    serializer = Blogserializers(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
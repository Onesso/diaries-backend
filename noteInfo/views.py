from django.shortcuts import render
from noteInfo.models import Blog
from noteInfo.serializers import Blogserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
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
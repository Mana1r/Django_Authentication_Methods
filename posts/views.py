from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework_api_key.permissions import HasAPIKey
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from django.contrib.auth.mixins import LoginRequiredMixin



class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [HasAPIKey]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostCreateView(LoginRequiredMixin, generics.CreateAPIView):
class PostCreateView( generics.CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session['username'] = username
#             request.session.save()
#         else:


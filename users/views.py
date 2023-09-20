from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404

from rest_framework.views import View, APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, PostSerializer
from .serializers import MyTokenObtainPairSerializer
from .models import User, Post, Follow


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        if request.data.get("all"):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                BlacklistedToken.objects.get_or_create(token=token)
            return Response(status=status.HTTP_205_RESET_CONTENT)

        else:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)


class CreatePostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(id=int(pk))
        except User.DoesNotExist:
            raise Http404()

    def post(self, request, pk):
        follower = self.request.user
        following = self.get_object(pk)
        if Follow.objects.filter(follower=follower, following=following).exists():
            return ValidationError(f"already following {following}")
        new_follow = Follow.objects.create(follower=follower, following=following)
        return Response(
            f"{follower} followed {following}", status=status.HTTP_201_CREATED
        )

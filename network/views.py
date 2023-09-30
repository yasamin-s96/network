from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import View, APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserSerializer,
    PostSerializer,
    LikeSerializer,
    CommentSerializer,
)
from .serializers import MyTokenObtainPairSerializer
from .models import *


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


class PostViewSet(GenericViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in ["retrieve", "all_posts"]:
            return Post.objects.all()
        elif self.action == "following_posts":
            following_authors = Follow.objects.filter(follower=self.request.user)
            following_ids = following_authors.values_list("following_id", flat=True)
            return Post.objects.filter(author_id__in=following_ids)
        else:
            return Post.objects.filter(author=self.request.user)

    @action(detail=False, permission_classes=[AllowAny])
    def all_posts(self, request):
        if not self.get_queryset():
            return Response(
                {"all_posts": "No Posts found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def following_posts(self, request):
        if not self.get_queryset():
            return Response(
                {"following_posts": "No Posts found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        post = get_object_or_404(self.get_queryset(), pk=pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        post = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(post, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(post, serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404()

    def post(self, request, pk):
        follower = self.request.user
        following = self.get_object(pk)
        if Follow.objects.filter(follower=follower, following=following).exists():
            return Response(
                f"already following {following}", status=status.HTTP_400_BAD_REQUEST
            )
        new_follow = Follow.objects.create(follower=follower, following=following)
        return Response(f"following {following}", status=status.HTTP_201_CREATED)

    def delete(self, requset, pk):
        follower = self.request.user
        following = self.get_object(pk)
        record = Follow.objects.filter(follower=follower, following=following)
        if record.exists():
            record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            f"not following {following}", status=status.HTTP_400_BAD_REQUEST
        )


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404()

    def post(self, request, pk):
        user = self.request.user
        post = self.get_post(pk)
        try:
            Like.objects.create(user=user, post=post)

        # if the user tries to like the same post again, IntegrityError raises due to the model's set constraint.
        except IntegrityError:
            return Response(
                "You've already liked this post", status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = self.request.user
        post = self.get_post(pk)
        record = Like.objects.filter(user=user, post=post)
        if record.exists():
            record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                "You have not already liked this post",
                status=status.HTTP_400_BAD_REQUEST,
            )


class CommentViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        serializer.save(user=self.request.user, post=post)

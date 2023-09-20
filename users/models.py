from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.db import models


class User(AbstractUser):
    pk = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.username


class Follow(models.Model):
    following = models.OneToOneField(
        User, related_name="following", on_delete=models.CASCADE, db_index=True
    )
    follower = models.OneToOneField(
        User, related_name="follower", on_delete=models.CASCADE, db_index=True
    )
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("following", "follower")


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

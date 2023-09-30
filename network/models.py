from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.db import models


class User(AbstractUser):
    fullname = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True, null=True)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.username


class Follow(models.Model):
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE, db_index=True
    )
    follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE, db_index=True
    )
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("following", "follower")

    def __str__(self):
        return f"{self.follower} is following {self.following}"


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

    def __str__(self):
        return f"{self.user} liked post {self.post.id}"


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s comment on post {self.post.id}"

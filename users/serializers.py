import re
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username

        return token


class UserSerializer(serializers.ModelSerializer):
    confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "fullname", "email", "password", "confirmation"]

    # custom validation
    def validate(self, data):
        # username validation: It must start with a letter and end with a letter or number.
        # the middle part can be alphanumeric [a-zA-z0-9._]
        if not re.match(r"[a-zA-z]\w*[a-zA-z0-9]", data["username"]):
            raise serializers.ValidationError("Invalid username format")

        # password validation
        if data["password"] != data["confirmation"]:
            raise serializers.ValidationError("Passwords do not match")

        # remove confirmation field so that it doesn't get sent to the create()
        data.pop("confirmation", None)

        # password format check
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                "Password length is less than 8 characters"
            )
        elif not re.search(r"[a-z]", data["password"]):
            raise serializers.ValidationError("Must contain lowercase character")
        elif not re.search(r"[A-Z]", data["password"]):
            raise serializers.ValidationError("Must contain uppercase character")
        elif not re.search(r"[0-9]", data["password"]):
            raise serializers.ValidationError("Must contain one digit")
        elif not re.search(r"[_@$]", data["password"]):
            raise serializers.ValidationError("Must contain one of the (_, @, $)")

        return data


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

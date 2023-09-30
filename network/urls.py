from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")

comment_router = routers.NestedDefaultRouter(router, "posts", lookup="post")
comment_router.register("comments", views.CommentViewSet)

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
    path("", include(comment_router.urls)),
    path("<int:pk>/follow/", views.FollowView.as_view(), name="follow"),
    path("posts/<int:pk>/like/", views.LikeView.as_view(), name="like"),
    # path("posts/<int:pk>/comment/", views.CommentViewSet.as_view({"get": "list"})),
    # path("posts/<int:pk>/comment/", views.CommentViewSet.as_view({"post": "create"})),
    # path("posts/<int:pk>/comment/", views.CommentViewSet.as_view({'post':'create'})),
]

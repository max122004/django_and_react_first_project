from django.urls import path

from posts.views import PostsListAPIView, PostsDetailAPIView, PostsCreateAPIView, PostsDetailUpdateAPIView, \
    LikeCreateAPIView, ShareCreateAPIView, CommentCreateAPIView, LikeDeleteAPIView, ShareDeleteAPIView, \
    CommentUpdateAPIView

urlpatterns = [
    path('list/', PostsListAPIView.as_view()),
    path('detail/', PostsDetailAPIView.as_view()),
    path('<int:pk>/', PostsDetailUpdateAPIView.as_view()),
    path('create/', PostsCreateAPIView.as_view()),
    path('create/like/', LikeCreateAPIView.as_view()),
    path('create/share/', ShareCreateAPIView.as_view()),
    path('create/comment/', CommentCreateAPIView.as_view()),
    path('delete/like/', LikeDeleteAPIView.as_view()),
    path('delete/share/', ShareDeleteAPIView.as_view()),
    path('update/comment/', CommentUpdateAPIView.as_view()),
]
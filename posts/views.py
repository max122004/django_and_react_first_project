from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from permissions import IsAuthorOrReadOnly
from posts.models import Posts, Like, Share, Comment
from posts.serializer import PostsListSerializer, PostsDetailSerializer, LikeSerializer, ShareSerializer, \
    PostsCreateSerializer, PostsDetailUpdateSerializer, CommentSerializer, CommentUpdateSerializer, \
    CommentCreateSerializer


class PostsListAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsListSerializer

    def get(self, request, *args, **kwargs):
        posts_category = request.GET.get('category', None)
        posts_name = request.GET.get('name', None)
        posts_text = request.GET.get('text', None)

        queryset = self.get_queryset()

        if posts_category:
            queryset = queryset.filter(category__name__icontains=posts_category)
        if posts_name:
            queryset = queryset.filter(title__icontains=posts_name)
        if posts_text:
            queryset = queryset.filter(text__icontains=posts_text)

        response_data = []
        for post in queryset:
            post_data = self.serializer_class(post).data

            likes = Like.objects.filter(posts=post)
            like_serializer = LikeSerializer(likes, many=True)
            post_data['likes'] = like_serializer.data

            shares = Share.objects.filter(posts=post)
            share_serializer = ShareSerializer(shares, many=True)
            post_data['shares'] = share_serializer.data

            response_data.append(post_data)

        return Response(response_data)


class PostsDetailAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['text'] #?text=
    search_fields = ['title, text'] #?search=
    ordering_fields = ['created'] #?ordering=created/-created - в обратном порядке

    def get_queryset(self):
        user = self.request.user  # Получаем аутентифицированного пользователя
        return Posts.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        response_data = []
        for post in queryset:
            post_data = self.serializer_class(post).data

            likes = Like.objects.filter(posts=post)
            like_serializer = LikeSerializer(likes, many=True)
            post_data['likes'] = like_serializer.data

            shares = Share.objects.filter(posts=post)
            share_serializer = ShareSerializer(shares, many=True)
            post_data['shares'] = share_serializer.data

            response_data.append(post_data)

        return Response(response_data)


class PostsDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class PostsCreateAPIView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, image=self.request.FILES.get('image'))


class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDeleteAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class ShareCreateAPIView(CreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShareDeleteAPIView(CreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()
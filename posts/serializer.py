from rest_framework import serializers

from authentication.models import User
from posts.models import Posts, Comment, Like, Share


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'image']  # Добавьте 'avatar' сюда, если у вас есть поле для изображения


class PostsListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UserSerializer(read_only=True)
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    shares_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'title', 'text', 'author', 'created', 'category', 'comments', 'image', 'likes_count', 'shares_count', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_shares_count(self, obj):
        return obj.shares.count()


class PostsDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    shares_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'title', 'text', 'author', 'created', 'category', 'comments', 'image', 'likes_count', 'shares_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_shares_count(self, obj):
        return obj.shares.count()


class PostsDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'text', 'image']


class PostsCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Posts
        fields = ['title', 'text', 'image']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Like
        fields = ['user', 'posts', 'created']


class ShareSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Share
        fields = ['user', 'posts', 'created']


class LikeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id']


class ShareDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['id']


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['author', 'posts', 'text']


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']
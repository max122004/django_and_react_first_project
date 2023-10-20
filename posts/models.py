from django.db import models

from authentication.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Posts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='logos/', default=1)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f'Id {self.id} - {self.title}'

class Comment(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="comments")
    created = models.DateField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ['user', 'posts']


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='shares')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Репост'
        verbose_name_plural = 'Репосты'
        unique_together = ['user', 'posts']

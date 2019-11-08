from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(max_length=2500, blank=True, db_index=True)
    img1 = models.ImageField(blank=True, null=True, upload_to='media/blog')
    img2 = models.ImageField(blank=True, null=True, upload_to='media/blog')
    img3 = models.ImageField(blank=True, null=True, upload_to='media/blog')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    maxResolution = models.CharField(max_length=200, blank=True)
    maxExcerpt = models.PositiveIntegerField(default = 0)
    megapixels = models.PositiveIntegerField(default = 2)
    rating = models.FloatField(default = 3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, db_index=True)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField(blank=True, null = True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,  null = True)
    updated = models.DateTimeField(auto_now=True, null = True)
    rating = models.FloatField(default = 0)
    product = models.ForeignKey(Product, related_name='blog_posts', blank = True, null = True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

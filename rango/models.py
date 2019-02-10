from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

# Category inherits from Model
# Each of these classes are really tables in the database
# python manage.py sqlmigrate rango 0001 to view underlying sql
# migration is a fancy term for sql_create
name_max_length = 128  # Instead of repeating max length.


class Category(models.Model):

    name = models.CharField(max_length=name_max_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=name_max_length, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, default='null')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    # This is toString()
    def __str__(self):
        return self.title


class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username

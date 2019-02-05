from django.template.defaultfilters import slugify
from django.db import models

# Category inherits from Model
# Each of these classes are really tables in the database
# python manage.py sqlmigrate rango 0001 to view underlying sql
# migration is a fancy term for sql_create


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
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
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, default='null')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    # This is toString()
    def __str__(self):
        return self.title


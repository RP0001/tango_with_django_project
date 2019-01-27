from django.db import models

# Category inherits from Model
# Each of these classes are really tables in the database
# python manage.py sqlmigrate rango 0001 to view underlying sql
# migration is a fancy term for sql_create

class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # This is toString()
    def __str__(self):
        return self.title


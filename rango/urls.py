from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #assume rango part is already cut
    url(r'^about/', views.about, name='about'), #add url pattern for about page
]

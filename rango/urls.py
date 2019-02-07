from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #assume rango part is already cut
    url(r'^about/', views.about, name='about'), #add url pattern for about page
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.show_page, name='show_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),

]

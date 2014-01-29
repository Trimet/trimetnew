from django.conf.urls import patterns, url

from catalog import views

urlpatterns = patterns('',
    url(r'^$', views.show_index, name='index'),


)

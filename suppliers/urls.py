from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('',
    url(r'^$', views.show_index, name='index'),
    url(r'^history/$', views.show_history, name='history'),
    url(r'^wordpress/photo/$', views.show_photo, name='photo'),
    url(r'^leaderships/$', views.show_leadership, name='leaderships'),
    url(r'^strong/$', views.show_strong, name='strong'),
    url(r'^awards/$', views.show_awards, name='awards'),
    url(r'^wordpress/$', views.show_wordpress, name='wordpress'),
    url(r'^partners/$', views.show_partners, name='partners'),
    url(r'^vacancies/$', views.show_vacancies, name='vacancies'),

)

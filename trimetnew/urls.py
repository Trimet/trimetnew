from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mainpage.views import show_index

urlpatterns = patterns('',

    url(r'^$', show_index, name='home'),
    url(r'^about/', include('about.urls', namespace="about")),

    url(r'^products/', include('products.urls', namespace="products")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^suppliers/', include('suppliers.urls', namespace="suppliers")),
    url(r'^contacts/', include('contacts.urls', namespace="contacts")),
    url(r'^catalog/', include('catalog.urls', namespace="catalog")),
    url(r'^kabinet/', include('kabinet.urls', namespace="kabinet")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import url
from Crawlers.views import load_sources

urlpatterns = [
    url(r'^Search/$', load_sources, name="load_sources"),
]

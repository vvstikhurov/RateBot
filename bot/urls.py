from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rate/(?P<pair>\w+)$', views.rate, name='rate'),
]
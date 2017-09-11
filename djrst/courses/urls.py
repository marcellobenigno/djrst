from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_, name='list'),
    url(r'^(?P<pk>\d+)/detalhe$', views.detail, name='detail'),
]

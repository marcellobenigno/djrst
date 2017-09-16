from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from .courses import views

router = routers.SimpleRouter()
router.register(r'cursos', views.CourseViewSet)
router.register(r'avaliacoes', views.ReviewViewSet)

urlpatterns = [
    url(r'^', include('djrst.core.urls', namespace='core')),
    url(r'^cursos/', include('djrst.courses.urls', namespace='courses_list')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/cursos/', include('djrst.courses.urls_api', namespace='courses')),
    url(r'^api/v2/', include(router.urls, namespace='apiv2')),

    url(r'^admin/', admin.site.urls),
]

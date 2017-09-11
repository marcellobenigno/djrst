from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('djrst.core.urls', namespace='core')),
    url(r'^cursos/', include('djrst.courses.urls', namespace='courses')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/cursos/', include('djrst.courses.urls_api', namespace='courses_api')),

    url(r'^admin/', admin.site.urls),
]

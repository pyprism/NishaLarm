from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from alarm import views


router = routers.DefaultRouter()
router.register(r'api', views.ApiViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hiren.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'alarm.views.test'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

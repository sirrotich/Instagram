from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
     url(r'^home/$', views.home, name='home'),
    url(r'^$',views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
]
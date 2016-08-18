from django.conf.urls import url
from zazzapp import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    url(r'^user/$', views.User.as_view(), name='user'),
    url(r'^shout/$', views.Shout.as_view(), name='shout'),
    url(r'^login/', drf_views.obtain_auth_token),
]

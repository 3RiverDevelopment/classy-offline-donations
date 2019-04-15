from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.core_login, name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^enable-user', views.enable_user, name='enable_user'),
    url(r'^donate', views.donate, name='donate'),
    url(r'^approve', views.approve, name='approve'),
    url(r'^unapprove/(?P<donation_id>[0-9]+)', views.unapprove, name='unapprove'),
]

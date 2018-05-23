from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^$', views.Home.as_view(), name='url_name_home'),
    url(r'^write/$', views.Write.as_view(), name='write'),
 
]
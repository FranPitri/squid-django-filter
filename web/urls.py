from django.conf.urls import url
from .views import home, permissions, groups
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'rules/$', permissions, name='permissions'),
    url(r'groups/$', groups, name='groups'),
]

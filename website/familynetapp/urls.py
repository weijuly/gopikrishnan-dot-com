from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from familynetapp import apis

urlpatterns = [
    url(r'^_api/persons/$', apis.person_list, name='person_list'),
    url(r'^_api/persons/(?P<pk>[0-9]+)/$', apis.person_detail, name='person_detail'),
    url(r'^_api/relations/$', apis.relation_list, name='relation_list'),
    url(r'^_api/relations/(?P<pk>[0-9]+)/$', apis.relation_detail, name='relation_detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

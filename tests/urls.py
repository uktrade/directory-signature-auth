from django.urls import re_path, include
from django.http import HttpResponse
from django.views import View


class TestView(View):
    def get(self, *args, **kwargs):
        return HttpResponse()


namespace_urls = [
    re_path(
        r'url-three',
        TestView.as_view(),
        name='url-three',
    ),
]


urlpatterns = [
    re_path(
        r'url-one',
        TestView.as_view(),
        name='url-one'
    ),
    re_path(
        r'url-two',
        TestView.as_view(),
        name='url-two'
    ),
    re_path(r'^blah/', include((namespace_urls, 'blah'), namespace='blah')),
]

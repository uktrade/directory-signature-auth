from django.urls import re_path
from django.http import HttpResponse
from django.views import View


class TestView(View):
    def get(self, *args, **kwargs):
        return HttpResponse()


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
]

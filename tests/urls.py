from django.conf.urls import url
from django.http import HttpResponse
from django.views import View


class TestView(View):
    def get(self, *args, **kwargs):
        return HttpResponse()


urlpatterns = [
    url(
        r'url-one',
        TestView.as_view(),
        name='url-one'
    ),
    url(
        r'url-two',
        TestView.as_view(),
        name='url-two'
    ),
]

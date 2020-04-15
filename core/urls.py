from django.conf.urls import url
from core import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name="core/robots.txt", content_type='text/plain')),
    url(r'^$', views.home, name='home'),
    url(r'^report', views.get_report, name='report'),
    url(r'^numbers', views.get_numbers, name='numbers'),
    url(r'^username', views.get_username, name='username'),
    url(r'^predictions', views.predictions_set, name='predictions'),
    url(r'^winners', views.winners, name='winners'),
]

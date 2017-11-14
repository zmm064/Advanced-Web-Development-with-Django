from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.VoteView.as_view()),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view()),
]

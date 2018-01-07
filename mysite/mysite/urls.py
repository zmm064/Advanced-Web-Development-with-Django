from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]

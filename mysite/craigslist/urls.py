from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'/login/^$', views.login, name='login'),  # redirect to index
    url(r'^(?P<city_id>[0-9]+)/$', views.city, name='city'),
    url(r'^(?P<city_id>[0-9]+)/listings/$', views.listings, name='listings'),
    # url(r'^(?P<city_id>[0-9]+)/listings/detail$', views.detail, name='detail'),
    url(r'^/listings/add$', views.ListingCreate.as_view(), name='listing-add')


]
#  ad a login and logout url. that way you can route a user with a link

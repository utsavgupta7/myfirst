from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from myfirst.views import hello,time,multiplication,greetings,report
from myfirst.books import views

urlpatterns = patterns('',(r'^hello/$',hello),(r'^time/$',time),(r'^multiply/(\d+)/(\d+)/$',multiplication),(r'^greet/([A-Za-z]+)/([A-Za-z]+)/$',greetings),(r'^admin/',include(admin.site.urls)),(r'^report/$',report),(r'^search-form/$',views.search_form), )

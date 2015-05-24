# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello_django.views import index, register, hello_world, login, ask, test, question, add, tags, logout, user, voted

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_kir.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^hello_world$', hello_world, name='hello_world'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^question/(?P<pk>[0-9]+)?/?$', question, name='question'),
    url(r'^test/$', test, name='test'),
    url(r'^add/$', add, name='add'), 
    url(r'^tags/(P<tag>)?$', tags, name='tags'),
    url(r'^user/(?P<pk>[0-9]+)?/?$', user, name="user"),
    url(r'^rated(?P<vote>up|down)/$', voted, name="vote"),    
)

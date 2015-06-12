"""pupilsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Students urls
    url(r'^$', 'pupils.templates.views.pupils.pupils_list', name='home'),

    url(r'^pupils/add/$', 'pupils.templates.views.pupils.pupils_add', name='pupils_add'),

    url(r'^pupils/(?P<sid>\d+)/edit/$', 'pupils.templates.views.pupils.pupils_edit', name='pupils_edit'),

    url(r'^pupils/(?P<sid>\d+)/delete/$', 'pupils.templates.views.pupils.pupils_delete', name='pupils_delete'),

    # Groups urls
    url(r'^groups/$', 'pupils.templates.views.groups.groups_list', name='groups'),

    url(r'^groups/add/$', 'pupils.templates.views.groups.groups_add', name='groups_add'),

    url(r'^groups/(?P<gid>\d+)/edit/$', 'pupils.templates.views.groups.groups_edit', name='groups_edit'),

    url(r'^groups/(?P<gid>\d+)/delete/$', 'pupils.templates.views.groups.groups_delete', name='groups_delete'),

    # Journal urls
    url(r'^journal/$', 'pupils.templates.views.journal.journal_list', name='journal'),

    url(r'^journal/pupil/(?P<gid>\d+)/$', 'pupils.templates.views.journal.journal_pupil', name='journal_pupil'),

    url(r'^journal/groups/(?P<gid>\d+)/$', 'pupils.templates.views.journal.journal_group', name='journal_group'),

    url(r'^admin/', include(admin.site.urls)),
)

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views import generic as cbv

urlpatterns = patterns(
    '',
    url(r'^$', cbv.TemplateView.as_view(template_name="main.html"), name='main')
)
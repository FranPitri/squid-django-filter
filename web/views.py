# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(req):
    context = {}
    context['site_header'] = 'Squid'
    return render(req, 'modules/home.html', context)

def permissions(req):
    context = {}
    context['site_header'] = 'Squid'
    return render(req, 'modules/permissions.html', context)

def groups(req):
    context = {}
    context['site_header'] = 'Squid'
    return render(req, 'modules/groups.html', context)
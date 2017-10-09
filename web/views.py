# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import GoupsForm
from django.shortcuts import render


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
    if req.method == 'POST':
        form = GoupsForm(req.POST)
        context['form'] = form
        if form.is_valid():
            pass
    else:
        context['form'] = GoupsForm()
        return render(req, 'modules/groups.html', context)

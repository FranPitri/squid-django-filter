# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Workstation, WorkGroup, Permission, PermissionsGroup

# Register your models here.

admin.site.register(Workstation)
admin.site.register(WorkGroup)
admin.site.register(Permission)
admin.site.register(PermissionsGroup)
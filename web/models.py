# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid


class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


class PermissionsGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    permissions = models.ManyToManyField(Permission)


class WorkGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    title = models.CharField(max_length=255, null=False, blank=False)
    permissions_group = models.ForeignKey(PermissionsGroup)


class Workstation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    ip = models.GenericIPAddressField(protocol='IPv4')
    permissions_group = models.ForeignKey(PermissionsGroup, null=False, blank=True)
    workgroup = models.ForeignKey(WorkGroup)

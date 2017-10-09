from django import forms
from django.contrib import admin
from .models import WorkGroup
from .models import PermissionsGroup
# from mptt.forms import TreeNodeMultipleChoiceField
from django.contrib.auth.models import User


class GoupsForm(forms.Form):
    title = forms.CharField(label='Titulo')
    permissions_group = forms.ModelChoiceField(queryset=PermissionsGroup.objects.all())
    users = forms.ModelMultipleChoiceField(
        required=False,
        queryset=User.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Categories', False))

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n',)

    class Meta:
        model = WorkGroup
        fields = ('title', 'permissions_group')

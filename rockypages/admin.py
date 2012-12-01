from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.admin import FlatpageForm
from reversion.admin import VersionAdmin
from flatblocks.models import FlatBlock


class FlatPageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))
    content = forms.CharField(widget=CKEditorWidget(), label=_("Content"))
    class Meta:
        model = FlatPage


class FlatPageAdmin(VersionAdmin):
    form = FlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

class FlatBlockAdmin(VersionAdmin):
    pass
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)

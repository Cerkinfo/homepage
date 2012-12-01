from django import forms
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from flatblocks.models import FlatBlock


class FlatBlockSimpleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label=_("Content"))
    class Meta:
        model = FlatBlock
        fields = ('header', 'content')

class FlatPageSimpleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label=_("Content"))
    class Meta:
        model = FlatPage
        fields = ('content',)

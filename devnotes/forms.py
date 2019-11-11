from django import forms
from .models import Devnote
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z_@./#&+-,! ]*$', 'Only alphanumeric characters with _@./#&+- \
    are allowed.')

class DevnoteForm(forms.ModelForm):
    """form to add django devnote"""
    name = forms.CharField(max_length=255, validators=[
        alphanumeric])
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Devnote
        fields = ['name', 'description']

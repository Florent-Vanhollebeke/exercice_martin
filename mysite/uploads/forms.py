from django import forms
from django.forms import ModelForm
from uploads.models import Person, File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = [
            "title",
            "content",
        ]


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
        ]

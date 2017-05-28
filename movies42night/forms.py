from django import forms

from movies42night.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title',)


class MovieProcessForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ()

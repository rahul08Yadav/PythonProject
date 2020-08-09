from django import forms


class IndexForm(forms.Form):
    post = forms.CharField()

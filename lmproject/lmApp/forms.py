from django import forms
class Emailsendform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.EmailField(required=False,widget=forms.Textarea)

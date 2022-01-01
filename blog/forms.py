from django import forms


class WhoAreYouForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=7)
    your_age = forms.IntegerField(label='Your age')
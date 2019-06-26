from django import forms


class NameForm(forms.Form):
    min = forms.IntegerField(label='min', min_value=0)
    max = forms.IntegerField(label='max', max_value=1000)


class MainForm(forms.Form):
    minimum = forms.IntegerField(label='minimum', min_value=0)
    maximum = forms.IntegerField(label='maximum', max_value=1000)

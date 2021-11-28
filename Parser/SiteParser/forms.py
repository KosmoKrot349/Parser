from django import forms

class Filter(forms.Form):
    filterField = forms.CharField(max_length=9999, label='search')

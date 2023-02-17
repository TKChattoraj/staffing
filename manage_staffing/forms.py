from django import forms

class LogInForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

    
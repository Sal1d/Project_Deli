from django.contrib.auth import get_user_model
from django import forms
from django.utils.safestring import mark_safe

from main.models import Book


class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Login', max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                                                'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                             'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                                           'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'surname', 'username',  'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CreateBookForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'text')
        exclude = ['author']


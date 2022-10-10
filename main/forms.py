from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser
from django.utils.safestring import mark_safe

from main.models import Book


class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Login', max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                                                'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               error_messages={'unique': "A user with that username already exists."})
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             error_messages={'unique': "A user with that email already exists."})
    phone = forms.CharField(label='Phone (Format: 8 999 999 99 99)', widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={'unique': "A user with that phone already exists."})
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                                   'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                                           'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'surname', 'username',  'email', 'phone', 'password2')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def clean_phone(self):
        int_list = '0123456789'
        phone = self.cleaned_data.get('phone')
        if len(phone) != 11:
            raise forms.ValidationError('Check your phone number')
        elif phone[0] != '8':
            raise forms.ValidationError('Your phone number must start with 8')
        else:
            for i in phone:
                if i not in int_list:
                    raise forms.ValidationError('Check your phone number')
        return phone


class CreateBookForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'text')
        exclude = ['author']


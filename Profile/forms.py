from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

INPUT_CLASS = (
    "w-full bg-slate-800 border border-slate-700 text-slate-100 "
    "placeholder-slate-500 rounded-lg px-4 py-2.5 text-sm "
    "focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-transparent "
    "transition duration-150"
)

SELECT_CLASS = (
    "w-full bg-slate-800 border border-slate-700 text-slate-100 "
    "rounded-lg px-4 py-2.5 text-sm "
    "focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-transparent "
    "transition duration-150"
)

FILE_CLASS = (
    "w-full text-sm text-slate-400 "
    "file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 "
    "file:text-sm file:font-medium file:bg-amber-400 file:text-slate-900 "
    "hover:file:bg-amber-300 cursor-pointer"
)
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered")

        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASS})
            field.help_text = None

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if username :
            qs_username = User.objects.filter(username=username)
            if self.instance.pk:
                qs_username = qs_username.exclude(pk=self.instance.pk)
            if qs_username.exists():
                self.add_error('username', "Username is already taken")
        if email :
            qs_email=User.objects.filter(email=email)
            if self.instance.pk:
                qs_email=qs_email.exclude(pk=self.instance.pk)
            if qs_email.exists():
                self.add_error('email', "Email is already registered")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASS})
            field.help_text = None


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'phone', 'gender']
        labels = {
            'picture': 'Profile Photo',
            'phone': 'Phone Number',
            'gender': 'Gender',
        }
        widgets = {
            'picture': forms.FileInput(attrs={
                'placeholder': 'Choose profile photo',
                'class': FILE_CLASS,
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': INPUT_CLASS,
            }),
            'gender': forms.Select(attrs={
                'class': SELECT_CLASS,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'Select gender')] + Profile.gender_choices
        self.fields['phone'].widget.attrs.update({'class': INPUT_CLASS})
        self.fields['gender'].widget.attrs.update({'class': SELECT_CLASS})
        self.fields['picture'].widget.attrs.update({'class': FILE_CLASS})
        for field in self.fields.values():
            field.help_text = None

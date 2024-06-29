from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label= _('Old Password'),strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'curent-password','autofocus':'True','class':'form_control'}))
    new_password1 = forms.CharField(label=_('New password'),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password','class':'form_control'}),
    help_text = password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password','class':'form_control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New password'),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password','class':'form_control'}),
    help_text = password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password','class':'form_control'}))

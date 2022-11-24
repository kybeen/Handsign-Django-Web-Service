import re
from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ValidationError

def username_validator(value):
    if re.search('[^A-Za-z0-9_@.+-]', value):
        raise ValidationError('8자이상 150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.')

class UserCreationForm(forms.Form):
    username = forms.CharField(label='사용자 이름', max_length=150, validators=[username_validator, MinLengthValidator(8)])
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(), validators=[MinLengthValidator(8)])
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('비밀번호가 일치하지 않습니다.')
        return password2

    def clean(self):
        username = self.cleaned_data.get('username') 
        password1 = self.cleaned_data.get('password1')

        if username and password1 and password1.startswith(username):
            raise ValidationError('사용자 이름과 비밀번호가 유사합니다.')

        return self.cleaned_data

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 要和form表单的名称相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)



class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
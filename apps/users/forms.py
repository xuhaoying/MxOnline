from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    # 定义的名字要和form表单的名称相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    # 注册表单
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码, 定制错误信息
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birthday', 'address', 'mobile']
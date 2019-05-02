from django import forms

class LoginForm(forms.Form):
    # 要和form表单的名称相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
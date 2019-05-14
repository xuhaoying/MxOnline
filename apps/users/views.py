from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import *


# 用户认证
class CustomBackend(ModelBackend):
    # 该方法被自动调用, 完成后台逻辑
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 用户可以使用用户名或者邮箱登录
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 把密码加密后对比
            if user.check_password(password):
                return user  # 验证成功
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form,
        })


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 向数据库发起验证
            user = authenticate(username=username, password=password)
            if user is not None:
                # django 登录
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {'msg': '用户名或密码错误'})
        else:
            return render(request, "login.html",{'login_form': login_form})




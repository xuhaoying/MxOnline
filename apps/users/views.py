from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            return render(request, "index.html")

    elif request.method == 'GET':
        return render(request, 'login.ht ml', locals())
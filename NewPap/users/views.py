from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
        if user and user.is_active:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('news:post_list'))
        else:
            form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    dj_logout(request)
    return render(request, 'logout_user.html')

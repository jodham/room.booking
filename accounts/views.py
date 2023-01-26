from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.forms import accountCreation


# Create your views here.
def register(request):
    if request.method == "POST":
        form = accountCreation(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, "successfully created account")
            return redirect('dashboard')
    else:
        form = accountCreation()
    templatename = 'accounts/register.html'
    context = {'form': form}
    return render(request, templatename, context)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'invalid details'
            templatename = 'accounts/login.html'
            context = {'error': error}
            return render(request, templatename, context)
    else:
        return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return redirect('index')

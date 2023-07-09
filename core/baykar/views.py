from django.shortcuts import render
from django.contrib.auth import authenticate
import requests
from django.shortcuts import redirect
from django.contrib import messages
import json
import pytz
import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from baykar.models import Profil

# Create your views here.




def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return HttpResponseRedirect('/login')

def loginpage(request):
    return render(request, 'login.html')

def registerpage(request):
    if request.method == "POST":
        SUCCESS_CODE = 201
        NO_CONTENT_CODE = 204
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["password2"]

        credentials = {
            'username': email,
            'email': email,
            'password1': password1,
            'password2': password2,
        }

        response = requests.post(
            url="http://127.0.0.1:8000/rest-auth/registration/",
            data=credentials
        )

        status_code = response.status_code

        if status_code == SUCCESS_CODE:
            user = authenticate(request, username=email, password=password1)
            profil = Profil(user=user, name=name, surname=surname)
            profil.save()

            request.session['token'] = response.json()['key']
            request.session.modified = True

            return redirect('login')

        if status_code == NO_CONTENT_CODE:
            user = authenticate(request, username=email, password=password1)
            profil = Profil(user=user, name=name, surname=surname)
            profil.save()


            return redirect('login')


        return render(request, 'register.html', {'err': json.loads(response.content)})

    return render(request, 'register.html')

def profilpage(request):
    if request.user.is_authenticated:
        return render(request, 'profil.html')
    return HttpResponseRedirect('/login')


def ihapage(request):
    if request.user.is_authenticated:

        act_user = User.objects.filter(is_active=True)

        return render(request, 'iha.html', {'users': act_user})
    return HttpResponseRedirect('/login')

def kiralamapage(request):
    if request.user.is_authenticated:

        act_user = User.objects.filter(is_active=True)

        return render(request, 'kiralama.html', {'users': act_user})
    return HttpResponseRedirect('/login')

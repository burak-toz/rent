from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, logout, login
import requests
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
import json

from baykar.models import Profil


def loginControl(request):
    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        try:
            u = get_object_or_404(User, email=email)
            user = authenticate(request, username=u.username, password=password)
            if user is not None:
                login(request, user)

                credentials = {
                    'username': u.username,
                    'password': password,
                }

                response = requests.post(
                    url="http://127.0.0.1:8000/rest-auth/login/",
                    data=credentials
                )
                request.session['token'] = response.json()['key']
                request.session.modified = True

                return redirect('homepage')

        except Exception as e:
            return redirect('login')
        return redirect('homepage')

def logoutControl(request):
	logout(request)
	return redirect('login')

def register(request):
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

        print(response.status_code)
        print(type(response.status_code))
        print(SUCCESS_CODE)
        print(type(SUCCESS_CODE))

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

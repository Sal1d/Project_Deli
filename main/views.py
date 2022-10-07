from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse

from main.forms import AuthenticationForm, UserRegistrationForm


def index(request):
    return render(request, 'main/index.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('NO 1')
            else:
                return HttpResponse('NO 2')
    else:
        form = AuthenticationForm()
    return HttpResponse('NO 3')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return HttpResponse('REG 3')
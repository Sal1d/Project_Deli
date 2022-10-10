from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse
import requests
from datetime import datetime
from djangoProject.settings import LOGIN_REDIRECT_URL
from main.forms import AuthenticationForm, UserRegistrationForm, CreateBookForm
from main.models import Book


def get_time():
    response = requests.get(url='https://yandex.com/time/sync.json?geo=67')
    data_time = response.json()
    unix_time = data_time.get('time')//1000
    time = datetime.utcfromtimestamp(int(unix_time)).strftime('%A, %d.%m.%y %H:%M')
    return time


def home(request):
    time = get_time()
    return render(request, 'main/home.html', {'time': time})


def success(request):
    time = get_time()
    return render(request, 'main/addbook.html', {'time': time})


def all_books(request):
    book_list = Book.objects.all()
    book_list = book_list[::-1]
    time = get_time()
    return render(request, 'main/allbooks.html', {'book_list': book_list, 'time': time})


def detail_book(request, book_id):
    a = Book.objects.get(id=book_id)
    time = get_time()
    return render(request, 'main/book.html', {'book': a, 'time': time})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return JsonResponse(data={}, status=201)
                else:
                    return HttpResponse('YOU BANNED')
            else:
                return JsonResponse(data={'error': "Wrong login or password"},
                                    status=400)
        else:
            return JsonResponse(
                data={'errors': form.errors},
                status=400,
            )
    else:
        form = AuthenticationForm()
    return HttpResponse('NO 3')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return JsonResponse(data={}, status=201)
        return JsonResponse(
            data={'errors': user_form.errors},
            status=400,
        )


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


@login_required(login_url=LOGIN_REDIRECT_URL)
def book_add(request):
    time = get_time()
    if request.method == 'POST':
        form = CreateBookForm(request.POST or None)
        if form.is_valid():
            book = form.save()
            book.author = request.user
            book.save()
            return JsonResponse(data={}, status=201)
        else:
            return JsonResponse(
                data={'error': 'Проверьте поля Title and Text'},
                status=400
            )
    return render(request, 'main/createnewbook.html', {'time': time})

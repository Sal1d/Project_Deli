from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse

from djangoProject.settings import LOGIN_REDIRECT_URL
from main.forms import AuthenticationForm, UserRegistrationForm, CreateBookForm
from main.models import Book


def home(request):
    return render(request, 'main/home.html')


def success(request):
    return render(request, 'main/addbook.html')

def all_books(request):
    book_list = Book.objects.all()
    book_list = book_list[::-1]
    return render(request, 'main/allbooks.html', {'book_list': book_list})


def detail_book(request, book_id):
    a = Book.objects.get(id=book_id)
    return render(request, 'main/book.html', {'book': a})


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
                return JsonResponse(data={'error': "Неверный логин или пароль"},
                                    status=400)
        else:
            return JsonResponse(
                data={'error': 'Введите логин или пароль'},
                status=400
            )
    else:
        form = AuthenticationForm()
    return HttpResponse('NO 3')


def user_login22(request):
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
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return HttpResponse('REG 3')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


@login_required(login_url=LOGIN_REDIRECT_URL)
def book_add(request):
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
    return render(request, 'main/createnewbook.html')

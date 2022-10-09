from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.all_books, name='all_books'),
    path('createbook/', views.book_add, name='book_add'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('book/<int:book_id>', views.detail_book, name='detail_book'),
    path('success/', views.success, name='success'),
]

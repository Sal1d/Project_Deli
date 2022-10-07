from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, surname, password, phone):
        user = self.model(email=email, username=username, first_name=first_name, surname=surname, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, surname, password, phone):
        user = self.create_user(email=email, username=username, first_name=first_name,
                                surname=surname, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        print(username_)
        return self.get(username=username_)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email', 'first_name', 'surname', 'phone']
    USERNAME_FIELD = 'username'

    object = CustomAccountManager()

    def get_name(self):
        return self.username

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.username



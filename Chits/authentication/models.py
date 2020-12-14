from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):

    def create_user(self, email,username, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, username ,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                   'email': 'email'}
class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )
    # DECIGNATION = (
    #     ("HR", "HR"),
    #     ("Software Development", "Software Development"),
    #     ("System Admin", "System Admin"),
    #     ("Service Desk", "Service Desk")
    # )
    firstname = models.CharField(max_length=255,unique=False)
    lastname = models.CharField(max_length=255, unique=False)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    # image = models.ImageField(upload_to='Pictures/%Y/%m/%d/', null=True, max_length=255)
    gender = models.CharField(max_length=255,choices=CHOICES,db_index=True)
    # dob = models.DateField(verbose_name='Date of birth',null=True)
    # designation = models.CharField(max_length=255,db_index=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=False)
    username = models.CharField(max_length=255, unique=True, db_index=True, default=None)


    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


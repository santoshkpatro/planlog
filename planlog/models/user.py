from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from planlog.models.base import BaseUUIDTimeStampedModel
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None):
        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email address')

        if not full_name:
            raise ValueError('Users must have an full name')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.is_email_verified = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            full_name=full_name,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(BaseUUIDTimeStampedModel, AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=155, unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)

    google_id = models.CharField(max_length=200, blank=True, null=True)
    github_id = models.CharField(max_length=200, blank=True, null=True)

    password_reset_required = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    last_login_at = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    login_count = models.PositiveIntegerField(default=0)
    login_failed_attempts = models.PositiveIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email

    def avatar_url(self):
        if not self.avatar:
            return None
        return "assets.planlog.in/%s".format(self.avatar)

    def access_token(self):
        return str(AccessToken.for_user(self))

    def refresh_token(self):
        return str(RefreshToken.for_user(self))

    """Admin panel config"""

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

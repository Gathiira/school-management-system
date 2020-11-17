from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )

        user.is_admin =True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    """
    docstring
    """
    username = None
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Does the user has specific permissions ??

        """
        return True

    def has_module_perm(self, app_label):
        """
        Does the user has permissions to view the app 'app_label'
        """

        return True

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    preffered_name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='profile-images', height_field=None, width_field=None, max_length=None, blank=True)
    discord_name = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    linkedin_profile_url = models.CharField(max_length=255)

    LEVELS = [
        ('BEGINNER', 'BEGINNER'),
        ('INTERMEDIATE', 'INTERMEDIATE'),
        ('EXPERT', 'EXPERT')
    ]
    current_level = models.CharField(max_length=255, choices=LEVELS)

    GENDER = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    ]

    gender = models.CharField(max_length=255, choices=GENDER)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
"""NOT READY"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .choices import *

class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, education_level='Lise', age=18, gender='Erkek', registiration_date=timezone.now, active=True, password = None):
        if not email or not name or not surname:
            raise ValueError("E-mail, isim, soyisim alanları boş kalamaz.")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.name, user_obj.surname = name, surname
        user_obj.age = age
        user_obj.gender = gender
        user_obj.education_level = education_level
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, name, surname, education_level='Lise', age=18, gender='Erkek', registiration_date=timezone.now, active = True, password = None):
        user = self.create_user(
            email,
            password = password,
            name = name,
            surname = surname,
            age = age,
            gender = gender,
            education_level = education_level,
            active = active,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, education_level='Lise', age=18, gender='Erkek', registiration_date = timezone.now, active = True, password = None):
        user = self.create_user(
            email,
            password = password,
            name = name,
            surname = surname,
            age = age,
            gender = gender,
            education_level = education_level,
            active = active,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    owner_id = models.IntegerField(unique = True, primary_key=True, verbose_name='User ID')
    email = models.EmailField(max_length=255, default=True, unique=True, verbose_name='E-Mail')
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    registiration_date = models.DateTimeField(
        verbose_name='Registiration Date',
        default=timezone.now
    )
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Erkek')
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='Lise')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'surname',
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name + self.surname

    def get_short_name(self):
        return self.name

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
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin



"""To extend the data"""
# class Profile(models.Model):
#     user = models.OneToOneField(User)

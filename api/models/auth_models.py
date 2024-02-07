
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from .base_models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self,
                     email,
                     password=None,
                     group_name=None,
                     **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        group = None

        # assign group
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                raise ValueError("Invalid group name.")

        user.save(using=self._db)

        if group:
            user.groups.add(group)

    def create_user(self, email,password=None, group_name=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email=email, password=password, group_name=group_name**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

    def set_initial_password(self, id, password):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise ValueError("Invalid user id.")

        if user.has_usable_password():
            raise ValueError("User password is already set.")

        user.set_password(password)
        user.is_active = True
        user.save()

        return user
    
class User(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=False)
    phone = PhoneNumberField(null=True,unique=True)
   
    last_login = models.DateTimeField(
        verbose_name=_('Last login datetime'),
        blank=True,
        null=True,
    )

    REQUIRED_FIELDS = []
    


    objects = UserManager()
    
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"




    def soft_delete(self):
        self.is_active = False
        

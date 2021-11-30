from django.db import models

# Custom user models for makking email as username 

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from accounts.models import User






class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    ROLES = (

        ('Mentor', 'Mentor'),
        ('User', 'User'),

        )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    roles = models.CharField(max_length=50, choices = ROLES, null=True)
    objects = UserManager() 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class TimestampedModel(models.Model):
    '''
    Timestamped Model  
    Common for all 
    '''
    create_date = models.DateTimeField(('Create Date'), auto_now_add=True, null=True, blank=True)
    modify_date = models.DateTimeField(('Modify Date'), auto_now=True, null=True, blank=True)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user',null=True, blank=True)
    modified_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_user',null=True, blank=True)

    class Meta:
        abstract = True
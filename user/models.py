from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, name, username, password=None):
        if not email:
            raise ValueError('Email must be provided.')
        if not name:
            raise ValueError('Name must be provided.')
        if not username:
            raise ValueError('Username must be provided.')
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            name=name,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, username, password=None):
        user = self.create_user(email, name, username, password)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user
    

class RHQUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=60, unique=True)
    phone = models.CharField(max_length=14)
    image = models.ImageField(upload_to='UserImage/', null=True, blank=True)
    date_joined = models.DateTimeField(default=now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.email 
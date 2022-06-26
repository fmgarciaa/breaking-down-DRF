from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    """Custom user mamanger.
    
    """
    def create_user(self, email, username, name, last_name, password=None):
        if not email:
            raise ValueError('an email is required!')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            name = name,
            last_name = last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, name, last_name, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            name = name,
            last_name = last_name
        )
        user.is_staff = True
        user.save()
        return user
        
    

class User(AbstractBaseUser):
    """Custom user.

    """
    username = models.CharField('username',unique=True, max_length=50)
    email = models.EmailField('email', max_length=254, unique=True)
    name = models.CharField('name', max_length=50, blank=False, null=False)
    last_name = models.CharField('last_name', max_length=50, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self) -> str:
        return f'{self.name},{self.last_name}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_staff

    



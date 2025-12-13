from django.db import models 
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

# create model class
class UserManager(BaseUserManager) :
    def create_user(self,email,password,**extra_fields) :
        if not email :
            raise ValueError(_('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields) :
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_superuser') is not True :
            raise ValueError(_('superuser must have is_superuser=True'))
        if extra_fields.get('is_staff') is not True :
            raise ValueError(_('superuser must havr is_staff=True'))
        
        return self.create_user(email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin) :
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Profile(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs) :
    if created :
        Profile.objects.create(user=instance)
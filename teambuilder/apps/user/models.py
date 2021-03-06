from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('The user must have an email')
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    REGION = ((u'NA', u'North America'), (u'EUW', u'Europe West'), (u'EUN', u'Europe Nordic & East'), (u'BR',u'Brazil'), (u'TR', u'Turkey'), (u'RU', u'Russia'), (u'LAN', u'Latin America North'), (u'LAS', u'Latin America South'), (u'OCE', u'Oceania'))
    email = models.EmailField(verbose_name='Email', unique=True, db_index=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True)
    lol_id = models.IntegerField(verbose_name='League of legends summoner\'s id', max_length=10, null=True, blank=True)
    region = models.CharField(verbose_name='Server', max_length=3, choices=REGION, blank=True)
    in_game_name =  models.CharField(verbose_name='In Game Name', max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    register_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label='user'
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-register_date',]

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_in_game_name(self):
        if self.in_game_name is not None:
            return True
        else:
            return False
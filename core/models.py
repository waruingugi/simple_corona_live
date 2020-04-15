from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from corona.settings import ADMIN_USERNAME
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Users(AbstractBaseUser):
    time_stamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        blank=True, null=True, unique=True, max_length=10)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return (self.username == ADMIN_USERNAME)

    @property
    def is_staff(self):
        return (self.username == ADMIN_USERNAME)

    def has_perm(self, perm, obj=None):
        return (self.username == ADMIN_USERNAME)

    def has_module_perms(self, app_label):
        return (self.username == ADMIN_USERNAME)


class Choices(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    answers = ArrayField(
        models.CharField(max_length=200), blank=True, null=True
    )
    active_cases = models.IntegerField(default=0, null=True)
    new_cases = models.IntegerField(default=0, null=True)
    total_cases = models.IntegerField(default=0, null=True) 

    class Meta:
        verbose_name = 'Choice'

    def __str__(self):
        return ("Username:{} \t Answers:{}".format(
            self.user.username, self.answers
            )
        )

from weakref import proxy
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# # Create your models here.
# class User(AbstractUser):
#     class Types(models.TextChoices):
#         EMPLOYEE = "EMPLOYEE", "Employee"
#         EMPLOYER = "EMPLOYER", "Employer"
#     type = models.CharField(_('Type'),max_length=50, choices = Types.choices, default = Types.EMPLOYEE )
#     name = models.CharField(_("Name of User"), blank=True, max_length=255)

#     def get_absolute_url(self):
#         return reverse("users:detail", kwargs={"username": self.username})

# class Employee(User):
#     class Meta:
#         proxy = True

# class Employer(User):
#     class Meta:
#         proxy = True
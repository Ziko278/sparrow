from django.db import models
from django.contrib.auth.models import User
from sparrow_admin.models import SchoolsModel


# Create your models here.
class UserRoleModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

from django.db import models
from sparrow_admin.models import SchoolsModel
from registration.models import StaffModel, StudentsModel, ClassesModel

# Class model was moved to registration app to avoid circular importation


class SubjectsModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    teachers = models.ManyToManyField(StaffModel, blank=True)
    is_compulsory = models.BooleanField()
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.


class TimeTablesModel(models.Model):
    """"""
    school_class = models.ForeignKey(ClassesModel, blank=True, null=True, on_delete=models.SET_NULL)


class StudentPostsModel(models.Model):
    """"""
    role = models.CharField(max_length=100)
    role_description = models.TextField()
    role_player = models.ForeignKey(StudentsModel, null=True, blank=True, on_delete=models.SET_NULL)


class SchoolHolidayModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    date = models.DateTimeField()


class ClubsModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(StudentsModel, blank=True)


class ClubsPositionsModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    supervisor = models.ForeignKey(StaffModel, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(StudentsModel, blank=True)

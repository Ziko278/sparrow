from django.db import models
from sparrow_admin.models import SchoolsModel


# Create your models here.
class SessionModel(models.Model):
    dash_format = models.CharField(max_length=20)
    slash_format = models.CharField(max_length=20)
    SessionStatus = (
        ('a', 'ACTIVE'), ('p', 'PAST'), ('f', 'NEXT')
    )
    status = models.CharField(max_length=1, choices=SessionStatus)

    def __str__(self):
        return self.slash_format


class SparrowAdminAcademicSettingModel(models.Model):
    default_session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st TERM', '1st TERM'), ('2nd TERM', '2nd TERM'), ('3rd TERM', '3rd TERM')
    )
    default_term = models.CharField(max_length=10, choices=TERM)


class SchoolAdminAcademicSettingModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st TERM', '1st TERM'), ('2nd TERM', '2nd TERM'), ('3rd TERM', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)


class SchoolAdminResultSettingModel(models.Model):
    TEST_NO = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')
    )
    tests = models.CharField(max_length=2, choices=TEST_NO)
    assignments = models.BooleanField(default=True)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)

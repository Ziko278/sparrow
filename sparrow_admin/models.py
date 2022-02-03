from django.db import models
# from setting.models import SchoolAdminResultSettingModel
"""This is the models for all school data management"""


# Create your models here.
class SchoolsModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    line_one = models.CharField(max_length=15)
    line_two = models.CharField(max_length=15, null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY SCHOOL'),
        ('sec', 'SECONDARY SCHOOL'),
        ('mix', 'COMBINED SCHOOL'),
    )
    type = models.CharField(max_length=5, choices=TYPE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    applicant_phone = models.CharField(max_length=15)
    POSITION = (
        ('o', 'SCHOOL OWNER'),
        ('d', 'SCHOOL DIRECTOR'),
        ('s', 'SCHOOL STAFF'),
        ('ot', 'OTHER'),
    )
    applicant_position = models.CharField(max_length=5, choices=POSITION)
    status = models.CharField(max_length=15, default="new", blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    activation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # result_setting = models.OneToOneField(SchoolAdminResultSettingModel, on_delete=models.CASCADE,
    #                             related_name="result_setting", blank=True)

    def __str__(self):
        return self.name

    """def get_absolute_url(self):
        return reversed('', args=[str(self.id)])
    """


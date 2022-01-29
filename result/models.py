from django.db import models
from registration.models import StudentsModel
from basic.models import ClassesModel
from sparrow_admin.models import SchoolsModel


# Create your models here.
class ResultModel(models.Model):
    # assignment = models.FloatField(null=True, blank=True)
    # first_test = models.FloatField(null=True, blank=True)
    # second_test = models.FloatField(null=True, blank=True)
    # third_test = models.FloatField(null=True, blank=True)
    # fourth_test = models.FloatField(null=True, blank=True)
    # fifth_test = models.FloatField(null=True, blank=True)
    # sixth_test = models.FloatField(null=True, blank=True)
    # exam = models.FloatField(null=True, blank=True)
    # total = models.FloatField(null=True, blank=True)
    # grade = models.CharField(max_length=1, null=True, blank=True)
    # $table->string('remark')->nullable();
    # $table->string('uploadedBy');
    # $table->timestamps();

    session = models.CharField(max_length=20)
    # change session to foreign key
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM)
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    result = models.JSONField(null=True, blank=True)


class ResultStatisticModel(models.Model):
    session = models.CharField(max_length=20)
    # change session to foreign key
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM)
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    result_statistic = models.JSONField()


class ResultRemarkModel(models.Model):
    session = models.CharField(max_length=20)
    # change session to foreign key
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM)
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    result_remark = models.JSONField()
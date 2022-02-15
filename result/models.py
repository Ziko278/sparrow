from django.db import models
from registration.models import StudentsModel
from basic.models import ClassesModel, SubjectsModel
from sparrow_admin.models import SchoolsModel
from setting.models import SessionModel


# Create your models here.
class ResultModel(models.Model):
    assignment = models.FloatField(null=True, blank=True, default=0)
    first_test = models.FloatField(null=True, blank=True, default=0)
    second_test = models.FloatField(null=True, blank=True, default=0)
    third_test = models.FloatField(null=True, blank=True, default=0)
    fourth_test = models.FloatField(null=True, blank=True, default=0)
    fifth_test = models.FloatField(null=True, blank=True, default=0)
    sixth_test = models.FloatField(null=True, blank=True, default=0)
    exam = models.FloatField(null=True, blank=True, default=0)
    total = models.FloatField(null=True, blank=True)
    grade = models.CharField(max_length=1, null=True, blank=True)
    remark = models.CharField(max_length=5, null=True, blank=True)
    # $table->string('remark')->nullable();
    # $table->string('uploadedBy');
    # $table->timestamps();

    session = models.CharField(max_length=20, null=True, blank=True)
    # change session to foreign key
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, null=True, blank=True)
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE, related_name='student_result',
                                null=True, blank=True)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE, null=True, blank=True)
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.student}"


class TermResult(models.Model):
    result = models.ManyToManyField(ResultModel, related_name='term_result', blank=True)
    total = models.FloatField(null=True, blank=True)
    average = models.FloatField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=1, null=True, blank=True)
    remark = models.CharField(max_length=5, null=True, blank=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, null=True, blank=True)
    # change session to foreign key
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, null=True, blank=True)
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.session} {self.term} {self.student_class}"


class StudentResult(models.Model):
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE, related_name='student_in_result',
                                null=True, blank=True)
    results = models.ForeignKey(TermResult, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.student}"


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
